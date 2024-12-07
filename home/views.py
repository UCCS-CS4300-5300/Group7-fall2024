from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages
from django.contrib.messages import get_messages
from django.db import IntegrityError, transaction
from .models import RAM, CPU, Motherboard, Storage, Build, Profile, ShoppingCart, CartItem
from .forms import BuildForm
from .compatibility_service import CompatibilityService
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout as auth_logout
from django.conf import settings
from .services.paypal_service import create_payment
from django.http import JsonResponse
import paypalrestsdk


def index(request):
    """
    Render the index page.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: Renders the index.html template.
    """
    return render(request, 'index.html')


@login_required
def build(request):
    """
    Render the build page where users can create and manage their builds.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: Renders the build.html template with the user's build components.
    """
    profile = request.user.profile

    # Retrieve or create an active Build object for the user's profile
    build, created = Build.objects.get_or_create(
        profile=profile,
        is_active=True,
        defaults={'profile': profile, 'is_active': True}
    )

    # If the build was newly created, save it to generate a primary key (build_id)
    if created:
        build.save()

    # Deactivate other active builds for the profile
    Build.objects.filter(profile=profile, is_active=True).exclude(build_id=build.build_id).update(is_active=False)

    context = {
        'build': build,
        'cpu': build.cpu,
        'motherboard': build.motherboard,
        'ram_modules': build.ram.all(),  # Assuming ram is a ManyToManyField
        'storages': build.storages.all()  # Assuming storages is a ManyToManyField
    }
    return render(request, 'build.html', context)


def part_browser(request):
    # Handle logic here if needed, e.g., fetching all parts or filtering by category
    category = request.GET.get('category', 'All Categories')
    query = request.GET.get('q', '')
    results = []

    # You could add your filtering/search logic here based on the category and query if needed.
    # Example:
    if category == 'CPU':
        results = CPU.objects.filter(name__icontains=query)
    elif category == 'RAM':
        results = RAM.objects.filter(name__icontains=query)
    elif category == 'Motherboard':
        results = Motherboard.objects.filter(name__icontains=query)
    elif category == 'Storage':
        results = Storage.objects.filter(name__icontains=query)
    else:
        # Fetch all components
        results = list(CPU.objects.filter(name__icontains=query)) + \
                  list(RAM.objects.filter(name__icontains=query)) + \
                  list(Motherboard.objects.filter(name__icontains=query)) + \
                  list(Storage.objects.filter(name__icontains=query))

    return render(request, 'part_browser.html', {'results': results, 'query': query, 'category': category})


def pre_built(request):
    """
    Render the pre-built page where users can view pre-built PC configurations.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: Renders the pre_built.html template.
    """
    return render(request, 'pre_built.html')


def account_page(request):
    """
    Render the account page where users can manage their account information.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: Renders the account_page.html template.
    """
    profile = request.user.profile
    saved_builds = Build.objects.filter(profile=profile, is_complete=True)
    context = {
        'saved_builds': saved_builds,
    }

    return render(request, 'account_page.html')


def login_or_register(request):
    """
    Handle user login and registration. Present the login form to the user.
    Args:
        request (HttpRequest): The HTTP request object.
    Returns:
        HttpResponse: Renders the login.html template with the login form.
    """
    if request.method == 'POST':
        login_form = AuthenticationForm(request, data=request.POST)
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login successful.")
                return redirect('index')
            else:
                messages.error(request, "Invalid login credentials.")
        else:
            messages.error(request, "Invalid login form submission.")

    login_form = AuthenticationForm()
    return render(request, 'auth/login.html', {'login_form': login_form})


def get_ram_results(query):
    ram_results = RAM.objects.filter(
        Q(name__icontains=query) |
        Q(ram_type__type__icontains=query) |
        Q(ram_speed__speed__icontains=query) |
        Q(ram_capacity__capacity__icontains=query)
    ).distinct()
    for ram in ram_results:
        ram.category = 'RAM'
    return ram_results


def get_cpu_results(query):
    cpu_results = CPU.objects.filter(
        Q(name__icontains=query) |
        Q(manufacturer__name__icontains=query) |
        Q(microarchitecture__name__icontains=query) |
        Q(socket_type__name__icontains=query)
    ).distinct()
    for cpu in cpu_results:
        cpu.category = 'CPU'
    return cpu_results


def get_motherboard_results(query):
    motherboard_results = Motherboard.objects.filter(
        Q(name__icontains=query) |
        Q(manufacturer__name__icontains=query) |
        Q(cpu_socket_type__name__icontains=query) |
        Q(supported_ram_types__type__icontains=query) |
        Q(supported_ram_speeds__speed__icontains=query)
    ).distinct()
    for motherboard in motherboard_results:
        motherboard.category = 'Motherboard'
    return motherboard_results


def get_storage_results(query):
    storage_results = Storage.objects.filter(
        Q(name__icontains=query) |
        Q(form_factor__name__icontains=query) |
        Q(capacity__capacity__icontains=query) |
        Q(type__type__icontains=query)
    ).distinct()
    for storage in storage_results:
        storage.category = 'Storage'
    return storage_results


@login_required
def search_pc_parts(request):
    query = request.GET.get('q', '').strip()
    category = request.GET.get('category', 'All Categories')
    results = []

    if query:
        try:
            if category == 'All Categories' or category == 'RAM':
                results.extend(get_ram_results(query))

            if category == 'All Categories' or category == 'CPU':
                results.extend(get_cpu_results(query))

            if category == 'All Categories' or category == 'Motherboard':
                results.extend(get_motherboard_results(query))

            if category == 'All Categories' or category == 'Storage':
                results.extend(get_storage_results(query))
        except Exception as e:
            messages.error(request, f"An error occurred during the search: {e}")

    return render(request, 'part_browser.html', {'results': results, 'query': query, 'category': category})


def register_view(request):
    """
    Handle user registration.
    """
    if request.method == 'POST':
        register_form = UserCreationForm(request.POST)
        if register_form.is_valid():
            user = register_form.save()
            login(request, user)  # Log the user in after registration
            messages.success(request, "Registration successful.")
            return redirect('index')  # Redirect to your home page after successful registration
    else:
        register_form = UserCreationForm()

    return render(request, 'auth/register.html', {'register_form': register_form})


@login_required
def add_to_build(request, part_id, category):
    profile = request.user.profile

    # Retrieve the active build
    build = Build.objects.filter(profile=profile, is_active=True).first()

    if not build:
        messages.error(request, "No active build found. Please create a new build.")
        return redirect('build_page')

    # Add the part to the active build
    if category == 'CPU':
        part = get_object_or_404(CPU, cpu_id=part_id)
        build.cpu = part
    elif category == 'RAM':
        part = get_object_or_404(RAM, ram_id=part_id)
        build.ram.add(part)
    elif category == 'Motherboard':
        part = get_object_or_404(Motherboard, motherboard_id=part_id)
        build.motherboard = part
    elif category == 'Storage':
        part = get_object_or_404(Storage, storage_id=part_id)
        build.storages.add(part)

    build.save()  # Save the changes
    return redirect('build')


@login_required
def remove_from_build(request, category):
    # Get the active build for the user
    build = get_object_or_404(Build, profile__user=request.user, is_active=True)

    # Remove the specified component based on the category
    if category == 'CPU':
        build.cpu = None
    elif category == 'RAM':
        build.ram.clear()  # RAM is Many-to-Many
    elif category == 'Motherboard':
        build.motherboard = None
    elif category == 'Storage':
        build.storages.clear()  # Storage is Many-to-Many

    # Save the build
    build.save()

    return redirect('build')  # Redirect back to the build page


def view_profile(request):
    context = {
        'user' : request.username
    }

    return render(request, 'account_page.html', context)


def logout_user(request):
    logout(request)
    return redirect('index')


@login_required
def save_build(request):
    build_name = request.GET.get("build_name")
    profile = request.user.profile

    if not build_name:
        messages.error(request, "Build name cannot be empty.")
        return redirect('build')

    # Retrieve the active build
    current_build = Build.objects.filter(profile=profile, is_active=True).first()

    if not current_build:
        messages.error(request, "No active build found.")
        return redirect('build')

    # Check for duplicate names
    if Build.objects.filter(profile=profile, name=build_name).exists():
        messages.error(request, f"A build with the name '{build_name}' already exists.")
        return redirect('build')

    # Save components and mark the build as complete
    current_build.name = build_name
    current_build.is_active = False  # Mark build as inactive
    current_build.is_complete = True
    current_build.save()

    # Check compatibility after saving
    try:
        # compatibility service returns a tuple with contents:(bool, list[])
        # the first value in result will be false if the build is not valid. The second value is a list of all the error message
        result = CompatibilityService.check_build_compatibility(current_build) 
        if result[0] == False:
            print('\n'.join(result[1])) 
            raise ValueError('\n\n'.join(result[1])) # create the error message
        messages.success(request, "Build saved and is compatible!")

    except ValueError as e:
        #self.client.cookies.pop('messages')
        messages.warning(request, f"Build: {current_build.name} was saved but compatibility issues were detected:\n\n {e}")
        # redirect to an error page for that  build.
        return redirect('build_error', build_id=current_build.build_id)

    # Clear the builder page components
    Build.objects.create(profile=profile, is_active=True)  # Create a new active build
    messages.success(request, f"Build '{build_name}' saved successfully!")
    return redirect('account_page')


@login_required
def delete_build(request, build_id):
    build = get_object_or_404(Build, build_id=build_id, profile__user=request.user)
    build.delete()
    messages.success(request, "Build deleted successfully.")
    return redirect('account_page')


def edit_build(request, build_id):
    build = get_object_or_404(Build, build_id=build_id, profile__user=request.user)

    if request.method == "POST":
        form = BuildForm(request.POST, instance=build)
        if form.is_valid():
            # Save the form first to ensure build_id is generated
            build = form.save(commit=False)
            build.save()  # Save to get a primary key

            # Now set the many-to-many fields
            form.cleaned_data.get('ram') and build.ram.set(form.cleaned_data['ram'])
            form.cleaned_data.get('storages') and build.storages.set(form.cleaned_data['storages'])
            # Check compatibility after saving
            try:
                # compatibility service returns a tuple with contents:(bool, list[])
                # the first value in result will be false if the build is not valid. The second value is a list of all the error message
                result = CompatibilityService.check_build_compatibility(build) 
                if result[0] == False:
                    print('\n'.join(result[1])) 
                    raise ValueError('\n\n'.join(result[1])) # create the error message
                messages.success(request, "Build saved and is compatible!")

            except ValueError as e:
                #self.client.cookies.pop('messages')
                messages.warning(request, f"Build: {build.name} was saved but compatibility issues were detected:\n\n {e}")
                # redirect to an error page for that  build.
                return redirect('build_error', build_id=build_id)

            return redirect('account_page')
    else:
        form = BuildForm(instance=build)

    return render(request, 'edit_build.html', {'form': form})


def view_build(request, build_id):
    build = get_object_or_404(Build, build_id=build_id)
    return render(request, 'view_build.html', {'build': build})


@login_required
def add_to_cart(request, item_id, category):
    profile = request.user.profile
    cart, created = ShoppingCart.objects.get_or_create(profile=profile)

    # Fetch the part based on its category
    if category == "RAM":
        item = get_object_or_404(RAM, pk=item_id)
    elif category == "CPU":
        item = get_object_or_404(CPU, pk=item_id)
    elif category == "Motherboard":
        item = get_object_or_404(Motherboard, pk=item_id)
    elif category == "Storage":
        item = get_object_or_404(Storage, pk=item_id)
    else:
        messages.error(request, "Invalid category.")
        return redirect('part_browser')

    # Check if the part is already in the cart
    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        name=item.name,
        price=item.price,
        category=category
    )
    if not created:
        cart_item.quantity += 1
    cart_item.save()

    # Update cart's total price
    cart.total_price += item.price
    cart.save()

    messages.success(request, f"Added {item.name} to your cart.")
    return redirect('view_cart')


@login_required
def add_build_to_cart(request):
    profile = request.user.profile
    cart, created = ShoppingCart.objects.get_or_create(profile=profile)

    if request.method == "POST":
        build_name = request.POST.get("build_name", "").strip()
        if not build_name:
            messages.error(request, "Build name cannot be empty.")
            return redirect('add_build_to_cart')

        active_build = Build.objects.filter(profile=profile, is_active=True).first()
        if not active_build:
            messages.error(request, "No active build found to add to the cart.")
            return redirect('build')

        # Update the build's name and mark it as complete
        active_build.name = build_name
        active_build.is_active = False
        active_build.is_complete = True
        active_build.save()

        # Add the build to the cart
        CartItem.objects.create(
            cart=cart,
            name=active_build.name,
            price=sum((
                active_build.cpu.price if active_build.cpu else 0,
                active_build.motherboard.price if active_build.motherboard else 0,
                sum(ram.price for ram in active_build.ram.all()),
                sum(storage.price for storage in active_build.storages.all())
            )),
            is_build=True
        )

        # Clear the active build
        Build.objects.create(profile=profile, is_active=True)

        messages.success(request, f"Added build '{build_name}' to your cart and cleared the builder page.")
        return redirect('build')

    return render(request, 'add_build_to_cart.html')


def get_active_build(profile):
    active_build = Build.objects.filter(profile=profile, is_active=True).first()
    if not active_build:
        return None, "No active build found."
    return active_build, None


@login_required
def view_cart(request):
    profile = request.user.profile
    cart, created = ShoppingCart.objects.get_or_create(profile=profile)
    cart = get_object_or_404(ShoppingCart, profile=profile)
    cart_items = cart.cart_items.all()

    context = {
        'cart_items': cart_items,
        'total_price': sum(item.price * item.quantity for item in cart_items)
    }
    return render(request, 'cart.html', context)


@login_required
def remove_from_cart(request, item_id):
    profile = request.user.profile
    cart = get_object_or_404(ShoppingCart, profile=profile)

    cart_item = get_object_or_404(CartItem, cart=cart, id=item_id)

    # Update the total price
    cart.total_price -= cart_item.price * cart_item.quantity
    cart.total_price = max(cart.total_price, 0)  # Prevent negative total price
    cart.save()

    cart_item.delete()

    messages.success(request, f"Removed {cart_item.name} from your cart.")
    return redirect('view_cart')


@login_required
def add_saved_build_to_cart(request, build_id):
    profile = request.user.profile
    cart, created = ShoppingCart.objects.get_or_create(profile=profile)

    # Retrieve the saved build
    saved_build = get_object_or_404(Build, build_id=build_id, profile=profile)

    # Check if the build is already in the cart
    if CartItem.objects.filter(cart=cart, name=saved_build.name, category="Build").exists():
        messages.warning(request, f"The build '{saved_build.name}' is already in your cart.")
        return redirect('account_page')

    # Add the build to the cart as a CartItem
    CartItem.objects.create(
        cart=cart,
        name=saved_build.name,
        price=saved_build.get_total_price(),  # Calculate price dynamically
        category="Build",
        quantity=1
    )

    # Update the cart's total price
    cart.total_price += saved_build.get_total_price()
    cart.save()

    messages.success(request, f"'{saved_build.name}' has been added to your cart.")
    return redirect('account_page')


@login_required
def create_paypal_payment(request):
    # Example: Calculate the total price from the shopping cart
    profile = request.user.profile
    cart = profile.shoppingcart
    total_price = sum(item.price * item.quantity for item in cart.cart_items.all())

    # Create a PayPal payment
    payment = create_payment(total_price)

    if payment.create():
        # Redirect to PayPal approval URL
        for link in payment.links:
            if link.rel == "approval_url":
                return redirect(link.href)
    else:
        return render(request, "payment_error.html", {"error": payment.error})


def execute_paypal_payment(request):
    payment_id = request.GET.get('paymentId')
    payer_id = request.GET.get('PayerID')

    payment = paypalrestsdk.Payment.find(payment_id)
    if payment.execute({"payer_id": payer_id}):
        # Payment successful
        return render(request, "payment_success.html")
    else:
        # Payment failed
        return render(request, "payment_error.html", {"error": payment.error})


def test_paypal(request):
    try:
        # Attempt a simple request to PayPal
        paypalrestsdk.configure({
            "mode": settings.PAYPAL_ENVIRONMENT,
            "client_id": settings.PAYPAL_CLIENT_ID,
            "client_secret": settings.PAYPAL_CLIENT_SECRET
        })
        response = paypalrestsdk.Payment.all({"count": 1})
        return JsonResponse({"status": "success", "response": response.to_dict()})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)})


def purchase_confirmed(request):
    profile = request.user.profile

    # Clear the shopping cart
    shopping_cart, created = ShoppingCart.objects.get_or_create(profile=profile)
    shopping_cart.cart_items.all().delete()  # Remove all cart items
    shopping_cart.total_price = 0  # Reset the total price
    shopping_cart.save()

    # Render the confirmation page
    return render(request, 'purchase_confirmed.html', {'message': "Your payment was successful, and your cart has been cleared!"})


def build_error(request, build_id):
    storage = get_messages(request)
    print(storage)

    context = {
        'error_message': storage,
        'build_id' : build_id,
        'user' : ""
    }
    return render(request, 'build_error.html', context)
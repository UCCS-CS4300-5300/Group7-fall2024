import paypalrestsdk
from django.conf import settings


# Initialize PayPal SDK
paypalrestsdk.configure({
    "mode": settings.PAYPAL_ENVIRONMENT,  # "sandbox" or "live"
    "client_id": settings.PAYPAL_CLIENT_ID,
    "client_secret": settings.PAYPAL_CLIENT_SECRET
})


def create_payment(total_price, currency="USD"):
    """
    Creates a PayPal payment.
    """
    payment = paypalrestsdk.Payment({
        "intent": "sale",
        "payer": {
            "payment_method": "paypal"
        },
        "redirect_urls": {
            "return_url": "https://app-jzlotoff-5.devedu.io/purchase-confirmed/",
            "cancel_url": "https://app-jzlotoff-5.devedu.io/cart/"
        },
        "transactions": [{
            "amount": {
                "total": f"{total_price:.2f}",
                "currency": currency
            },
            "description": "PC Build Checkout"
        }]
    })
    return payment

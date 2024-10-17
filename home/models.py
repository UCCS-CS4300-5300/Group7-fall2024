from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# profile
class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE,)
    profile_name = models.CharField(max_length=20, blank=True)

	def __str__(self):
		return self.user.username

# Create a user Profile by default when user signs up
def create_profile(sender, instance, created, **kwargs):
	if created:
		user_profile = Profile(user=instance)
		user_profile.save()

post_save.connect(create_profile, sender=User) # automatically create a profile when user signs up

class Shopping_Cart(models.Model):
	profile = models.OneToOneField(Profile, on_delete=models.CASCADE)
    total_price = models.FloatField(default = 0.0)

	def __str__(self):
		return self.profile.profile_name

# container model for the parts of the PC
class Build(models.Model):
	profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    is_complete = models.BooleanField(default = False)

	mother_board = models.ForeignKey(Mother_Board, on_delete=models.CASCADE)
    cpu = models.ForeignKey(CPU, on_delete=models.CASCADE)
    memory = models.ForeignKey(Memory, on_delete=models.CASCADE)
	cpu_cooler = models.ForeignKey(CPU_Cooler, on_delete=models.CASCADE)
	storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
	power_supply = models.ForeignKey(Power_Supply, on_delete=models.CASCADE)
	fan = models.ForeignKey(Fan, on_delete=models.CASCADE)
	case = models.ForeignKey(Case, on_delete=models.CASCADE)

class Mother_Board(model.Model):
    #item_id
    #title
    #price
    #condition
    #category
    #seller_info
    #shipping_info

class CPU(model.Model):
    #item_id
    #title
    #price
    #condition
    #category
    #seller_info
    #shipping_info

class Memory(model.Model):
    #item_id
    #title
    #price
    #condition
    #category
    #seller_info
    #shipping_info

class CPU_Cooler(model.Model):
    #item_id
    #title
    #price
    #condition
    #category
    #seller_info
    #shipping_info

class Storage(model.Model):
    #item_id
    #title
    #price
    #condition
    #category
    #seller_info
    #shipping_info

class Power_Supply(model.Model):
    #item_id
    #title
    #price
    #condition
    #category
    #seller_info
    #shipping_info

class Fan(model.Model):
    #item_id
    #title
    #price
    #condition
    #category
    #seller_info
    #shipping_info

class Case(model.Model):
    #item_id
    #title
    #price
    #condition
    #category
    #seller_info
    #shipping_info

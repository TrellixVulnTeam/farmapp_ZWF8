from django.db import models
from django.contrib.auth.models import User

def upload_to(instance, filename):
    return 'user_profile_image/{}/{}'.format(instance.user.id, filename)

class UserDetails(models.Model):
    name = models.CharField(
        max_length=256, null=True)
    full_name = models.CharField(
        max_length=256, null=True)
    user = models.ForeignKey(User)
    email = models.EmailField(max_length=256)
    phone = models.BigIntegerField(default=0)
    proof = (
        ("Adhaar", "Adhaar"),
        ("VoterId", "VoterId"),
        ("RationId", "RationId"),
        ("PanId", "PanId"),
        ("Other", "Other")
    )
    idproof_type = models.CharField(max_length=25,
        null=True, blank=True, choices=proof)
    gender_ = (
        ("Male", "Male"),
        ("Female", "Female")
    )
    gender = models.CharField(max_length=25, choices=gender_)
    proof_number = models.CharField(max_length=256, null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="user-profiles")
    address = models.TextField()


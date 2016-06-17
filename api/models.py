from django.db import models
from django.contrib.auth.models import User


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
    proof = (
        ("Male", "Male"),
        ("Female", "Female")
    )
    gender = models.CharField(max_length=25, choices=proof)
    proof_number = models.CharField(max_length=256, null=True, blank=True)
    image = models.CharField(max_length=256, null=True, blank=True)
    address = models.TextField()


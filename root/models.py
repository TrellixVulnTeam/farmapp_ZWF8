from django.db import models

# Create your models here.

def upload_to(instance):
    return 'Images/{}/{}'.format(instance.__class__.__name__, instance.id)

class State(models.Model):
    unique_id = models.CharField(
        max_length=256, null=True)
    name = models.CharField(
        max_length=256, null=True)

class District(models.Model):
    unique_id = models.CharField(
        max_length=256, null=True)
    name = models.CharField(
        max_length=256, null=True)
    state = models.ForeignKey(State)

class Taluk(models.Model):
    unique_id = models.CharField(
        max_length=256, null=True)
    name = models.CharField(
        max_length=256, null=True)
    state = models.ForeignKey(State)
    district = models.ForeignKey(District)

class Village(models.Model):
    unique_id = models.CharField(
        max_length=256, null=True)
    name = models.CharField(
        max_length=256, null=True)
    taluk = models.ForeignKey(Taluk)
    state = models.ForeignKey(State)
    district = models.ForeignKey(District)
    pincode = models.CharField(
        max_length=256, null=True)

class Officer_Details(models.Model):
    name = models.CharField(
        max_length=256, null=True)
    full_name = models.CharField(
        max_length=256, null=True)
    email = models.EmailField(max_length=256)
    qualification_details = models.TextField()
    village = models.ForeignKey(Village)
    date_joining = models.DateField()
    assignee = models.ForeignKey("self")
    mobile = models.BigIntegerField(default=0)
    address = models.TextField()
    taluk = models.ForeignKey(Taluk)
    state = models.ForeignKey(State)
    district = models.ForeignKey(District)
    proof = (
        ("Adhaar", "Adhaar"),
        ("VoterId", "VoterId"),
        ("RationId", "RationId"),
        ("PanId", "PanId"),
        ("Other", "Other")
    )
    idproof_type = models.CharField(max_length=25, choices=proof)
    proof_number = models.CharField(max_length=256, null=True, blank=True)
    image = models.ImageField(upload_to=upload_to)

class Farmer_Details(models.Model):
    name = models.CharField(
        max_length=256, null=True)
    full_name = models.CharField(
        max_length=256, null=True)
    village = models.ForeignKey(Village)
    date_joining = models.DateField()
    mobile = models.BigIntegerField(default=0)
    address = models.TextField()
    taluk = models.ForeignKey(Taluk)
    state = models.ForeignKey(State)
    district = models.ForeignKey(District)
    detailed_history = models.TextField()
    account_details = models.TextField(null=True, blank=True)
    account_number = models.BigIntegerField(null=True, blank=True)
    proof = (
        ("Adhaar", "Adhaar"),
        ("VoterId", "VoterId"),
        ("RationId", "RationId"),
        ("PanId", "PanId"),
        ("Other", "Other")
    )
    idproof_type = models.CharField(max_length=25, choices=proof)
    proof_number = models.CharField(max_length=256, null=True, blank=True)
    image = models.ImageField(upload_to=upload_to)

class Crop(models.Model):
    crop_name = models.CharField(
        max_length=256, null=True)
    specialty = models.CharField(
        max_length=256, null=True)
    description = models.TextField()

class Crop_Type(models.Model):
    type_name = models.CharField(
        max_length=256, null=True)
    crop = models.ForeignKey(Crop)
    specialty = models.CharField(
        max_length=256, null=True)
    region_grown = models.CharField(
        max_length=256, null=True)
    description = models.TextField()
    time_for_yield = models.IntegerField()

class Service_Provider(models.Model):
    company_name = models.CharField(
        max_length=256, null=True)
    Sector = models.ForeignKey(Crop)
    specialization = models.CharField(
        max_length=256, null=True)
    contact = models.CharField(
        max_length=256, null=True)
    address = models.TextField()
    since = models.DateField()

class Farm_Land_Details(models.Model):
    image = models.ImageField(upload_to=upload_to)
    total_area = models.FloatField()
    village = models.ForeignKey(Village)
    farmer = models.ForeignKey(Farmer_Details)
    date_joining = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    address = models.TextField()
    taluk = models.ForeignKey(Taluk)
    state = models.ForeignKey(State)
    district = models.ForeignKey(District)
    crop = models.ForeignKey(Crop)
    crop_type = models.ForeignKey(Crop_Type)

class Farming_Type(models.Model):
    Types = (
        ("Organic", "Organic"),
        ("In Organinc", "In_Organic"),
        ("No Pestisided & No Fertilizer", "No_Pestisides_&_No_Fertilizer")
    )
    types = models.CharField(max_length=50, choices=Types)

class Transaction_Type(models.Model):
    Types = (
        ("Philanthropic", "Philanthropic"),
        ("investment for crop", "investment_for_crop"),
        ("investment on intrest", "investment on intrest")
    )
    types = models.CharField(max_length=50, choices=Types)

class Farming(models.Model):
    land = models.ForeignKey(Farm_Land_Details)
    farmer = models.ForeignKey(Farmer_Details)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    expected_end_date = models.DateField()
    no_of_units = models.IntegerField(default=0)
    officer = models.ForeignKey(Officer_Details)
    no_of_units_for_fund = models.IntegerField()
    farming_type = models.ForeignKey(Farming_Type)
    crop_type = models.ForeignKey(Crop_Type)
    no_of_units_funded = models.IntegerField()
    estimated_yield = models.FloatField()


class Crop_Life_Cycle(models.Model):
    video = models.FileField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_to)
    description = models.TextField(null=True, blank=True)
    farm = models.ForeignKey(Farming)
    day = models.DateField()
    day_count = models.IntegerField()
    service = models.ForeignKey(Service_Provider, null=True, blank=True)
    cost_service = models.FloatField()
    cost_for_day = models.FloatField()


class Yield(models.Model):
    video = models.FileField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_to)
    description = models.TextField()
    farm = models.ForeignKey(Farming)
    day = models.DateField()
    day_count = models.IntegerField()
    service = models.ForeignKey(Service_Provider)
    estimated_cost = models.FloatField()
    cost_end_of_farm = models.FloatField(null=True, blank=True)
    estimated_yield = models.FloatField()
    final_yield = models.FloatField(null=True, blank=True)
    spend_per_unit = models.FloatField(null=True, blank=True)
    our_price_quote_per_unit = models.FloatField()
    market_price_per_unit = models.FloatField()
    no_of_units_sold_fruit = models.IntegerField(null=True, blank=True)
    no_of_units_to_seed = models.IntegerField(null=True, blank=True)

class Delivery(models.Model):
    key = models.CharField(max_length=256, null=True, blank=True)
    status = models.CharField(max_length=256, null=True, blank=True)
    from_address = models.TextField()
    to_address = models.TextField()
    service_provider = models.ForeignKey(Service_Provider)


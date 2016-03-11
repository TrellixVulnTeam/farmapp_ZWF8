from django.contrib import admin
from .models import *

# Register your models here.

class DistrictAdmin(admin.ModelAdmin):
    fields = ['name' , 'state' , 'state_name', 'unique_id' ]
    list_display = ['unique_id', 'state', 'state_name', 'name']

    # def get_name(self, obj):
    #     return obj.state.name
    # get_name.admin_order_field  = 'get_name'  #Allows column order sorting
    # get_name.short_description = 'State Name'  #Renames column head
    #fields = ('unique_id', 'name', 'state_name')

admin.site.register(State)
admin.site.register(District, DistrictAdmin)
admin.site.register(Taluk)
admin.site.register(Village)
#admin.site.register(Author)

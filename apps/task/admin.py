from django.contrib import admin

# Register your models here.
from apps.task.models import Customer, BranchData, CustomerHomeAddressData

admin.site.register(Customer)
admin.site.register(BranchData)
admin.site.register(CustomerHomeAddressData)

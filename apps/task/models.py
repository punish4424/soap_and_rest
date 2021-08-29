from django.db import models


class Customer(models.Model):
    # Fields
    name = models.CharField(max_length=100)
    fathers_name = models.CharField(max_length=100)
    customer_profile = models.CharField(max_length=100)
    loan_account_number = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Customer'
        verbose_name_plural = 'Customers'


class BranchData(models.Model):
    # Relationships
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='branch_data')

    # Fields
    zone_name = models.CharField(max_length=100)
    region_name = models.CharField(max_length=100)
    area_name = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)
    branch_code = models.CharField(max_length=100)

    def __str__(self):
        return self.branch_name

    class Meta:
        verbose_name = 'Branch data'
        verbose_name_plural = 'Branch data'


class CustomerHomeAddressData(models.Model):
    # Relationships
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='address')

    # Fields
    pincode = models.CharField(max_length=100)
    landmark = models.CharField(max_length=100)
    address1 = models.CharField(max_length=100)
    address2 = models.CharField(max_length=100, null=True, blank=True)
    address3 = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.customer.name

    class Meta:
        verbose_name = 'Customer home address'
        verbose_name_plural = 'Customer home address'

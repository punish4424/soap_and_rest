from rest_framework import serializers

from apps.task.models import Customer, BranchData, CustomerHomeAddressData


class BranchDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchData
        fields = ("zone_name", "region_name", "area_name", "branch_name", "branch_code")


class CustomerHomeAddressDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerHomeAddressData
        fields = ("pincode", "landmark", "address1", "address2", "address3")


class CustomerSerializer(serializers.ModelSerializer):
    branch_data = BranchDataSerializer(many=True)
    address = CustomerHomeAddressDataSerializer(many=True)

    class Meta:
        model = Customer
        fields = [
            "name",
            "fathers_name",
            "customer_profile",
            "loan_account_number",
            "branch_data",
            "address",
        ]

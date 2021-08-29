import csv
import io

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_xml.parsers import XMLParser

from apps.task.models import Customer, BranchData, CustomerHomeAddressData
from apps.task.serializer import CustomerSerializer


class XMLtoJSONAPIView(APIView):
    parser_classes = (XMLParser,)

    def post(self, request, format=None, *args, **kwargs):
        response = {}
        response["from_date"] = request.data.get("fromDate")
        response["to_date"] = request.data.get("toDate")
        response["type"] = request.data.get("transType")
        response["agent"] = {}
        response["agent"]["id"] = request.data.get("agents").get("agentId")
        return Response(response)


class RestAPIView(APIView):
    serializer_class = CustomerSerializer

    def get(self, request, *args, **kwargs):
        customers = Customer.objects.all()
        serializer_data = self.serializer_class(customers, many=True)
        return Response(serializer_data.data)

    def post(self, request, *args, **kwargs):
        input_file = request.FILES["input_file"]
        decoded_file = input_file.read().decode("utf-8")
        io_string = io.StringIO(decoded_file)

        for counter, data in enumerate(
            csv.reader(io_string, delimiter=";", quotechar="|")
        ):
            if counter == 0:
                continue
            try:
                data = data[0].split(",")
                customer = get_object_or_404(Customer, loan_account_number=data[3])
            except:
                customer = Customer.objects.create(
                    name=data[0],
                    fathers_name=data[1],
                    customer_profile=data[2],
                    loan_account_number=data[3],
                )
            finally:
                BranchData.objects.create(
                    customer=customer,
                    zone_name=data[4],
                    region_name=data[5],
                    area_name=data[6],
                    branch_name=data[7],
                    branch_code=data[8],
                )
                CustomerHomeAddressData.objects.create(
                    customer=customer,
                    pincode=data[9],
                    landmark=data[10],
                    address1=data[11],
                    address2=data[12],
                    address3=data[13],
                )

        customers = Customer.objects.all()
        serializer_data = self.serializer_class(customers, many=True)
        return Response(serializer_data.data)

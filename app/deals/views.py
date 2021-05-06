from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Deals
from .serializers import DealsSerializer

from rest_framework import status
from django.db.models import Sum
from .serializers import TestSer

class DealsView(APIView):
  def get(self, request):
#    deals = Deals.objects.all()
#    serializer = DealsSerializer(deals, many=True)

    customers = Deals.objects.values('customer').annotate(Sum('total'))
    customersTop = customers.order_by('-total__sum')[0:5]
    serializer = TestSer(customersTop, many=True)
    #serializer =  TestSer(test)
    return Response({"deals": serializer.data})
    #return Response({"response":customersTop})


from rest_framework.parsers import FormParser, MultiPartParser
from .serializers import FileSerializer
import io, csv


class FileView(APIView):
  parser_classes = (MultiPartParser, FormParser)

  def post(self, request, *args, **kwargs):
    file_serializer = FileSerializer(data=request.data)
    if file_serializer.is_valid():
      Deals.objects.all().delete()
      file = file_serializer.validated_data['deals']
      decoded_file = file.read().decode()
      io_string = io.StringIO(decoded_file)
      reader = csv.reader(io_string)
      for row in reader:
        if row[2]=='total': continue
        deal = Deals(
          customer=row[0],
          item=row[1],
          total=row[2],
          quantity=row[3],
          date=row[4]
        )
        deal.save()
      return Response({"Status":"OK"}, status=status.HTTP_200_OK)
    else:
      return Response({"Status":"Error"}, file.serializer.errors, status=status.HTTP_400_BAD_REQUEST)

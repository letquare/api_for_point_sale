
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework import generics

from .serializers import PointOfSaleSerializer, VisitSerializer
from .models import Employee, PointOfSale


class ViewSale(generics.ListAPIView):
    """
    Method needed for get data about point of sale on phone employee
    """
    serializer_class = PointOfSaleSerializer

    def get_queryset(self):

        employee = get_object_or_404(Employee, phone=self.kwargs['phone'])
        queryset = PointOfSale.objects.filter(employee=employee)
        return queryset


class VisitPointSale(generics.CreateAPIView):
    """
    Method needed for add data about visit on point of sale
    """
    serializer_class = VisitSerializer

    def create(self, request, *args, **kwargs):
        visitor = get_object_or_404(Employee, phone=self.kwargs['phone'])
        data = request.data
        context = {
            'pk': self.kwargs['pk'],
            'visitor': visitor
        }
        serializer = VisitSerializer(data=data, context=context)
        if serializer.is_valid():
            serializer.save()
            data = {
                'id': serializer.data['id'],
                'time': serializer.data['datatime']
            }
            return JsonResponse(data, status=201)
        return JsonResponse(serializer.errors, status=400)

from django.urls import path
from .views import ViewSale, VisitPointSale

# /api/v1/
urlpatterns = [
    path('ShowPointSales/<int:phone>/', ViewSale.as_view()),
    path('GoPointSale/<int:phone>/<int:pk>/', VisitPointSale.as_view()),
]

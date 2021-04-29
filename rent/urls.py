from django.urls import path

from rent.views import RentHistory, AddRent

urlpatterns = [
    path('', RentHistory.as_view(), name='rent'),
    path('create/', AddRent.as_view(), name='add_rent'),
]
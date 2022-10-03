from django.urls import path
from .views import BrandsView

urlpatterns = [
    path('crud_brands/', BrandsView.as_view()),
    path('crud_brands/<int:id>', BrandsView.as_view())
]

from django.urls import path
from django.conf.urls import include
#from .views import sceneApi
from . import views
from rest_framework.decorators import permission_classes, authentication_classes
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter

router = DefaultRouter(trailing_slash=False)

urlpatterns = [
    path('secondschema/test', authentication_classes([])(permission_classes([AllowAny])(views.GetSecondSchema)).as_view({'get':'getTest'}), name='getsecondschemafortest'),
    path('secondschema/screenplay', authentication_classes([])(permission_classes([AllowAny])(views.GetSecondSchema)).as_view({'get':'getScreenplay'}), name='getScreenplay'),
    ]




# api/urls.py
from django.urls import path
from .views import ItemList, CategoryItemList

urlpatterns = [
    path('items/', ItemList.as_view(), name='item-list'),
    path('items/<str:category>/', CategoryItemList.as_view(), name='category-item-list'),
]

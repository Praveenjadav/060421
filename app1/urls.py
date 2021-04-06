from django.urls import path
from app1 import views
app_name="app1"

urlpatterns = [
    path('',views.index,name="a1"),
    path('page1/',views.page1,name="page1"),
    path('sample1/',views.sample_app1,name="sample1"),
]

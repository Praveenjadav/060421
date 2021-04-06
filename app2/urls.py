from django.urls import path
from app2 import views
app_name="app2"

urlpatterns = [
    path('',views.index,name="a1"),
    path('page1/',views.page1,name="page1"),
    path('sample2/',views.sample_app2,name="sample2"),
]

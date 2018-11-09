from django.urls import path
from . import views

urlpatterns = [
    path('<int:thesis_pk>', views.thesis_detail, name='thesis_detail' ),
]
from django.urls import path
from . import views


urlpatterns=[
    path('hello/',views.sayhello),
    path('see2',views.see),
    path('detail/<int:id>/',views.detail, name='detail'),
]
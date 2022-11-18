from . import views
from django.urls import path

urlpatterns = [

      path('',views.demo,name="demo"),
      # path('arithmetic/',views.operations,name="operations"),

    ]

# path('subtract/', views.subtraction, name="subtraction"),
from django.urls import path
from categories.views import AllCategories
from categories.views import CreateCategory
from . import views

from django.contrib.auth.decorators import login_required




urlpatterns = [
 
 path('',AllCategories.as_view(),name='categories.index'),
 path('create',login_required(CreateCategory.as_view()),name='categories.create'),
 path('showcat/<int:id>',views.showcat,name='categories.show'),
    
]






from django.urls import path
from . import views
urlpatterns = [
    path('base',views.base,name='base'),
    path('delete/<int:id>',views.deletepro,name='delete'),
    path('show/<int:id>',views.show,name='show'),
    path('posts',views.posts,name='posts'),
    path('items',views.home,name='items'),
    path('edit/<int:id>',views.editpost,name='edit'),
    
]






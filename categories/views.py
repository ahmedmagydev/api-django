from django.shortcuts import render , redirect

# Create your views here.
from django.views import View
from categories.models import Category
from categories.forms import CategoryModelForm
from django.contrib.auth.decorators import login_required

# @login_required   
class AllCategories(View):
    
    
    def get(self, request):
        categories=Category.objects.all()
        return render(request,'categories/index.html',context={'categories':categories})
    
    
# @login_required   
class CreateCategory(View):
    def get(self, request):
        categoryform = CategoryModelForm()
        
        return render(request,'categories/create.html',context={'form':categoryform})
    
    
    
    
    def post(self, request):
        categoryform = CategoryModelForm(request.POST,request.FILES)
        if categoryform.is_valid():
            categoryform.save()  
            return redirect('categories.index')
        return redirect('categories.create')
    
# @login_required   
def showcat(request,id):
    showcat=Category.objects.get(pk=id)
    return render(request,'categories/showcat.html',{"cat":showcat})
     
    
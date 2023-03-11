from django.shortcuts import render, get_object_or_404, redirect
from .forms import AddPro
from posts.models import NewProducts
from categories.models import Category
from django.contrib.auth.decorators import login_required
# Create your views here.



def base(request):
    return render(request,'base.html')

def posts(request):
    if request.method=='GET':
        # cats=Category.get_all_categories()

        dataform=AddPro()
        return render(request, 'posts.html', context={'lf': dataform})
            
        # return render(request,'posts.html',{'lf':AddPro})
    elif request.method=='POST':
        dataform  = AddPro(request.POST, request.FILES)
        if dataform.is_valid():
            dataform.save()
            return render(request,'posts.html',{'lf': dataform})



def home(request):
    products=NewProducts.objects.all()
    return render(request,'items.html',{"pros":products})


@login_required
def deletepro(request, id):
    products = get_object_or_404(NewProducts, pk=id)
    products.delete()
    return redirect('items')
    # return render(request,'items.html' ,{"pros":products})



def show(request,id):
    showpro=NewProducts.objects.get(pk=id)
    return render(request,'show.html',{"product":showpro})

@login_required
def editpost(request ,id):
    mypost =NewProducts.objects.get(id=id)
    if request.method=='GET':
        dataform=AddPro(instance=mypost)
        return render(request, 'edit.html', context={'lf': dataform})
            
        # return render(request,'posts.html',{'lf':AddPro})
    elif request.method=='POST':
        dataform  = AddPro(request.POST, request.FILES ,instance=mypost)
        if dataform.is_valid():
            dataform.save()
            return render(request,'edit.html',{'lf':AddPro})



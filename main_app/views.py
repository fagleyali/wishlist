from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.edit import CreateView,DeleteView
from .models import Wish


class WishList(ListView):
    model = Wish
    

class WishCreate(CreateView):
    model = Wish
    fields= '__all__'

    success_url='/'

def wish_delete(request, wish_id):
    Wish.objects.get(id=wish_id).delete()
    return redirect('/')
    




# Create your views here.

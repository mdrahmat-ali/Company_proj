from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from testapp.models import Company
from django.urls import reverse_lazy

class CompanyListView(ListView):
    model=Company

class CompanyDetailView(DetailView):
    model=Company

class CompanyCreateView(CreateView):
    model=Company
    fields=('name','location','ceo')  #or we can use __all__()

class CompanyUpdateView(UpdateView):
    model=Company
    fields=('name','ceo')

class CompanyDeleteView(DeleteView):
    model=Company
    success_url=reverse_lazy('companies')
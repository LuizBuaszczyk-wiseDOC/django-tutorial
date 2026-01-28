from typing import Any
from django.db.models.query import QuerySet
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class OwnerListView(ListView):
    pass
    
class OwnerDetailView(DetailView):
    pass
    
class OwnerCreateView(LoginRequiredMixin, CreateView):   
    def form_valid(self, form):
        object = form.save(commit=False)  
        object.owner = self.request.user
        object.save()
        return super(OwnerCreateView, self).form_valid(form)
            
class OwnerUpdateView(LoginRequiredMixin, UpdateView):
    def get_queryset(self):
        """Adicionando novo filtro AND para verificar se o usuário é o owner"""
        qs = super(OwnerUpdateView, self).get_queryset()
        return qs.filter(owner=self.request.user)
    
class OwnerDeleteView(LoginRequiredMixin, DeleteView):
    def get_queryset(self):
        """Adicionando novo filtro AND para verificar se o usuário é o owner"""
        qs = super(OwnerDeleteView, self).get_queryset()
        return qs.filter(owner=self.request.user)
    
    
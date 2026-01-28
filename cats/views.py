from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from cats.models import Cat, Breed
from cats.forms import BreedForm

# Create your views here.

## Cat
class CatList(LoginRequiredMixin, View):
    def get(self, request):
        cats = Cat.objects.all()
        breed_count = Breed.objects.count()
        
        context = {'breed_count': breed_count, 'cat_list': cats}
        return render(request, 'cats/cat_list.html', context)
    
class CatCreate(LoginRequiredMixin, CreateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')
    
class CatUpdate(LoginRequiredMixin, UpdateView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')
        
class CatDelete(LoginRequiredMixin, DeleteView):
    model = Cat
    fields = '__all__'
    success_url = reverse_lazy('cats:all')
    
## Breed

class BreedView(LoginRequiredMixin, View):
    def get(self, request):
        breeds = Breed.objects.all()
        context = {'breed_list': breeds}
        return render(request, 'cats/breed_list.html', context)
    
class BreedCreate(LoginRequiredMixin, View):
    template = 'cats/breed_form.html'
    success_url = reverse_lazy('cats:all')
    
    def get(self, request):
        form = BreedForm()
        ctx = {'form': form}
        return render(request, self.template, ctx)
    
    def post(self, request):
        form = BreedForm(request.POST)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        breed = form.save()
        return redirect(self.success_url)
        
class BreedUpdate(LoginRequiredMixin, View):
    model = Breed
    template = 'cats/breed_form.html'
    success_url = reverse_lazy('cats:all')
    
    def get(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        form = BreedForm(instance=breed)
        ctx = {'form': form}
        return render(request, self.template, ctx)
    
    def post(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        form = BreedForm(request.POST, instance=breed)
        if not form.is_valid():
            ctx = {'form': form}
            return render(request, self.template, ctx)

        form.save()
        return redirect(self.success_url)
        
class BreedDelete(LoginRequiredMixin, View):
    model = Breed
    template = 'cats/breed_confirm_delete.html'
    success_url = reverse_lazy('cats:all')
    
    def get(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        ctx = {'breed': breed}
        return render(request, self.template, ctx)
    
    def post(self, request, pk):
        breed = get_object_or_404(self.model, pk=pk)
        breed.delete()
        return redirect(self.success_url)      
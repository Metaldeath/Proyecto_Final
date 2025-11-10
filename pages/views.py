from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from .models import Page
from .forms import PageForm

class PageListView(ListView):
    model = Page
    template_name = 'pages/list.html'
    context_object_name = 'pages'
    paginate_by = 10

    def get_queryset(self):
        q = self.request.GET.get('q', '')
        qs = Page.objects.order_by('-fecha')
        if q:
            qs = qs.filter(titulo__icontains=q)
        return qs

class PageDetailView(DetailView):
    model = Page
    template_name = 'pages/detail.html'
    context_object_name = 'page'

class OwnerRequiredMixin(UserPassesTestMixin):
    def test_func(self):
        obj = self.get_object()
        return obj.autor == self.request.user

class PageCreateView(LoginRequiredMixin, CreateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/form.html'
    success_url = reverse_lazy('pages:list')

    def form_valid(self, form):
        form.instance.autor = self.request.user
        messages.success(self.request, "Página creada correctamente.")
        return super().form_valid(form)

class PageUpdateView(LoginRequiredMixin, OwnerRequiredMixin, UpdateView):
    model = Page
    form_class = PageForm
    template_name = 'pages/form.html'
    success_url = reverse_lazy('pages:list')

    def form_valid(self, form):
        messages.success(self.request, "Página actualizada.")
        return super().form_valid(form)

class PageDeleteView(LoginRequiredMixin, OwnerRequiredMixin, DeleteView):
    model = Page
    template_name = 'pages/confirm_delete.html'
    success_url = reverse_lazy('pages:list')

    def delete(self, request, *args, **kwargs):
        messages.success(request, "Página eliminada.")
        return super().delete(request, *args, **kwargs)

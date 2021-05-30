from django.shortcuts import render, get_object_or_404,redirect
from .models import *


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, pk):
        obj = get_object_or_404(self.model, pk=pk)
        return render(request, self.template, context={self.model.__name__.lower(): obj})


class ObjectCreateMixin:
    model_form = None
    template = None

    def get(self, request):
        form = self.model_form()
        return render(request, self.template, context={'form': form})

    def post(self, request):
        bound_form = self.model_form(request.POST)
        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form})


class ObjectUpdateMixin:
    model = None
    model_form = None
    template = None

    def get(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        bound_form = self.model_form(instance=obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})

    def post(self, request, pk):
        obj = self.model.objects.get(pk=pk)
        bound_form = self.model_form(request.POST, instance=obj)

        if bound_form.is_valid():
            new_obj = bound_form.save()
            return redirect(new_obj)
        return render(request, self.template, context={'form': bound_form, self.model.__name__.lower(): obj})


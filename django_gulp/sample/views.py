from django.shortcuts import render
from django.views.generic import TemplateView

from . import models


class SampleView(TemplateView):

    def get(self, request, *args, **kwargs):

        context = { 'tasks': models.Task.objects.all()}
        return render(self.request, "sample/detail.html" , context)

sample = SampleView.as_view()

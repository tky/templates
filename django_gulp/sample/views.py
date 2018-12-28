from django.shortcuts import render
from django.views.generic import TemplateView


class SampleView(TemplateView):

    def get(self, request, *args, **kwargs):

        context = {}
        return render(self.request, "sample/detail.html" , context)

sample = SampleView.as_view()

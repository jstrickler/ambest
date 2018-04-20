#!/usr/bin/env python
# (c) 2017 CJ Associates
#
from django.views.generic import TemplateView, ListView, DetailView
from .models import Band

class BandListView(ListView):
    context_object_name = 'bands'
    template_name = 'bands_class_list.html'
    model = Band


class BandDetailView(DetailView):
    context_object_name = 'band'
    template_name = 'band_class_details.html'
    model = Band

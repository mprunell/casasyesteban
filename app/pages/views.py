# -*- encoding: utf-8 -*-
from django.views.generic import TemplateView, DetailView
from django.template.loader import select_template
from django.template.base import TemplateDoesNotExist
from pages.models import Home, About, Work, Consultancy, Workshops, Workshop, Contact


class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update({
            'object': Home.objects.get(),
            'active': {'home': 'active'}
        })

        return context


class AboutView(TemplateView):
    template_name = 'pages/about.html'

    def get_context_data(self, **kwargs):
        context = super(AboutView, self).get_context_data(**kwargs)
        context.update({
            'active': {'about': 'active'},
            'object': About.objects.get(),
        })

        return context


class WorkView (TemplateView):
    template_name = 'pages/work.html'

    def get_context_data(self, **kwargs):
        context = super(WorkView, self).get_context_data(**kwargs)
        context.update({
            'active': {'work': 'active'},
            'object': Work.objects.get(),
        })

        return context


class ConsultancyView (TemplateView):
    template_name = 'pages/consultancy.html'

    def get_context_data(self, **kwargs):
        context = super(ConsultancyView, self).get_context_data(**kwargs)
        context.update({
            'object': Consultancy.objects.get(),
            'active': {'consultancy': 'active'}
        })

        return context


class WorkshopsView (TemplateView):
    template_name = 'pages/workshops.html'

    def get_context_data(self, **kwargs):
        context = super(WorkshopsView, self).get_context_data(**kwargs)
        context.update({
            'active': {'workshops': 'active'},
            'object': Workshops.objects.get(),
        })

        return context


class WorkshopView (TemplateView):
    template_name = 'pages/workshop.html'

    def get_context_data(self, **kwargs):
        context = super(WorkshopView, self).get_context_data(**kwargs)
        context.update({
            'object': Workshop.objects.get(slug=kwargs['wsid']),
            'active': {'workshops': 'active'}
        })

        return context


class ContactView(TemplateView):
    template_name = 'pages/contact.html'

    def get_context_data(self, **kwargs):
        context = super(ContactView, self).get_context_data(**kwargs)

        context.update({
            'active': {'contact': 'active'},
            'object': Contact.objects.get()
        })

        return context
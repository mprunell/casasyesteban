# -*- encoding: utf-8 -*-
from django.views.generic import TemplateView, DetailView
from django.template.loader import select_template
from django.template.base import TemplateDoesNotExist
from pages.models import Home, About, Work, Consultancy, Workshops, Workshop, Contact

EFFECTIVE_COMMUNICATION = {
    'name': u'Comunicacion Efectiva',
    'description': u'El objetivo de este taller apunta a que los participantes '
                   u'amplíen sus conocimientos acerca del poder que tiene la palabra, '
                   u'aprendiendo a reconocer las diferentes interferencias que dificultan '
                   u'o incluso impiden el desarrollo de una comunicación efectiva. '
                   u'Se entrenará en la identificación de las principales señales emitidas '
                   u'por los individuos tanto a nivel verbal como físico, los diferentes estilos '
                   u'en la forma de comunicar y se capacitará de manera de optimizar lo que '
                   u'realmente importa: comunicar efectivamente.'
}

ANGER_MANAGEMENT = {
    'name': u'Autoregulacion del Enojo',
    'description': u'El enojo es una emoción natural en el ser humano, no obstante, la expresión inadecuada del mismo, podrá tornarse en un obstáculo importante dentro la organización. Puede generar dificultades en el clima, pérdida de colaboradores claves, así como afectar la toma de decisiones y el vínculo con los clientes entre otras consecuencias. En este taller se pretende que los participantes aprendan a transformar efectivamente el enojo que destruye en enojo que resuelve, para ello se entrenará en habilidades que permitan expresar las ideas de un modo adecuado, manteniendo la firmeza sin apelar a agresiones que inhiben y/o anulan la expresión de puntos de vista diferentes. ',
}

STRESS_MANAGEMENT = {
    'name': u'Manejo del Estres',
    'description': u'El estrés es un conjunto de reacciones físicas y psicológicas que surgen ante cualquier demanda que supera nuestra capacidad adaptativa. Desarrollamos un programa en el que los participantes aprenden a identificar, controlar, y desarrollar nuevas estrategias en el manejo del estrés tanto a nivel laboral como personal. ',
}

MOTIVATION = {
    'name': u'Motivacion',
    'description': u'Es una sensación de logro que los individuos pueden generar a partir de los pensamientos y anticipaciones positivas generadas frente aquello que desean obtener. El objetivo general es que los integrantes tomen conciencia del proceso de motivación aprendiendo a identificar las prioridades y necesidades de sus colaboradores. Los objetivos específicos se diseñarán a partir de los requerimientos solicitados por la empresa.',
}

HOW_TO_BE_AN_EFFECTIVE_LEADER = {
    'name': u'Como ser un lider eficiente',
    'description': u'Conducir un grupo humano es una tarea compleja, que requiere de competencias específicas para obtener los resultados esperados tanto del desempeño individual como en equipo. Jefes ineficientes o áreas conducidas en forma inadecuada generan obstáculos sustanciales para el desarrollo empresarial. Este taller pretende que los integrantes desarrollen habilidades que permitan potenciar el establecimiento de metas y prioridades para logar una eficiente conjunción de recursos en pos de alcanzar los objetivos de la organización.',
}

COACHING = {
    'name': u'Coaching Personal y/o Grupal',
    'description': u'Proceso en el que se busca el camino más eficaz para alcanzar los objetivos fijados, utilizando las propias habilidades de las personas y/o equipos. Se enseña a identificar y manejar los obstáculos y se gestiona el entrenamiento de nuevas habilidades si el objetivo trazado lo requiere.',
}

WORKSHOPS = {
    'effective-communication': EFFECTIVE_COMMUNICATION,
    'anger-management': ANGER_MANAGEMENT,
    'stress-management': STRESS_MANAGEMENT,
    'motivation': MOTIVATION,
    'how-to-be-an-efficient-leader': HOW_TO_BE_AN_EFFECTIVE_LEADER,
    'coaching': COACHING,
}


class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context.update({
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
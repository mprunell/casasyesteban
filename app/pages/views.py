from django.views.generic import TemplateView
from pages.models import Home


class HomeView(TemplateView):
    template_name = 'pages/home.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        home = Home.objects.all()
        if home:
            home = home[0]
        else:
            home = None
        print home
        print home.carousel.image_set.all()[0]
        context.update({
            'home': home,
        })

        return context

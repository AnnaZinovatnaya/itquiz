from django.utils import timezone
from django.views.generic.list import ListView

from itquiz.apps.quizes.models import Category, Quiz


class IndexView(ListView):
    model = Quiz
    template_name = 'index.html'
    context_object_name = 'quizes_list'
    queryset = Quiz.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories_list'] = Category.objects.all()
        return context

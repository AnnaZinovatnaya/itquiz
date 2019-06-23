from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from itquiz.apps.quizes.models import Category, Quiz, Question


class IndexView(ListView):
    model = Quiz
    template_name = 'index.html'
    context_object_name = 'quizes_list'
    queryset = Quiz.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories_list'] = Category.objects.all()
        return context


class CategoryView(DetailView):
    model = Category
    template_name = 'category.html'
    context_object_name = 'category'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['quizes_list'] = Quiz.objects.filter(category__slug=self.kwargs['slug'])
        return context


class QuizView(DetailView):
    model = Quiz
    template_name = 'quiz.html'
    context_object_name = 'quiz'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['questions_list'] = Question.objects.filter(quiz__slug=self.kwargs['slug'])
        return context

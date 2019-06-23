from django.contrib import admin
from itquiz.apps.quizes.models import Quiz, Question, Answer, Category
from django.forms.models import BaseInlineFormSet
from django.core.exceptions import ValidationError


class AnswerInlineFormSet(BaseInlineFormSet):
    def clean(self):
        super(AnswerInlineFormSet, self).clean()
        total_checked = 0

        for form in self.forms:
            if not form.is_valid():
                return
            if form.cleaned_data and not form.cleaned_data.get('DELETE'):
                if form.cleaned_data['is_correct']:
                    total_checked += 1

        if total_checked < 1:
            raise ValidationError("You must have at least one correct answer")


class AnswerInline(admin.TabularInline):
    formset = AnswerInlineFormSet
    model = Answer
    extra = 1


class QuestionAdmin(admin.ModelAdmin):
    fields = ['quiz', 'text']
    inlines = [AnswerInline]
    list_display = ('text', 'quiz')
    list_filter = ['quiz']


class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1


class QuizAdmin(admin.ModelAdmin):
    list_display = ["title", "is_valid"]

    def is_valid(self, obj):
        return len(Question.objects.filter(quiz__pk=obj.id)) != 0

    is_valid.boolean = True


admin.site.register(Category)
admin.site.register(Quiz, QuizAdmin)
admin.site.register(Question, QuestionAdmin)
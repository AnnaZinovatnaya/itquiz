from django.db import models


class Category(models.Model):
    title = models.CharField(db_index=True, max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "categories"


class Quiz(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    title = models.CharField(db_index=True, max_length=255)
    category = models.ForeignKey('quizes.Category', on_delete=models.CASCADE, related_name='quizes')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "quizes"


class Question(models.Model):
    text = models.TextField()
    quiz = models.ForeignKey('quizes.Quiz', on_delete=models.CASCADE, related_name='questions')

    def is_multi_choice(self):
        return len(self.answers.filter(question__pk=self.pk)) > 1

    def __str__(self):
        return self.text


class Answer(models.Model):
    question = models.ForeignKey('quizes.Question', on_delete=models.CASCADE, related_name='answers')
    text = models.TextField()
    is_correct = models.BooleanField()

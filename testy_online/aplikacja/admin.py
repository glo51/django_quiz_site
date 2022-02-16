from django.contrib import admin
from .models import Test, Question, Answer


class QuestionAnswers(admin.TabularInline):
    model = Answer
    extra = 4


class TestQuestions(admin.TabularInline):
    model = Question
    extra = 10


class TestAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'difficulty', 'pub_date')
    readonly_fields = ['pub_date']
    search_fields = ['title']
    list_filter = ['category', 'difficulty', 'pub_date']
    inlines = [TestQuestions]


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'test')
    search_fields = ['question_text', 'test__title']
    inlines = [QuestionAnswers]


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('answer_text', 'question', 'is_correct')
    search_fields = ['answer_text', 'question__question_text']
    list_filter = ['is_correct']


admin.site.register(Test, TestAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)

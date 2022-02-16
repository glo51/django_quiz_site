from django.contrib import admin as a
from .models import Result


class ResultAdmin(a.ModelAdmin):
    list_display = ('__str__', 'user', 'score', 'max_score', 'percent', 'completion_date')
    readonly_fields = ['user', 'test', 'score', 'max_score', 'completion_date']
    list_filter = ['user']
    search_fields = ['user__username', 'test__title']


a.site.register(Result, ResultAdmin)

from django.contrib.auth.models import User
from django.db import models as m
from aplikacja.models import Test


class Result(m.Model):
    user = m.ForeignKey(User, on_delete=m.CASCADE)
    test = m.ForeignKey(Test, on_delete=m.CASCADE)
    score = m.PositiveIntegerField(default=0)
    max_score = m.PositiveIntegerField(default=0)
    completion_date = m.DateTimeField('completion', auto_now_add=True)

    @property
    def percent(self):
        return '{:.0%}'.format(self.score / self.max_score)

    def __str__(self):
        return f'{self.user} | {self.test} | {self.completion_date.strftime("%d.%m.%Y")}'

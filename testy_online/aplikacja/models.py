from django.db import models as m


class Test(m.Model):
    title = m.CharField(max_length=100)
    category = m.CharField(max_length=50)
    questions_number = m.PositiveSmallIntegerField(default=0)
    difficulty = m.PositiveSmallIntegerField(choices=[(1, 'easy'), (2, 'normal'), (3, 'hard')])
    pub_date = m.DateField('published', auto_now=True)

    def __str__(self):
        return self.title


class Question(m.Model):
    test = m.ForeignKey(Test, on_delete=m.CASCADE)
    question_text = m.CharField(max_length=200)

    def __str__(self):
        return self.question_text


class Answer(m.Model):
    question = m.ForeignKey(Question, on_delete=m.CASCADE)
    answer_text = m.CharField(max_length=150)
    is_correct = m.BooleanField(default=False)

    def __str__(self):
        return self.answer_text

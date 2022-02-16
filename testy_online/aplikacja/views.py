from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Test, Question


def tests(req):
    tests_list = Test.objects.order_by('pub_date')
    context = {'tests_list': tests_list}
    return render(req, 'aplikacja/tests.html', context)


@login_required
def q_and_a(req, test_id):
    test_title = get_object_or_404(Test, pk=test_id).title
    q_and_a_list = Question.objects.filter(test=test_id)
    if not q_and_a_list:
        return render(req, 'aplikacja/error.html')
    context = {'q_and_a_list': q_and_a_list, 'test_title': test_title, 'test_id': test_id}
    return render(req, 'aplikacja/q_and_a.html', context)

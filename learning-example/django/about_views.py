# django lib
from django.shortcuts import render

# the variables need to put in context before send to template
def index(request):
    question_list = [1,2,3,4]
    context = {'some_list':question_list}
    return render(request,'polls/index.html',context)

# 404 page
from django.http import Http404
from django.shortcuts import render
from .modal import Question

def detail(request,question_id):
    try:
        question = Question.object.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(request,'polls/detail.html',{'question':question})

# sometime we need to redirect the url
# and sometime we need to get the info in 'POST' 
from django.urls import reverse
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import get_object_or_404,render
# ...
def vote(request,question_id):
    # ...
    pk = request.POST['question_id']  # about how to get the 'POST'
    return HttpResponseRedirect(reverse('polls:results',args=(question_id,)))

from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.http import Http404
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from .models import Choice, Question
from .forms import QuestionForm, ChoicesForm
from django.utils import timezone


# Create your views here.
def index(abc):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	return render(abc, 'polls/index.html', {'latest_question_list':latest_question_list})


def detail(request, question_id):
	try:
		question = Question.objects.get(pk = question_id)
	except Question.DoesNotExist:
		raise Http404(" DoesNotExist")
	
	return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
	result_question = get_object_or_404(Question, pk=question_id)
	return render(request, 'polls/results.html', {'question': result_question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
    	selected_choice = question.choice_set.get(pk=int(request.POST['choice']))
    

    except(keyError, Choice.DoesNotExist):
    	return render(request, 'polls/detail.html', {
    		'question' : question,
    		'error_message' : "You didn't select a choice."
    		})
    else:
    	selected_choice.votes+=1
    	selected_choice.save()
    	#return HttpResponse(request, 'polls/results.html' , { 'question : question.id'})
    	return HttpResponseRedirect(reverse('results', args=(question.id,)))


def form(request):
	questionform = QuestionForm()


	if request.method == 'POST':
		responseform = QuestionForm(request.POST)
		if responseform.is_valid():
			newquestion = responseform.cleaned_data['question']
			newadd = Question.objects.create(question_text = newquestion, pub_date = timezone.now())
			return HttpResponseRedirect('/')
		else:
			return HttpResponseRedirect('/form')

	return render(request, 'polls/form.html', {'form' : questionform })

def addchoice(request):
	choiceform = ChoicesForm()
	if request.method == 'POST':
		responsechoice = ChoicesForm(request.POST)
		if responsechoice.is_valid():
			responsechoice.save()
		else:
			return HttpResponseRedirect('/addchoice')

	return render(request, 'polls/addchoice.html',{ 'choiceform' : choiceform})



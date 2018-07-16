from django import forms
from django.forms import ModelForm
from .models import Choice, Question

class QuestionForm(forms.Form):
	question = forms.CharField(max_length= 100)

class ChoicesForm(ModelForm):
	"""docstring for ChoicesForm"""
	class Meta:
		model = Choice
		fields = [ 'question', 'choice_text']
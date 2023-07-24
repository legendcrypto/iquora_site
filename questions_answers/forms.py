from django import forms
from .models import Answer

class AddQuestion(forms.Form):
    question = forms.CharField(label="Ask a Question", required = True, widget=forms.TextInput(attrs={'style': 'width: 80%; height: 100px'}))

class AddAnswer(forms.ModelForm):
    answer = forms.CharField(label="Answer this question", required = True, widget=forms.TextInput(attrs={'style': 'width: 80%; height: 80px'}))

    class Meta:
        model = Answer
        fields =  ('answer', )

from django.shortcuts import render, redirect
from .forms import AddQuestion, AddAnswer
from questions_answers.models import Question, Answer

# Create your views here.
def show_questions(request):
    if not request.user.is_authenticated:
        return redirect("/")
    questions = Question.objects.all()
    return render(request=request, template_name="home.html", context={"questions": questions})

def add_question(request):
    if not request.user.is_authenticated:
        return redirect("/")
    if request.method == "POST":
        form = AddQuestion(data=request.POST)
        if form.is_valid():
            Question.objects.create(question=form.cleaned_data.get('question'))
            return redirect("/questions")
    form = AddQuestion()
    return render(request=request, template_name="add-question.html", context={"form": form})

def show_question_answers(request, id):
    if not request.user.is_authenticated:
        return redirect("/")
    answers = Answer.objects.filter(question=id)
    question = Question.objects.get(id=id).question
    if request.method == "POST":
        form = AddAnswer(data=request.POST)
        if form.is_valid():
            Answer.objects.create(question_id=id, answer=form.cleaned_data.get('answer'))
        return redirect("/questions/question/{}".format(id))
    form = AddAnswer()
    return render(request=request, template_name="show-question-answers.html", context={"question": question, "answers": answers, "question_id": id, "form": form})

def like_answer(request, id):
    if not request.user.is_authenticated:
        return redirect("/")
    answer = Answer.objects.get(id=id)
    answer.like_count += 1
    answer.save()
    return redirect("/questions/question/{}".format(answer.question_id))

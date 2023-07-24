from django.urls import path
from questions_answers import views

urlpatterns = [
    path("", views.show_questions, name="show_questions"),
    path("add-question", views.add_question, name="add_question"),
    path("question/<int:id>/", views.show_question_answers, name="show_question_answers"),
    path("like-answer/<int:id>/", views.like_answer, name="like_answer"),
]

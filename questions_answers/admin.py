from django.contrib import admin
from questions_answers.models import *

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
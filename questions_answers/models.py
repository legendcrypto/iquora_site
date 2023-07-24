from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=1000, null=False, blank=False)

    def __str__(self):
        return self.question

class Answer(models.Model):
    answer = models.CharField(max_length=1500)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    like_count = models.IntegerField(default=0)

    def __str__(self):
        extra = ""
        if len(self.answer) > 100:
            extra = "      .........Read for more............"
        return self.answer[0: 100] + extra

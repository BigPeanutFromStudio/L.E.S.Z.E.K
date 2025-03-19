from django.db import models
from django.contrib.auth.models import User

class Code(models.Model):
    codeName = models.CharField(max_length=5000)
    def __str__(self):
        return self.codeName

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=10000)
    answer_a = models.CharField(max_length=5000)
    answer_b = models.CharField(max_length=5000)
    answer_c = models.CharField(max_length=5000)
    answer_d = models.CharField(max_length=5000)
    correct_answer = models.CharField(null=True,blank=True,max_length=5000)
    media = models.CharField(null=True,blank=True, max_length=5000) #FilePathField
    code_ID = models.ForeignKey(Code,on_delete=models.DO_NOTHING)
    class Meta:
        unique_together = ('question', 'media', 'code_ID')
    def __str__(self):
        mediaRef = None
        if self.media:
            mediaRef = "vid" if self.media.split('.')[1] == "mp4" else "img" 
        else:
            mediaRef = '0'
        return f'{self.code_ID}_{mediaRef}'


class QuestionApplication(models.Model):
    questionID = models.ForeignKey(Question,on_delete=models.DO_NOTHING)
    correct_answer = models.CharField(max_length=5000)
    user_ID = models.ForeignKey(User,on_delete=models.DO_NOTHING)
    sent_at = models.DateTimeField()
    def __str__(self):
        return f'{self.questionID.code_ID} - {self.questionID.question}'
    
    
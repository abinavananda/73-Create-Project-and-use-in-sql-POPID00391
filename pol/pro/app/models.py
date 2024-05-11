from django.db import models

# Create your models here.
class Question(models.Model):
    question = models.CharField(max_length=300)

    def __str__(self):
        return self.question

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    option = models.CharField(max_length=100)
    vote = models.IntegerField(default=0)
    image = models.ImageField(upload_to='pol_images')

    def __str__(self):
        return self.option

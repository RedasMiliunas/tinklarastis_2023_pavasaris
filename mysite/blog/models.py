from django.db import models
from django.contrib.auth.models import User
# from datetime import date
from tinymce.models import HTMLField


# Create your models here.
class Post(models.Model):
    title = models.CharField(verbose_name='Pavadinimas', max_length=50)
    text = HTMLField(verbose_name='Tekstas', max_length=5000)
    author = models.ForeignKey(to=User, verbose_name='Autorius', on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name='Data', auto_now_add=True)

    def num_comments(self):
        return len(Comment.objects.filter(post=self.pk))    #sioje vietoje del post len (skaiciaus) parasyta funkcija
    class Meta:
        ordering = ['-date']    #ordering parametras kaip mes rikiuojame, prirasom '-', kad butu nuo naujausio iraso

class Comment(models.Model):
    post = models.ForeignKey(to='Post', verbose_name='Straipsnis', on_delete=models.CASCADE, related_name='comments')
    body = models.TextField(verbose_name='Tekstas', max_length=5000)
    author = models.ForeignKey(to=User, verbose_name='Autorius', on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name='Data', auto_now_add=True)

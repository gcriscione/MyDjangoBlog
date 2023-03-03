from django.db import models

# Create your models here.
class Post(models.Model):
    titolo = models.CharField(max_length=120)
    contenuto = models.TextField()
    data = models.DateTimeField(auto_now=False, auto_now_add=True)
    slag = models.SlugField()

    def __str__(self) -> str:
        return self.titolo
from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    titolo = models.CharField(max_length=120)
    contenuto = models.TextField()
    data = models.DateTimeField(auto_now=False, auto_now_add=True)
    slug = models.SlugField()

    def __str__(self) -> str:
        return self.titolo
    
    # restituisce l'URL assoluto per un oggetto di tipo Post,
    # basato sul nome della vista post_singolo
    def get_absolute_url(self):
        return reverse("post_singolo", kwargs={"pk": self.pk, "slug": self.slug })


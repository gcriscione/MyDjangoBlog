from django.views.generic import ListView
from posts.models import Post

# Create your views here.
class Lista_post(ListView):
    template_name = 'posts\lista_post.html'
    queryset = Post.objects.all().order_by("data")
    paginate_by = 5;
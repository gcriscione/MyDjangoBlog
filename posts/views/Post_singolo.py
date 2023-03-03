from django.views.generic import DetailView
from posts.models import Post

# Create your views here.
class Post_singolo(DetailView):
    template_name = 'posts\post_singolo.html'
    model = Post


    
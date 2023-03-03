from django.views.generic.base import TemplateView

# Create your views here.
class Post_singolo(TemplateView):
    template_name = 'posts\post_singolo.html'
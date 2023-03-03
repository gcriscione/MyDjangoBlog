from django.urls import path

# importa le view definite nella cartella views
# importate definire __init__.py!
from . import views


urlpatterns = [
    path('', views.Lista_post.as_view(), name='lista_post'),
    path('post-singolo/', views.Post_singolo.as_view(), name='post_singolo'),
    path('contatti', views.Contatti.as_view(), name='contatti'),
]
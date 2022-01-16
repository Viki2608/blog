from django.urls import path


from . import views
from .views import AddPostView, DetailView

urlpatterns = [
    path("", views.frontpage, name="frontpage"),
    path("article/<int:pk>",views.DetailView.as_view(),name='article-detail'),
    path('add_post/',views.AddPostView.as_view(),name='add_post'),

]

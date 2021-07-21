'''Urls to blog'''
# Django
from django.urls import path
# Views
from . import views

app_name = 'blog'

urlpatterns = [
    path(route='',
         view=views.PostMainPage.as_view(),
         name='main_page'),

    path(route='blog/search/',
         view=views.search,
         name='post_search'),

    path(route='blog/pasive/',
         view=views.PasiveView.as_view(),
         name='pasive'),

    path(route='blog/active/',
         view=views.ActiveView.as_view(),
         name='active'),

    path(route='blog/diode/<slug>/',
         view=views.DiodesDetailView.as_view(),
         name='details'),

    path(route='blog/transitor/<slug>/',
         view=views.TransistorDetailView.as_view(),
         name='details_t'),

    path(route='blog/post/<slug>/',
         view=views.PostDetailView.as_view(),
         name='post_details'),
]

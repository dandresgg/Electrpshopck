#Django
from django.urls import path
#Views
from . import views

app_name = 'blog'

urlpatterns =[
	path(route = '',
		view = views.PostMainPage.as_view(),
		name = 'main_page'),	

	path(route ='blog/search/', 
		view = views.post_search, 
		name='post_search'),

	path(route = 'blog/pasive/',
		view = views.PasiveView.as_view(),
		name = 'pasive'),

	path(route = 'blog/active/',
		view = views.ActiveView.as_view(),
		name = 'active'),

	path(route = 'blog/<slug>/',
		view = views.DiodesDetailView.as_view(),
		name = 'details'),	
]
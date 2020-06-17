#Django
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Post, Resistors, Capacitors, Diodes, Transistors


# Create your views here.

class PostMainPage(ListView):
	'''returning all published posts'''
	template_name = 'blog/main_page.html'
	context_object_name = 'posts'
	queryset = Post.objects.all()
	sucucces_url = reverse_lazy('blog:main_page')


class PasiveView(ListView):
	'''return pasive components'''
	template_name = 'blog/pasive_components.html'
	context_object_name = 'pasive'
	queryset = Post.objects.all()
	sucucces_url = reverse_lazy('blog:pasive')

	def get_context_data(self, *args, **kwargs):
		resistors_m = Resistors.objects.filter(division__contains='metal_film')
		resistors_p = Resistors.objects.filter(division__contains='power')
		resistors_potenciometer = Resistors.objects.filter(division__contains='potenciomenter')
		resistors_trimmer = Resistors.objects.filter(division__contains='acuracy')
		resistors_general = Resistors.objects.filter(division__contains='general')
		capacitors = Capacitors.objects.all()
		diodes = Diodes.objects.all()
		devise = 'Dispositivos Pasivos'
		context = {
			'resistors_m':resistors_m,
			'resistors_p':resistors_p,
			'resistors_potenciometer':resistors_potenciometer,
			'resistors_trimmer': resistors_trimmer,	
			'capacitors':capacitors,
			'resistors_general':resistors_general,
			'diodes':diodes,
			'devise':devise,
		}
		return context


class ActiveView(ListView):
	'''retunr active components'''
	template_name = 'blog/active_components.html'
	context_object_name = 'active'
	queryset = Post.objects.all()
	sucucces_url = reverse_lazy('blog:active')

	def get_context_data(self, *args, **kwargs):
		transistors = Transistors.objects.all()
		devise = 'Dispositivos Activos'
		context = {
			'transistors':transistors,
			'devise':devise
		}
		return context


class CapacitorsDetailView(DetailView):
	'''Componet's details'''
	template_name = 'blog/component_detail.html'
	slug_field = 'slug'
	slug_url_kwarg = 'slug'
	queryset = Capacitors.objects.all()
	context_object_name = 'component'
	sucucces_url = reverse_lazy('blog:details')



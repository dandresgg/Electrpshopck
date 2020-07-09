#Django
from django.views.generic import ListView, DetailView
from django.urls import reverse_lazy
from .models import Post, Resistors, Capacitors, Diodes, Transistors
from .forms import SearchForm
from django.contrib.postgres.search import SearchVector
from django.shortcuts import render


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
		#Resistors
		resistors_c = Resistors.objects.filter(division__contains='carbon')
		resistors_t = Resistors.objects.filter(division__contains='termistor')
		resistors_potenciometer = Resistors.objects.filter(division__contains='potenciometer')
		resistors_trimmer = Resistors.objects.filter(division__contains='accuracy')
		resistors_general = Resistors.objects.filter(division__contains='general')
		#Capacitors
		capacitors_g = Capacitors.objects.filter(division__contains='general')
		capacitors_c = Capacitors.objects.filter(division__contains='ceramic')
		capacitors_e = Capacitors.objects.filter(division__contains='electrolitic')
		capacitors_p = Capacitors.objects.filter(division__contains='polyester')
		#Diodes
		diodes_g 	= Diodes.objects.filter(division__contains='general')
		diodes_r 	= Diodes.objects.filter(division__contains='rectifier') 
		diodes_z	= Diodes.objects.filter(division__contains='zener')  
		diodes_led	= Diodes.objects.filter(division__contains='l.e.d')
		diodes_schottky	= Diodes.objects.filter(division__contains='shottky')
		diodes_d	= Diodes.objects.filter(division__contains='device')

		devise = 'Dispositivos Pasivos'
		context = {
			#resistors context
			'resistors_general':resistors_general,
			'resistors_c':resistors_c,
			'resistors_t':resistors_t,
			'resistors_potenciometer':resistors_potenciometer,
			'resistors_trimmer': resistors_trimmer,	
			#Capacitors context
			'capacitors_g':capacitors_g,
			'capacitors_c':capacitors_c,
			'capacitors_e':capacitors_e,
			'capacitors_p':capacitors_p,
			#Diodes context
			'diodes_g':diodes_g,
			'diodes_r':diodes_r,
			'diodes_z':diodes_z,
			'diodes_led':diodes_led,
			'diodes_schottky': diodes_schottky,
			'diodes_d': diodes_d,
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
		transistors_g 	= Transistors.objects.filter(division__contains='general')
		transistors_b 	= Transistors.objects.filter(division__contains='bipolar') 
		transistors_j 	= Transistors.objects.filter(division__contains='jfet') 
		transistors_m 	= Transistors.objects.filter(division__contains='mosfet') 
		transistors_p	= Transistors.objects.filter(division__contains='fototransistor')
		transistors_d	= Transistors.objects.filter(division__contains='device') 
		devise = 'Dispositivos Activos'
		context = {
			'transistors_g':transistors_g,
			'transistors_b':transistors_b,
			'transistors_j':transistors_j,
			'transistors_m':transistors_m,
			'transistors_d':transistors_d,
			'devise':devise,
		}
		return context


def search(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        print(query)
        if form.is_valid():
        	'''querys'''
	        query = form.cleaned_data['query']
	        
	        '''results'''
	        try:
	        	results = Post.published.annotate(
	            search=SearchVector('title', 'body'),
		        ).filter(search=query)
		        if not results:
		        	results = Resistors.published.annotate(
		        		search=SearchVector('title', 'description'),
		        		).filter(search=query) 
		        if not results:
		        	results = Capacitors.published.annotate(
		        		search=SearchVector('title', 'description'),
		        		).filter(search=query)   
		        if not results:
		        	results = Diodes.published.annotate(
		        		search=SearchVector('title', 'description'),
		        		).filter(search=query)
		        if not results:
		        	results = Transistors.published.annotate(
		        		search=SearchVector('title', 'description'),
		        		).filter(search=query)     					        				

	        except Exception as e:
	        	raise
	        else:
	        	pass
	        finally:
	        	pass
	        
	       
    return render(request,
                  'blog/search.html',
                  {'form': form,
                   'query': query,
                   'results': results})


class DiodesDetailView(DetailView):
	'''Componet's details'''
	template_name = 'blog/component_detail.html'
	slug_field = 'slug'
	slug_url_kwarg = 'slug'
	queryset = Diodes.objects.filter(division__contains='device')
	context_object_name = 'component'
	sucucces_url = reverse_lazy('blog:details')

class TransistorDetailView(DetailView):
	'''Componet's details'''
	template_name = 'blog/component_detail.html'
	slug_field = 'slug'
	slug_url_kwarg = 'slug'
	queryset = Transistors.objects.filter(division__contains='device')
	context_object_name = 'component'
	sucucces_url = reverse_lazy('blog:details_t')


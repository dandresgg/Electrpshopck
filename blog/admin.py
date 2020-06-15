from django.contrib import admin
from .models import Post, Resistors, Capacitors, Diodes, Transistors

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'publish', 'status')
	list_filter = ('status', 'created', 'publish')
	search_filter = ('title')

@admin.register(Resistors)
class ResistordAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'publish', 'status')
	list_filter = ('status', 'created', 'publish')
	search_filter = ('title')

@admin.register(Capacitors)
class CapacitorsAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'publish', 'status')
	list_filter = ('status', 'created', 'publish')
	search_filter = ('title')

@admin.register(Diodes)
class DiodesAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'publish', 'status')
	list_filter = ('status', 'created', 'publish')
	search_filter = ('title')

@admin.register(Transistors)
class TransistorsAdmin(admin.ModelAdmin):
	list_display = ('title', 'slug', 'author', 'publish', 'status')
	list_filter = ('status', 'created', 'publish')
	search_filter = ('title')


	

"""
Register to admin
"""
# Django
from django.contrib import admin
from .models import Post, Resistors, Capacitors, Diodes, Transistors


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    '''Post admin class'''
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish')
    search_filter = ('title')


@admin.register(Resistors)
class ResistordAdmin(admin.ModelAdmin):
    '''Resistor admin class'''
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish')
    search_filter = ('title')


@admin.register(Capacitors)
class CapacitorsAdmin(admin.ModelAdmin):
    '''Capacitor admin class'''
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish')
    search_filter = ('title')


@admin.register(Diodes)
class DiodesAdmin(admin.ModelAdmin):
    '''Diodes admin class'''
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish')
    search_filter = ('title')


@admin.register(Transistors)
class TransistorsAdmin(admin.ModelAdmin):
    '''Transistors admin class'''
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish')
    search_filter = ('title')

from django.contrib import admin
from django.db import models

# Models
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """Post admin"""
    list_display = (
        'pk', 
        'user', 
        'profile',
        'title', 
        'photo',
        'created', 
        'modified'
    )
    
    list_display_links = (
        'pk',
        'user'
    )
    
    list_editable = (
        'title',
    )
    
    list_filter = (
        'created', 
        'modified',
        'user__is_active',
        'user__is_staff',
    )

    fieldsets = (
        ('Profile', {
            'fields':(
                ('user'),
                ('title','photo')
            )
        }),
        ('Metadata', {
            'fields':(
                ('created', 'modified')
            )
        })
    )
    readonly_fields= ('user','created', 'modified')

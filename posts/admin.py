# Django
from django.contrib import admin

# Posts
from posts.models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'title', 'created', 'modified')
    list_display_links = ('pk','title')
    list_filter = ('user__username','title')
    search_fields = ('user__username','title')

    fieldsets = (
        ('Post Data', {
            "fields": (
                ('user','profile',),
                ('title','photo')
            ),
        }),
        ('Metadata', {
            'fields': (
                ('created','modified',),
            ),
        })
    )

    readonly_fields = (
        'created', 'modified'
    )

admin.site.register(Post, PostAdmin)
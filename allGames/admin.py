from django.contrib import admin
from allGames.models import Game, Sponsor, Recommend, Comment
from django.db import models
from tinymce.widgets import TinyMCE

class PostAdmin(admin.ModelAdmin):
    formfield_overrides = {
        models.TextField: {"widget": TinyMCE},
    }

admin.site.register(Game, PostAdmin)
admin.site.register(Sponsor)
admin.site.register(Recommend, PostAdmin)
admin.site.register(Comment)

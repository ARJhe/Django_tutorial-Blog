from django.contrib import admin
from .models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    exclude = ('author',)
    list_display = ('title', 'content', 'date_posted', 'author')
    # To access the logged in user, you need access to the "request" object.
    def changelist_view(self, request, extra_context=None):
        setattr(self, 'user', request.user)
        return super().changelist_view(request, extra_context)
    # exclude 'author' so that doesn't need to fill this field
    # and overwrite save_model to save automatically.
    def save_model(self, request, obj, form, change):
        if not change:
            obj.author = request.user
        obj.save()

admin.site.register(Post, PostAdmin)
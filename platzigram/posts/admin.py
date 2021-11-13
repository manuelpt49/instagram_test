from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#Models
from django.contrib.auth.models import User
from posts.models import Post

# Register your models here.
@admin.register(Post)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk','user', 'profile', 'title', 'photo')



class ProfileInline(admin.StackedInline):
    model = Post
    can_delete = False
    verbose_name_plural = 'posts'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
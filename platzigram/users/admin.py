from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
#Models
from django.contrib.auth.models import User
from users.models import Profile

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('pk','user', 'phone_number', 'website', 'picture')
    list_display_links = ('pk','user')
    list_editable = ('phone_number','website')
    search_fields = ('user__email', 'user__first_name', 'phone_number')
    list_filter = ('user__is_active', 'user__is_staff')

    fieldsets = (
        ('Profile', {
           'fields': ('user', 'picture'),
        }),
        ('Extra info', {
            'fields': (
                ('website', 'phone_number'),
                ('biography')
            )
        }),
        ('Meta data',{
            'fields': (
                ('created', 'modified'),
            )
        })
    )

    readonly_fields = ('created','modified','user')

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'profiles'

class UserAdmin(BaseUserAdmin):
    inlines = (ProfileInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
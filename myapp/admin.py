from django.contrib import admin

from .models import User



from django.urls import path


class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'is_admin')
    list_filter = ('is_admin',)
    search_fields = ('username', 'email')

admin.site.register(User, UserAdmin)


urlpatterns = [
    path('admin/', admin.site.urls),
    # Other URL patterns for your application
]





from django.contrib import admin

# RegisterView your models here.
from openbook_auth.models import User, UserProfile
from openbook_categories.models import Category


class CategoryInline(admin.TabularInline):
    model = Category.users.through


class UserProfileInline(admin.TabularInline):
    model = UserProfile

    def has_delete_permission(self, request, obj=None):
        return False


class UserAdmin(admin.ModelAdmin):
    inlines = [
        UserProfileInline,
        CategoryInline,
    ]
    search_fields = ('username',)
    list_display = ('username', 'is_staff', 'is_superuser')
    list_filter = ('is_staff', 'is_superuser')

    exclude = ('password',)

    def has_add_permission(self, request, obj=None):
        return False


admin.site.register(User, UserAdmin)

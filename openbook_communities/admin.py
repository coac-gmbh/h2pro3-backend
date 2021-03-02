from django.contrib import admin

from openbook_communities.models import Community
from openbook_categories.models import Category

class CategoryInline(admin.TabularInline):
    model = Category.communities.through

class CommunityAdmin(admin.ModelAdmin):
    inlines = [
        CategoryInline,
    ]


admin.site.register(Community, CommunityAdmin)

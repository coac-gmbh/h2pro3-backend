from django.contrib import admin

from openbook_communities.models import Community
from openbook_categories.models import Category


class CategoryInline(admin.TabularInline):
    model = Category.communities.through


class CommunityAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ('creator', 'name', 'title', 'description', 'rules')}),
        (None, {'fields': ('avatar', 'cover', 'starrers')}),
        ('H2pro3', {'fields': ('group_type', 'about_us', 'website', 'closed')}),
        ('City', {'classes': ['collapse'], 'fields': ('population', 'area', 'energy_demand')}),
        ('Company', {'classes': ['collapse'], 'fields': ('industry', 'employee', 'location')}),
        ('University', {'classes': ['collapse'], 'fields': ('institution', 'departments')}),
    ]
    inlines = [
        CategoryInline,
    ]


admin.site.register(Community, CommunityAdmin)

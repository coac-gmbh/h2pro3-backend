from django.contrib import admin

from openbook_communities.models import Community


class CommunityAdmin(admin.ModelAdmin):
    pass


admin.site.register(Community, CommunityAdmin)

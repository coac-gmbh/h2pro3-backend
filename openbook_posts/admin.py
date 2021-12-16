from django.contrib import admin

# RegisterView your models here.
from openbook_circles.models import Circle
from openbook_posts.models import Post, PostImage, PostComment, PostReaction, TrendingPost, TopPost


class PostImageInline(admin.TabularInline):
    model = PostImage

    def has_delete_permission(self, request, obj=None):
        return False


class PostCommentInline(admin.TabularInline):
    model = PostComment

    readonly_fields = (
        'commenter',
        'text',
        'created'
    )

    def has_add_permission(self, request, obj):
        return False


class PostReactionInline(admin.TabularInline):
    model = PostReaction

    readonly_fields = [
        'reactor',
        'emoji'
    ]

    def has_add_permission(self, request, obj):
        return False


class PostCircleInline(admin.TabularInline):
    model = Circle.posts.through

    def has_delete_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_add_permission(self, request, obj):
        return False


class PostAdmin(admin.ModelAdmin):
    inlines = [
        PostReactionInline,
        PostImageInline,
        PostCommentInline,
        PostCircleInline
    ]

    list_display = (
        'id',
        'created',
        'creator',
        'community',
        'text_truncated',
        'count_comments',
        'count_reactions',
        'has_text',
        'has_image'
    )

    search_fields = ['id', 'creator__username', 'community__name', 'text']

    def has_add_permission(self, request, obj=None):
        return False

    def has_change_permission(self, request, obj=None):
        return False


class TrendingPostAdmin(admin.ModelAdmin):
    raw_id_fields = ('post',)
    list_display = ('post', 'created')


class TopPostAdmin(admin.ModelAdmin):
    raw_id_fields = ('post',)
    list_display = ('post', 'created')


admin.site.register(Post, PostAdmin)
admin.site.register(TrendingPost, TrendingPostAdmin)
admin.site.register(TopPost, TopPostAdmin)

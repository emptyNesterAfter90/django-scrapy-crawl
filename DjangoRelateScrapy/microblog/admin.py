from django.contrib import admin

# Register your models here.
from microblog.models import HotSpot, FreshNews, FunnyStory, Society, Fashion, TopEvent, TopList


@admin.register(HotSpot)
class SpotAdmin(admin.ModelAdmin):
    # 设置页面列的名称
    list_display = ['pk', 'content', 'author', 'publishTime', 'repost',
                    'comment', 'approve', 'address', 'image']
    list_per_page = 10

    ordering = ('pk',)

    search_fields = ['content']

    # 执行动作的位置
    actions_on_bottom = True
    actions_on_top = False


@admin.register(FreshNews)
class SpotAdmin(admin.ModelAdmin):
    # 设置页面列的名称
    list_display = ['pk', 'content', 'author', 'publishTime', 'image', 'address']
    list_per_page = 10

    ordering = ('pk',)

    search_fields = ['content']

    # 执行动作的位置
    actions_on_bottom = True
    actions_on_top = False


@admin.register(FunnyStory)
class SpotAdmin(admin.ModelAdmin):
    # 设置页面列的名称
    list_display = ['pk', 'content', 'author', 'publishTime', 'repost',
                    'comment', 'approve', 'address', 'image']
    list_per_page = 10

    ordering = ('pk',)

    search_fields = ['content']

    # 执行动作的位置
    actions_on_bottom = True
    actions_on_top = False


@admin.register(Society)
class SpotAdmin(admin.ModelAdmin):
    # 设置页面列的名称
    list_display = ['pk', 'content', 'author', 'publishTime', 'repost',
                    'comment', 'approve', 'address', 'image']
    list_per_page = 10

    ordering = ('pk',)

    search_fields = ['content']

    # 执行动作的位置
    actions_on_bottom = True
    actions_on_top = False


@admin.register(Fashion)
class SpotAdmin(admin.ModelAdmin):
    # 设置页面列的名称
    list_display = ['pk', 'content', 'author', 'publishTime', 'repost',
                    'comment', 'approve', 'address', 'image']
    list_per_page = 10

    ordering = ('pk',)

    search_fields = ['content']

    # 执行动作的位置
    actions_on_bottom = True
    actions_on_top = False


@admin.register(TopEvent)
class SpotAdmin(admin.ModelAdmin):
    # 设置页面列的名称
    list_display = ['pk', 'content', 'author', 'publishTime', 'repost',
                    'comment', 'approve', 'address', 'image']
    list_per_page = 10

    ordering = ('pk',)

    search_fields = ['content']

    # 执行动作的位置
    actions_on_bottom = True
    actions_on_top = False


@admin.register(TopList)
class SpotAdmin(admin.ModelAdmin):
    # 设置页面列的名称
    list_display = ['pk', 'content', 'author', 'publishTime', 'repost',
                    'comment', 'approve', 'address', 'image']
    list_per_page = 10

    ordering = ('pk',)

    search_fields = ['content']

    # 执行动作的位置
    actions_on_bottom = True
    actions_on_top = False



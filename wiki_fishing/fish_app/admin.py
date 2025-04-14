from django.contrib import admin
from fish_app.models import Fish, Bait, FishBaitRelation

class FishAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'habitat', 'avg_weight', 'season_activity')
    list_filter = ('type', 'habitat', 'season_activity', 'is_red_book')
    search_fields = ('name', 'scientific_name', 'description')
    readonly_fields = ('get_size_info',)
    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'scientific_name', 'type', 'description', 'image')
        }),
        ('Среда обитания', {
            'fields': ('habitat', 'area')
        }),
        ('Характеристики', {
            'fields': (('avg_weight', 'max_weight', 'avg_length'), 'get_size_info')
        }),
    )


class BaitAdmin(admin.ModelAdmin):
    list_display = ('name', 'type', 'target_fish', 'price_category', 'rating')
    list_filter = ('type', 'target_fish', 'price_category')
    search_fields = ('name', 'description')

    fieldsets = (
        ('Основная информация', {
            'fields': ('name', 'type', 'description', 'image')
        }),
        ('Характеристики', {
            'fields': ('target_fish', 'price_category', 'rating')
        }),
    )


class FishBaitRelationAdmin(admin.ModelAdmin):
    list_display = ('fish', 'bait', 'efficiency')
    list_filter = ('bait__type', 'fish__type')
    search_fields = ('fish__name', 'bait__name')


admin.site.register(Fish, FishAdmin)
admin.site.register(Bait, BaitAdmin)
admin.site.register(FishBaitRelation, FishBaitRelationAdmin)
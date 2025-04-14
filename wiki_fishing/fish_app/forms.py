from django import forms
from .models import Fish, Bait

class FishForm(forms.ModelForm):
    class Meta:
        model = Fish
        fields = [
            'name', 'scientific_name', 'type', 'description', 'image',
            'habitat', 'area', 'season_activity', 'best_catch_time',
            'optimal_temperature', 'temperature_range', 'is_red_book',
            'avg_weight', 'max_weight', 'avg_length'
        ]


class BaitForm(forms.ModelForm):
    class Meta:
        model = Bait
        fields = [
            'name', 'type', 'description', 'image',
            'target_fish', 'price_category', 'rating'
        ]
#        exclude = ['baits']  # Исключаем поле baits из автоматического добавления


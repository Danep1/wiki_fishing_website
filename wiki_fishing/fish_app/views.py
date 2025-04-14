import random

from django.shortcuts import render, get_object_or_404, redirect

from .forms import FishForm, BaitForm
from .models import Fish, Bait, FishBaitRelation

def index(request):
    # Получаем случайную рыбу и приманку
    fish_count = Fish.objects.count()
    bait_count = Bait.objects.count()

    random_fish = Fish.objects.all()[random.randint(0, fish_count - 1)] if fish_count > 0 else None
    random_bait = Bait.objects.all()[random.randint(0, bait_count - 1)] if bait_count > 0 else None

    return render(request, 'index.html', {
        'random_fish': random_fish,
        'random_bait': random_bait
    })

def fish_list(request):
    fishes = Fish.objects.all().order_by('name')
    return render(request, 'fish_list.html', {'fishes': fishes})

def fish_detail(request, fish_id):
    fish = get_object_or_404(Fish, pk=fish_id)
    baits = fish.baits.all()  # Используем related_name из FishBaitRelation
    return render(request, 'fish_detail.html', {'fish': fish, 'baits': baits})

def bait_list(request):
    baits = Bait.objects.all().order_by('name')
    return render(request, 'bait_list.html', {'baits': baits})

def bait_detail(request, bait_id):
    bait = get_object_or_404(Bait, pk=bait_id)
    # Получаем связи с рыбами и сразу выбираем нужные поля
    relations = FishBaitRelation.objects.filter(bait=bait).select_related('fish')
    return render(request, 'bait_detail.html', {
        'bait': bait,
        'relations': relations  # Передаем связи вместо рыб
    })

def add_fish(request):
    if request.method == 'POST':
        form = FishForm(request.POST, request.FILES)
        if form.is_valid():
            fish = form.save()
            baits = request.POST.getlist('baits')
            for bait_id in baits:
                bait = Bait.objects.get(id=bait_id)
                FishBaitRelation.objects.create(fish=fish, bait=bait, efficiency=3)  # Установите efficiency по умолчанию
            return redirect('fish_list')  # Перенаправление на список рыб после успешного добавления
    else:
        form = FishForm()
    baits = Bait.objects.all()
    return render(request, 'add_fish.html', {'form': form, 'baits': baits})

def add_bait(request):
    if request.method == 'POST':
        form = BaitForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('bait_list')  # Перенаправление на список приманок после успешного добавления
    else:
        form = BaitForm()
    return render(request, 'add_bait.html', {'form': form})
import os
from django.core.files import File
from django.core.management.base import BaseCommand
from fish_app.models import Fish, Bait, FishBaitRelation
from django.conf import settings

class Command(BaseCommand):
    help = 'Загружает тестовые данные с изображениями'

    def handle(self, *args, **options):
        # Пути к изображениям (относительно MEDIA_ROOT)
        IMAGE_PATHS = {
            'baits': {
                'Червь дождевой': 'baits\\common_worm.png',
                'Блесна': 'baits\\lure.png',
            },
            'fish': {
                'Карп': 'fish\\carp.png',
                'Ёрш': 'fish\\ruffe.png',
                'Окунь': 'fish\\bass.png',
            }
        }

        # Очистка старых данных
        Fish.objects.all().delete()
        Bait.objects.all().delete()
        FishBaitRelation.objects.all().delete()

        def add_image_to_instance(instance, image_path):
            if image_path:
                full_path = os.path.join(settings.MEDIA_ROOT, image_path)
                if os.path.exists(full_path):
                    # Сохраняем в нужную папку без создания копии
                    instance.image.name = image_path  # Прямое указание пути
                    instance.save()
                    self.stdout.write(self.style.SUCCESS(
                        f'Изображение {image_path} привязано к {instance}'
                    ))

        # Добавляем рыб с изображениями
        fish_data = [
            {
                'name': 'Карп',
                'scientific_name': 'Cyprinus carpio',
                'type': 'peaceful',
                'description': 'Крупная пресноводная рыба семейства карповых.',
                'habitat': 'fresh',
                'area': 'Европа, Азия',
                'season_activity': 'summer',
                'best_catch_time': 'all_day',
                'avg_weight': 3,
                'max_weight': 40,
                'avg_length': 50,
                'image': IMAGE_PATHS['fish']['Карп']
            },
            {
                'name': 'Ёрш',
                'scientific_name': 'Gymnocephalus cernua',
                'type': 'predator',
                'description': 'Небольшая хищная рыба с колючими плавниками.',
                'habitat': 'fresh',
                'area': 'Европа, Северная Азия',
                'season_activity': 'all_season',
                'best_catch_time': 'evening',
                'avg_weight': 0.1,
                'max_weight': 0.5,
                'avg_length': 15,
                'image': IMAGE_PATHS['fish']['Ёрш']
            },
            {
                'name': 'Окунь',
                'scientific_name': 'Perca fluviatilis',
                'type': 'predator',
                'description': 'Хищник с характерными полосами по бокам.',
                'habitat': 'fresh',
                'area': 'Европа, Северная Азия',
                'season_activity': 'all_season',
                'best_catch_time': 'morning',
                'avg_weight': 0.5,
                'max_weight': 4.5,
                'avg_length': 25,
                'image': IMAGE_PATHS['fish']['Окунь']
            }
        ]

        for data in fish_data:
            fish = Fish.objects.create(**{k: v for k, v in data.items() if k != 'image'})
            add_image_to_instance(fish, data['image'])

        # Добавляем приманки с изображениями
        bait_data = [
            {
                'name': 'Червь дождевой',
                'type': 'bait',
                'description': 'Универсальная натуральная наживка.',
                'target_fish': 'universal',
                'price_category': 'low',
                'rating': 5,
                'image': IMAGE_PATHS['baits']['Червь дождевой']
            },
            {
                'name': 'Блесна',
                'type': 'lure',
                'description': 'Искусственная приманка для хищных рыб.',
                'target_fish': 'predator',
                'price_category': 'high',
                'rating': 4,
                'image': IMAGE_PATHS['baits']['Блесна']
            }
        ]

        for data in bait_data:
            bait = Bait.objects.create(**{k: v for k, v in data.items() if k != 'image'})
            add_image_to_instance(bait, data['image'])

        # Создаём связи между рыбами и приманками
        relations = [
            {'fish': 'Карп', 'bait': 'Червь дождевой', 'efficiency': 5, 'notes': 'Лучше работает в тёплой воде'},
            {'fish': 'Ёрш', 'bait': 'Червь дождевой', 'efficiency': 4, 'notes': 'Клюёт на мелкого червя'},
            {'fish': 'Окунь', 'bait': 'Червь дождевой', 'efficiency': 3, 'notes': 'Предпочитает красных червей'},
            {'fish': 'Окунь', 'bait': 'Блесна', 'efficiency': 5, 'notes': 'Идеальна блесна 3-5 см'}
        ]

        for rel in relations:
            fish = Fish.objects.get(name=rel['fish'])
            bait = Bait.objects.get(name=rel['bait'])
            FishBaitRelation.objects.create(fish=fish, bait=bait, efficiency=rel['efficiency'], notes=rel['notes'])

        self.stdout.write(self.style.SUCCESS('Успешно загружены тестовые данные с изображениями'))
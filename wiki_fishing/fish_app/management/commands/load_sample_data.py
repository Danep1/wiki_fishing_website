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
                'Опарыш': 'baits\\maggot.jpg',
                'Мотыль': 'baits\\moth.png',
                'Кукуруза': 'baits\\corn.png',
                'Овсянка': 'baits\\oatmeal.png',
                'Хлеб': 'baits\\bread.jpg',
                'Силикон': 'baits\\silicone.jpg',
            },
            'fish': {
                'Карп': 'fish\\carp.png',
                'Ёрш': 'fish\\ruffe.png',
                'Окунь': 'fish\\bass.png',
                'Щука': 'fish\\pike.jpg',
                'Судак': 'fish\\zander.png',
                'Лещ': 'fish\\bream.jpg',
                'Сом': 'fish\\catfish.jpg',
                'Форель': 'fish\\trout.png',
                'Сиг': 'fish\\whitefish.jpg',
                'Плотва': 'fish\\roach.jpg',
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
            },
            {
                'name': 'Щука',
                'scientific_name': 'Esox lucius',
                'type': 'predator',
                'description': 'Крупная хищная рыба с вытянутым телом.',
                'habitat': 'fresh',
                'area': 'Европа, Северная Азия',
                'season_activity': 'spring',
                'best_catch_time': 'morning',
                'avg_weight': 2,
                'max_weight': 20,
                'avg_length': 60,
                'image': IMAGE_PATHS['fish']['Щука']
            },
            {
                'name': 'Судак',
                'scientific_name': 'Sander lucioperca',
                'type': 'predator',
                'description': 'Хищная рыба с крупными зубами.',
                'habitat': 'fresh',
                'area': 'Европа, Северная Азия',
                'season_activity': 'spring',
                'best_catch_time': 'evening',
                'avg_weight': 1,
                'max_weight': 10,
                'avg_length': 40,
                'image': IMAGE_PATHS['fish']['Судак']
            },
            {
                'name': 'Лещ',
                'scientific_name': 'Abramis brama',
                'type': 'peaceful',
                'description': 'Крупная мирная рыба с высоким телом.',
                'habitat': 'fresh',
                'area': 'Европа, Азия',
                'season_activity': 'summer',
                'best_catch_time': 'all_day',
                'avg_weight': 2,
                'max_weight': 8,
                'avg_length': 45,
                'image': IMAGE_PATHS['fish']['Лещ']
            },
            {
                'name': 'Сом',
                'scientific_name': 'Silurus glanis',
                'type': 'predator',
                'description': 'Очень крупная хищная рыба с усами.',
                'habitat': 'fresh',
                'area': 'Европа, Азия',
                'season_activity': 'summer',
                'best_catch_time': 'night',
                'avg_weight': 10,
                'max_weight': 200,
                'avg_length': 150,
                'image': IMAGE_PATHS['fish']['Сом']
            },
            {
                'name': 'Форель',
                'scientific_name': 'Salmo trutta',
                'type': 'predator',
                'description': 'Хищная рыба с красивой окраской.',
                'habitat': 'fresh',
                'area': 'Европа, Северная Америка',
                'season_activity': 'spring',
                'best_catch_time': 'morning',
                'avg_weight': 1,
                'max_weight': 15,
                'avg_length': 40,
                'image': IMAGE_PATHS['fish']['Форель']
            },
            {
                'name': 'Сиг',
                'scientific_name': 'Coregonus lavaretus',
                'type': 'peaceful',
                'description': 'Мирная рыба с серебристым телом.',
                'habitat': 'fresh',
                'area': 'Европа, Северная Америка',
                'season_activity': 'spring',
                'best_catch_time': 'all_day',
                'avg_weight': 1,
                'max_weight': 5,
                'avg_length': 35,
                'image': IMAGE_PATHS['fish']['Сиг']
            },
            {
                'name': 'Плотва',
                'scientific_name': 'Rutilus rutilus',
                'type': 'peaceful',
                'description': 'Небольшая мирная рыба с плоским телом.',
                'habitat': 'fresh',
                'area': 'Европа, Азия',
                'season_activity': 'summer',
                'best_catch_time': 'all_day',
                'avg_weight': 0.5,
                'max_weight': 2,
                'avg_length': 20,
                'image': IMAGE_PATHS['fish']['Плотва']
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
            },
            {
                'name': 'Опарыш',
                'type': 'bait',
                'description': 'Натуральная наживка для мирных рыб.',
                'target_fish': 'peaceful',
                'price_category': 'low',
                'rating': 4,
                'image': IMAGE_PATHS['baits']['Опарыш']
            },
            {
                'name': 'Мотыль',
                'type': 'bait',
                'description': 'Натуральная наживка для мирных рыб.',
                'target_fish': 'peaceful',
                'price_category': 'low',
                'rating': 3,
                'image': IMAGE_PATHS['baits']['Мотыль']
            },
            {
                'name': 'Кукуруза',
                'type': 'bait',
                'description': 'Натуральная наживка для мирных рыб.',
                'target_fish': 'peaceful',
                'price_category': 'low',
                'rating': 3,
                'image': IMAGE_PATHS['baits']['Кукуруза']
            },
            {
                'name': 'Овсянка',
                'type': 'bait',
                'description': 'Натуральная наживка для мирных рыб.',
                'target_fish': 'peaceful',
                'price_category': 'low',
                'rating': 3,
                'image': IMAGE_PATHS['baits']['Овсянка']
            },
            {
                'name': 'Хлеб',
                'type': 'bait',
                'description': 'Натуральная наживка для мирных рыб.',
                'target_fish': 'peaceful',
                'price_category': 'low',
                'rating': 3,
                'image': IMAGE_PATHS['baits']['Хлеб']
            },
            {
                'name': 'Силикон',
                'type': 'lure',
                'description': 'Искусственная приманка для хищных рыб.',
                'target_fish': 'predator',
                'price_category': 'high',
                'rating': 4,
                'image': IMAGE_PATHS['baits']['Силикон']
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
            {'fish': 'Окунь', 'bait': 'Блесна', 'efficiency': 5, 'notes': 'Идеальна блесна 3-5 см'},
            {'fish': 'Щука', 'bait': 'Блесна', 'efficiency': 5, 'notes': 'Идеальна блесна 10-15 см'},
            {'fish': 'Судак', 'bait': 'Блесна', 'efficiency': 5, 'notes': 'Идеальна блесна 5-10 см'},
            {'fish': 'Лещ', 'bait': 'Опарыш', 'efficiency': 4, 'notes': 'Лучше работает в тёплой воде'},
            {'fish': 'Сом', 'bait': 'Червь дождевой', 'efficiency': 5, 'notes': 'Лучше работает в тёплой воде'},
            {'fish': 'Форель', 'bait': 'Блесна', 'efficiency': 5, 'notes': 'Идеальна блесна 3-5 см'},
            {'fish': 'Сиг', 'bait': 'Опарыш', 'efficiency': 4, 'notes': 'Лучше работает в тёплой воде'},
            {'fish': 'Плотва', 'bait': 'Опарыш', 'efficiency': 4, 'notes': 'Лучше работает в тёплой воде'}
        ]

        for rel in relations:
            fish = Fish.objects.get(name=rel['fish'])
            bait = Bait.objects.get(name=rel['bait'])
            FishBaitRelation.objects.create(fish=fish, bait=bait, efficiency=rel['efficiency'], notes=rel['notes'])

        self.stdout.write(self.style.SUCCESS('Успешно загружены тестовые данные с изображениями'))

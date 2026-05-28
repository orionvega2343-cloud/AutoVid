from django.core.management.base import BaseCommand
from catalog.models import CarModel, Brand, Part


class Command(BaseCommand):
    help = 'Заполняет базу тестовыми данными Auto-VID'

    def handle(self, *args, **kwargs):
        self.stdout.write('Начало наполнения базы...')

        Part.objects.all().delete()
        Brand.objects.all().delete()
        CarModel.objects.all().delete()

        car1 = CarModel.objects.create(brand='Renault', name='Master', generation='II (1997-2010)')
        car2 = CarModel.objects.create(brand='Renault', name='Master', generation='III (2010-2024)')
        car3 = CarModel.objects.create(brand='Lada', name='Largus', generation='I (2012-2021)')
        car4 = CarModel.objects.create(brand='Renault', name='Trafic', generation='II (2001-2014)')
        car5 = CarModel.objects.create(brand='Opel', name='Movano', generation='A (1998-2010)')
        car6 = CarModel.objects.create(brand='Nissan', name='Primastar', generation='I (2001-2014)')
        self.stdout.write(self.style.SUCCESS('Созданы автомобили'))

        b_renault = Brand.objects.create(name='Renault OEM', country='Франция')
        b_sasic = Brand.objects.create(name='Sasic', country='Франция')
        b_contitech = Brand.objects.create(name='Contitech', country='Германия')
        b_snr = Brand.objects.create(name='SNR', country='Франция')
        b_valeo = Brand.objects.create(name='Valeo', country='Франция')
        b_dayco = Brand.objects.create(name='Dayco', country='США')
        self.stdout.write(self.style.SUCCESS('Созданы бренды'))

        p1 = Part.objects.create(sku='8200674661', name='Фильтр масляный', brand=b_renault, category='filters', price=850, in_stock=15)
        p1.applicable_cars.add(car1, car2)

        p2 = Part.objects.create(sku='4000746', name='Сайлентблок переднего рычага', brand=b_sasic, category='suspension', price=420, in_stock=8)
        p2.applicable_cars.add(car3)

        p3 = Part.objects.create(sku='5PK1750', name='Ремень генератора поликлиновой', brand=b_contitech, category='belts', price=1250, in_stock=0)
        p3.applicable_cars.add(car4, car6)

        p4 = Part.objects.create(sku='7701477642', name='Колодки тормозные передние', brand=b_renault, category='brakes', price=2100, in_stock=12)
        p4.applicable_cars.add(car2, car5)

        p5 = Part.objects.create(sku='8660001483', name='Подшипник ступицы', brand=b_snr, category='suspension', price=1850, in_stock=6)
        p5.applicable_cars.add(car5)

        self.stdout.write(self.style.SUCCESS('База наполнена!'))
        
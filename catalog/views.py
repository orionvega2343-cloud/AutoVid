from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import Http404

# ---------------------------------------------------------------------------
# MOCK-данные (временные, до подключения к моделям БД)
# ---------------------------------------------------------------------------

MOCK_CARS = [
    {'id': 1, 'brand': 'Renault', 'name': 'Master', 'generation': 'III (2010-2024)'},
    {'id': 2, 'brand': 'Lada', 'name': 'Largus', 'generation': 'I (2012-2021)'},
    {'id': 3, 'brand': 'Opel', 'name': 'Movano', 'generation': 'A (1998-2010)'},
]

MOCK_PARTS = [
    {
        'id': 1,
        'sku': '8200674661',
        'name': 'Фильтр масляный',
        'brand': 'Renault OEM',
        'category': 'Фильтры',
        'price': 850,
        'in_stock': 15,
        'car_id': 1,
        'description': 'Оригинальный масляный фильтр для двигателей Renault.',
    },
    {
        'id': 2,
        'sku': '4000746',
        'name': 'Сайлентблок переднего рычага',
        'brand': 'Sasic',
        'category': 'Подвеска',
        'price': 420,
        'in_stock': 8,
        'car_id': 2,
        'description': 'Сайлентблок переднего рычага подвески.',
    },
    {
        'id': 3,
        'sku': '5PK1750',
        'name': 'Ремень генератора поликлиновой',
        'brand': 'Contitech',
        'category': 'Ремни и шкивы',
        'price': 1250,
        'in_stock': 0,
        'car_id': 1,
        'description': 'Поликлиновой ремень привода генератора, профиль 5PK.',
    },
    {
        'id': 4,
        'sku': '7701477642',
        'name': 'Колодки тормозные передние',
        'brand': 'Renault OEM',
        'category': 'Тормозная система',
        'price': 2100,
        'in_stock': 12,
        'car_id': 3,
        'description': 'Комплект передних тормозных колодок.',
    },
    {
        'id': 5,
        'sku': '8660001483',
        'name': 'Подшипник ступицы',
        'brand': 'SNR',
        'category': 'Подвеска',
        'price': 1850,
        'in_stock': 6,
        'car_id': 3,
        'description': 'Передний ступичный подшипник в сборе.',
    },
]


def _get_part_or_404(part_id):
    """Возвращает запчасть из MOCK_PARTS по id или поднимает Http404."""
    for part in MOCK_PARTS:
        if part['id'] == part_id:
            return part
    raise Http404('Запчасть не найдена')


# ---------------------------------------------------------------------------
# Views
# ---------------------------------------------------------------------------

def catalog_view(request):
    """Главная каталога: поиск по артикулу/названию и фильтр по авто."""
    query = request.GET.get('q', '').strip()
    car_id = request.GET.get('car', '').strip()

    parts = MOCK_PARTS

    if query:
        q_lower = query.lower()
        parts = [
            p for p in parts
            if q_lower in p['sku'].lower() or q_lower in p['name'].lower()
        ]

    if car_id:
        try:
            car_id_int = int(car_id)
            parts = [p for p in parts if p['car_id'] == car_id_int]
        except ValueError:
            pass

    context = {
        'parts': parts,
        'cars': MOCK_CARS,
        'query': query,
        'selected_car': car_id,
    }
    return render(request, 'catalog/catalog_list.html', context)


def part_detail_view(request, part_id):
    """Карточка детали по id."""
    part = _get_part_or_404(part_id)
    return render(request, 'catalog/part_detail.html', {'part': part})


def quick_order_view(request, part_id):
    """Приём POST-запроса быстрого заказа: проверка полей и редирект."""
    part = _get_part_or_404(part_id)

    if request.method != 'POST':
        return redirect('catalog:part_detail', part_id=part_id)

    client_name = request.POST.get('client_name', '').strip()
    client_phone = request.POST.get('client_phone', '').strip()

    if not client_name or not client_phone:
        messages.error(request, 'Заполните имя и телефон.')
        return redirect('catalog:part_detail', part_id=part_id)

    # TODO: сохранение заказа в БД (модель Order) на следующем этапе
    messages.success(
        request,
        f'Заказ на «{part["name"]}» принят. Менеджер свяжется с вами.'
    )
    return redirect('catalog:part_detail', part_id=part_id)

# AutoVid - Гайд для разработчиков

## Содержание
[1. Как клонировать](#как-клонировать)<br>
[2. Как активировать venv](#как-активировать-venv)<br>
[3. Как установить зависимости](#как-установить-зависимости)<br>
[4. Как работать с ветками](#как-работать-с-ветками)<br>
[5. Структура проекта](#структура-проекта)<br>

---

## Как клонировать
```bash
git clone https://github.com/orionvega2343-cloud/AutoVid.git
cd AutoVid
```

---

## Как активировать venv
**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```
**Mac/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

---

## Как установить зависимости
```bash
pip install -r requirements.txt
```

---

## Как работать с ветками

Все работают в ветке `develop`. В `main` код попадает только через Pull Request.

**Workflow:**
1. Клонируй репо и переключись на `develop`:
```bash
git checkout develop
```
2. Пиши код, коммить:
```bash
git add .
git commit -m "описание изменений"
git push origin develop
```
3. Когда готово — создай **Pull Request** на GitHub: `develop` → `main`
4. После апрува PR код попадает в `main`

> ⚠️ Прямой пуш в `main` запрещён
> 
> 
### Префиксы коммитов

| Префикс | Когда использовать |
|---|---|
| `feat:` | Новая функциональность |
| `fix:` | Исправление бага |
| `style:` | Верстка, CSS, JS |
| `refactor:` | Рефакторинг кода |
| `docs:` | Изменения в документации |
| `chore:` | Настройка проекта, зависимости |
| `test:` | Тесты |

**Примеры:**
```
feat: добавил модель Product
fix: исправил роутер каталога
style: сверстал шапку сайта
docs: обновил README
```
---


---

## Кто где работает

### Бэкенд разработчик
Работает внутри каждого приложения:
- `models.py` — модели базы данных
- `views.py` — логика страниц
- `urls.py` — роутер
- `admin.py` — настройка админки
- `migrations/` — миграции БД

### Фронтенд разработчик
Работает в:
- `templates/` — HTML шаблоны
- `static/` — CSS, JS, картинки, шрифты

### Все
- Ветка `develop` — рабочая ветка
- `requirements.txt` — если добавил библиотеку, обнови файл:
```bash
pip freeze > requirements.txt
```

---


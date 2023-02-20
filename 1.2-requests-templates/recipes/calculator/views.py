from django.shortcuts import render

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
    'soup puree': {
        'картофель, шт': 3,
        'морковь, шт': 3,
        'лук, шт': 3,
        'тыква, г': 300,
        'сливки, г': 200,
        'паприка, ч.л.': 0.5,
        'соль, ч.л.': 0.5,
        'масло подсолнечное, ст.л.': 2,
        'вода, л': 1,
    },
}


def calculate_view(requests, dish_get):
    servings = int(requests.GET.get('servings', 1))
    send_dish = {}
    for dish, ingredients in DATA.items():
        if dish_get == dish:
            for ing, count in ingredients.items():
                send_dish[ing] = count * servings

    context = {
        'recipe': send_dish
    }

    return render(requests, 'calculator/index.html', context)
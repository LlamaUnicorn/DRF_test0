from django.http import JsonResponse
from app_goods.entities import Item


def items_list(request):
    if request.method == "GET":
        items_for_sale = [
            Item(
                name="Кофеварка",
                description="Варит отличный кофе",
                weight=100),
            Item(
                name="Беспроводные наушники",
                description="Отличный звук",
                weight=150),
        ]
        return JsonResponse(items_for_sale)

from django.http import JsonResponse
from app_goods.entities import Item
from app_goods.serializers import ItemSerializer


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
        # return JsonResponse(ItemSerializer(items_for_sale, many=True).data,
        #                     safe=False)
        return JsonResponse(ItemSerializer(Item(
                    name="Кофеварка",
                    description="Варит отличный кофе",
                    weight=100
                )).data, safe=False)

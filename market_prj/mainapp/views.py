from django.shortcuts import render, get_object_or_404
from .models import Accommodation

def main(request):
    # Можно выводить, например, последние 3 размещения на главной
     latest_accommodations = Accommodation.get_items()[:3]
     return render(request, 'mainapp/index.html', {'latest_accommodations': latest_accommodations})



def accommodations(request):
    # Получаем все активные объекты
    objs = Accommodation.get_items()
    return render(request, 'mainapp/accommodations.html', {'accommodations': objs})

def accommodation(request, pk):
    # Получаем конкретное размещение по pk
    obj = get_object_or_404(Accommodation, pk=pk)
    return render(request, 'mainapp/accommodation_detail.html', {'accommodation': obj})

# def accommodations(request):
#     accommodations_list = (
#         Accommodation.objects
#         .filter(is_active=True)
#         .order_by('country', 'region', 'name')
#     )
#
#     context = {
#         'title': 'размещение',
#         'list_of_accommodations': accommodations_list,
#     }
#     return render(request, 'mainapp/accommodations.html', context)
#
#
# def accommodation(request, pk):
#     acc = get_object_or_404(Accommodation, pk=pk)
#
#     context = {
#         'title': acc.name,
#         'accommodation': acc,
#     }
#     return render(request, 'mainapp/accommodation_detail.html', context)


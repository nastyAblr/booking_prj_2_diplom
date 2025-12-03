from django.shortcuts import render, get_object_or_404
from mainapp.models import Accommodation


def main(request):
    return render(request, 'mainapp/index.html')


def accommodations(request):
    accommodations_list = (
        Accommodation.objects
        .filter(is_active=True)
        .order_by('country', 'region', 'name')
    )

    context = {
        'title': 'размещение',
        'list_of_accommodations': accommodations_list,
    }
    return render(request, 'mainapp/accommodations.html', context)


def accommodation(request, pk):
    acc = get_object_or_404(Accommodation, pk=pk)

    context = {
        'title': acc.name,
        'accommodation': acc,
    }
    return render(request, 'mainapp/accommodation_details.html', context)




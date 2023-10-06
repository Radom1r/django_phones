from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    phone_list = Phone.objects.all()
    sorting = request.GET.get('sort', 'name')
    if sorting == 'name':
        context = {'phones': sorted(phone_list, key=lambda phone: phone.name), 'sorting' : sorting}
    elif sorting == 'min_price':
        context = {'phones': sorted(phone_list, key=lambda phone: phone.price), 'sorting' : sorting}
    elif sorting == 'max_price':
        context = {'phones': sorted(phone_list, key=lambda phone: phone.price, reverse=True), 'sorting' : sorting}
    return render(request, template, context)


def show_product(request, phone_slug):
    template = 'product.html'
    phone_card = Phone.objects.get(slug=phone_slug)
    context = {'phone':phone_card}
    return render(request, template, context)

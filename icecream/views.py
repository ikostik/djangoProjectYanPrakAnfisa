# from django.http import HttpResponse
from django.shortcuts import render
from .models import icecream_db


# def icecream_list(request):
#     icecreams = ''
#     for i in range(len(icecream_db)):
#         icecreams += f"<a href='/icecream/{i}/'>{icecream_db[i]['name']}</a><br>"
#     context = {
#         'icecreams_': icecreams
#     }
#     return render(request, 'icecream/icecream-list.html', context)

# def icecream_list(request):
#     icecreams = ''
#     for name in range(len(icecream_db)):
#         icecreams += icecream_db[name]['name'] + '::'
#     return HttpResponse(f'Cписок сортов мороженого: {icecreams}')


def icecream_detail(request, pk):
    name_ = icecream_db[pk]['name']
    description_ = icecream_db[pk]['description']
    context = {
        'name': name_,
        'description': description_,
    }
    return render(request, "icecream/icecream-detail.html", context)

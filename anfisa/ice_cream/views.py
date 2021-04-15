from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def ice_cream_list(request):
    return HttpResponse('Список мороженого')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def ice_cream_detail(request, pk):
    return HttpResponse(f'Мороженое номер {pk}')

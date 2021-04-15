from django.http import HttpResponse


def index(request):
    return HttpResponse('Главная страница')


def icecream_list(request):
    return HttpResponse('Список мороженого')


# В урл мы ждем парметр, и нужно его прередать в функцию для использования
def icecream_detail(icecream_detail, pk):
    return HttpResponse(f'Мороженое с id {pk}')
св 
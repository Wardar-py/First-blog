from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.conf import settings
from pages.models import Pages
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def index(request):
    object_list = Pages.objects.all()
    paginator = Paginator(object_list, 3)
    name = request.GET.get('name')
    try:
        my_pages = paginator.page(name)
    except PageNotAnInteger:
        my_pages = paginator.page(1)
    except EmptyPage:
        my_pages = paginator.page(paginator.num_pages)

    context = {'name' : name, 'pages' : my_pages}
    return render(request,'index.html', context=context)

def page_detail(request, year, month, day, pages):
    pages = get_object_or_404(Pages, slug=pages, status='published',
                              published__year=year, publish__month=month,
                              published__day=day)
    return render(request, 'detail.html', context=pages)

def ded_moroz(request):
    my_list = [
        "Строка 1", "Строка 2", "Строка 3"
    ]
    my_articles = []
    my_articles.append({"title" : "Статья 1", "text" : "<b>Жирные слова</b> продолжение текста"})
    my_articles.append({"title": "Статья 2", "text": "Текста"})

    context = {"title": "название страницы", "list_of_strings" : my_list, "list_of_articles" : my_articles }
    return render(request, 'ded_moroz.html', context=context)

def my_404(request):
    render(request, '404.html')
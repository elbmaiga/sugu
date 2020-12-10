from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.db.models import Q
from django.db.models import Sum
from .models import *
from commands.models import *
from sugu.views import get_panner
# Create your views here.

def index(request):
    articles = Articles.objects.filter(available=True).order_by('-created_at')
    articles_promo = Articles.objects.filter(available=True, promo=True).order_by('-created_at')[:3]
    articles_star = Articles.objects.filter(available=True, star=True).order_by('-created_at')[:1]


    datas = {
        'articles': articles,
        'articles_2': articles,
        'articles_star': articles_star,
        'articles_promo': articles_promo,
    }
    return render(request, 'articles/index.html', datas)

def detail(request, article_slug):
    article = get_object_or_404(Articles, slug = article_slug)
    sql = """ SELECT `articles_images`.id, `articles_images`.image FROM `articles_images` 
                INNER JOIN `articles_articles_images` ON `articles_images`.id = `articles_articles_images`.images_id 
                INNER JOIN `articles_articles` ON `articles_articles`.id = `articles_articles_images`.articles_id
                WHERE `articles_articles`.id = {}  """.format(article.id)
    other_img = Images.objects.raw(sql)

    datas = {
        'article': article,
        'images': other_img,
    }
    return render(request, 'articles/detail.html', datas)

def search(request, params=""):

    params = request.GET['s']

    #results = Articles.objects.filter(Q(title__icontains=params) | Q(category__category__exact=params))
    results = Articles.objects.filter(title__icontains=params)

    data = {
        'articles': results
    }
    return render(request, 'articles/search.html', data)

def search_category(request, params=""):
    results = Articles.objects.filter(category__category__icontains=params)
    data = {
        'articles': results
    }
    return render(request, 'articles/search.html', data)


def add_panner(request, article_slug, quantity=1):
    user_cookies = request.COOKIES['sessionid']
    
    if request.method == 'POST':
        quantity = int(request.POST['quantity'])

    article = Articles.objects.get(slug=article_slug)
        
    try:
        article_on_panner = Articles_On_Panner.objects.create(articles=article, quantity=quantity)
    except:
        pass
    else:
        try:
            get_panner = Panner.objects.get(user_cookies=user_cookies)
        except:
            panner = Panner.objects.create(user_cookies=user_cookies)
            panner.articles.add(article_on_panner)
            panner.save()
        else:
            for a in get_panner.articles:
                return HttpResponse(a)
            # get_panner.articles.add(article_on_panner)
            # get_panner.save()
    
    return redirect("/")
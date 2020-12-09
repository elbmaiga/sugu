from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.http import HttpResponse
from django.db.models import Sum
from .models import *
from commands.models import *
from sugu.views import get_panner
# Create your views here.

def index(request):
    articles = Articles.objects.filter(available=True).order_by('-created_at')
    articles_promo = Articles.objects.filter(available=True, promo=True).order_by('-created_at')[:3]
    articles_star = Articles.objects.filter(available=True, star=True).order_by('-created_at')[:1]
    category = []

    datas = {
        'articles': articles,
        'articles_2': articles,
        'articles_star': articles_star,
        'articles_promo': articles_promo,
        'categories': category,
    }
    return render(request, 'articles/index.html', datas)

def detail(request, article_slug):
    article = get_object_or_404(Articles, slug = article_slug)
    sql = """ SELECT `articles_images`.id, `articles_images`.image FROM `articles_images` 
                INNER JOIN `articles_articles_images` ON `articles_images`.id = `articles_articles_images`.images_id 
                INNER JOIN `articles_articles` ON `articles_articles`.id = `articles_articles_images`.articles_id
                WHERE `articles_articles`.id = {}  """.format(article.id)
    other_img = Images.objects.raw(sql)

    sql2 = """SELECT `articles_category`.id, category FROM `articles_category` 
                INNER JOIN `articles_articles_category` ON `articles_category`.`id`=`articles_articles_category`.`category_id` 
                INNER JOIN `articles_articles` ON `articles_articles`.`id` = `articles_articles_category`.`articles_id`
                WHERE `articles_articles_category`.`articles_id` = {} """.format(article.id)
    categ = Category.objects.raw(sql2)

    sql3  = """ SELECT SUM(articles_articles.price) FROM commands_panner_articles
                                        INNER JOIN commands_panner ON commands_panner_articles.panner_id = commands_panner.id
                                        INNER JOIN commands_articles_on_panner ON commands_articles_on_panner.id = commands_panner_articles.articles_on_panner_id
                                        INNER JOIN articles_articles ON commands_articles_on_panner.articles_id = articles_articles.id
                                        WHERE commands_panner.user_cookies = {} """.format("ddd")

    datas = {
        'article': article,
        'images': other_img,
        'categories': categ,
        'h': get_panner(request, 'dd')
    }
    return render(request, 'articles/detail.html', datas)

def search(request, params=""):
    params = request.GET['s']
    results = Articles.objects.filter(category__category__icontains=params)
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
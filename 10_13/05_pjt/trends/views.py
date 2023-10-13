from django.shortcuts import render, redirect
from .models import Keyword, Trend
from bs4 import BeautifulSoup
from selenium import webdriver
# Create your views here.
def keyword(request):
    
    keys = Keyword.objects.all()
    if request.method == "POST":
        k = Keyword()
        k.name = request.POST.get("key")
        k.save()
        return redirect("trends:keyword")
    else:
        context = {
            'keys' : keys
        }
        return render(request, 'trends/keyword.html', context)


def keyword_detail(request, pk):
    key = Keyword.objects.get(pk=pk)
    key.delete()
    return redirect('trends:keyword')


def crawling(request):
    keyword = "python"
    url = f'https://www.google.com/search?q={keyword}'
    
    driver = webdriver.Chrome()
    driver.get(url)
    
    html = driver.page_source
    soup = BeautifulSoup(html, "html.parser")
    
    for nobr_tag in soup.find_all('nobr'):
        nobr_tag.decompose()

    result_stats = soup.select_one("div#result-stats")
    results = result_stats.text[7:]
    context = {
        'results' : results,
    }
    return render(request, 'trends/crawling.html', context)


def crawling_histogram(request):
    return render(request, 'trends/crawling_histogram.html')


def crawling_advanced(request):
    return render(request, 'trends/crawling_advanced.html')


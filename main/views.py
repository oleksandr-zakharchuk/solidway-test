from django.shortcuts import render
from .models import Articles


def index(request):
    news = Articles.objects.all()
    row_count = (len(news) // 2) + 1
    row_count_range = range(0, row_count)
    #news_range = [2] * row_count_range
    #news_range = range(1, len(news), 2)
    return render(request, 'main/index.html', {'news': news, 'row_count_range': row_count_range})

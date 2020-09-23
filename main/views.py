from django.shortcuts import render, redirect
from .models import MelonList
from .crawling import melon_crawling

# Create your views here.
def index(request):
    songs = MelonList.objects.all()
    return render(request, "index.html", {"songs": songs})


def crawling(request):
    melon_data_list = melon_crawling()  # 정의해놓은 함수로 크롤링 결과값 가져오기
    MelonList.objects.all().delete()  # 이전 오브젝트들 삭제
    for i in range(len(melon_data_list)):
        MelonList(
            rank=melon_data_list[i][0],
            name=melon_data_list[i][1],
            singer=melon_data_list[i][2],
            album=melon_data_list[i][3],
        ).save()
    return redirect("index")

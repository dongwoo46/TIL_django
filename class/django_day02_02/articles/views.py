from django.shortcuts import render

import random
import requests

# Create your views here.
def greeting(request):
    foods = ['pizza','chicken','noodles','라면','고기','타코']
    # foods = []

    return render(request, 'articles/greeting.html',{'foods':foods})


def index(request):
    return render(request, 'articles/index.html')

def lotto(request):
    # lotto 당첨번호 가져오기
    url = 'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo=1054'
    # 파이썬으로 요청해서 응답받기 (자세한 내용은 requests docs에서 참고) 
    res = requests.get(url)
    lotto_dict = res.json()

    bonus = lotto_dict['bnusNo']
    lotto=[]
    for i in range(1,7):
        lotto.append(lotto_dict[f'drwtNo{i}'])
    lotto = lotto+[bonus]
    win_rate = {
        "1등": 0,
        "2등": 0,
        "3등": 0,
        "4등": 0,
        "5등": 0,
        "꽝": 0,
    }                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
    lst = [x for x in range(1,45)]
    for i in range(1000):
        number = random.sample(lst,7)
        cnt = 0
        rank = ''
        
        for i in number:
            if i in lotto:
                cnt+=1
        if cnt == 3:
            win_rate['5등'] +=1 
        elif cnt == 4:
            win_rate['4등'] +=1
        elif cnt == 5:
            win_rate['3등'] +=1
        elif cnt == 6:
            win_rate['2등'] +=1
        elif cnt == 7:
            win_rate['1등'] +=1
        else:
            win_rate['꽝'] +=1
    


    context = {
        'number':number,
        'lotto':lotto,
        'cnt':cnt,
        'win_rate':win_rate,
    }
    # context대신 그냥 바로 3번째에  'number':number 넣어도됨
    return render(request, 'articles/lotto.html', context)


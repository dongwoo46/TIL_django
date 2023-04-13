from django.shortcuts import render

# Create your views here.
def calculator(request,num1,num2):
    add = num1 + num2
    mult = num1 * num2
    minus = num1 - num2
    if num2 == 0:
        ans = "계산할 수 없습니다."
    else:
        ans = num1 / num2

    context = {
        'num1':num1,
        'num2':num2,
        'add':add,
        'mult':mult,
        'minus':minus,
        'ans':ans
    }

    
    return render(request, 'calculators/calculator.html',context)
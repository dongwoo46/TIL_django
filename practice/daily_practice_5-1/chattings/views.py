from django.shortcuts import render,redirect
from .forms import ChatForm
from .models import Chat

# Create your views here.
def index(request):
    chats = Chat.objects.all()
    context = {'chats':chats}
    return render(request, 'chattings/index.html',context)

def create(request):
    if request.method == 'POST':
        # 새로운 게시글 생성
        form = ChatForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data.get('user')
            content = form.cleaned_data.get('content')
            chat = Chat(user=user, content=content)
            chat.save()
            return redirect('chattings:index', chat.pk)
    else:
        form = ChatForm()
        
    context = {'form':form}
    return render(request,'chattings/create.html',context)

def detail(request, pk):
    chat = Chat.objects.get(pk=pk)
    context = {'chat': chat}
    return render(request, 'chattings/detail.html', context)
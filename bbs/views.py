from django.shortcuts import render,redirect
from bbs.models import Board
# Create your views here.


def b_list(request):
    if request.user.is_authenticated:
        posts = Board.objects.all().order_by('-id')
        context={
            'post':posts
        }
        return render(request,'bbs/list.html',context)
    else:
        return redirect('home')



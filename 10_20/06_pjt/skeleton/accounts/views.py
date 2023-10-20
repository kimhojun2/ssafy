from django.shortcuts import render,redirect
from django.views.decorators.http import require_http_methods, require_POST
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm
from django.contrib.auth import get_user_model
from boards.models import Board, Comment
from django.contrib.auth.decorators import login_required
# Create your views here.


@ require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect("boards:index")
        
    if request.method =='POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            # 저장 및 자동 로그인
            user = form.save()
            auth_login(request, user)
            return redirect("boards:index")
            # form.save()
            # return redirect("boards:index")
    else:
        form = CustomUserCreationForm()
        
    context = {
        'form' : form,
    }
    return render(request, 'accounts/signup.html', context)


@ require_http_methods(['GET', 'POST'])
def login(request):
    if request.user.is_authenticated:
        return redirect("boards:index")
        
    if request.method =='POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect("boards:index")
            # form.save()
            # return redirect("boards:index")
    else:
        form = AuthenticationForm()
        
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)



# 세션 데이터를 삭제하네 -> POST요청
@require_POST
def logout(request):
    # 로그인 된 사용자만 로그아웃
    if request.user.is_authenticated:
        auth_logout(request)
    return redirect("boards:index")


def profile(request, user_pk):
    User = get_user_model()
    boards = Board.objects.filter(author_id = user_pk)
    comments = Comment.objects.filter(author_id = user_pk)
    person = User.objects.get(pk=user_pk)
    context = {
        'person' : person,
        'boards' : boards,
        'comments' : comments,
    }
    return render(request, 'accounts/profile.html', context)

@login_required
def follow(request, user_pk):
    User = get_user_model()
    you = User.objects.get(pk=user_pk)
    me = request.user
    
    if me in you.followers.all():
        you.followers.remove(me)
    else:
        you.followers.add(me)
        
    return redirect('accounts:profile', you.id)
    
        
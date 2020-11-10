from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from django.utils import timezone
from django.contrib.auth.decorators import login_required

# Create your views here.

def index(request):
    # HttpResponse로 text 데이터를 줌
    # return HttpResponse("HELLO SOHYEONG!")
    # 첫 번째 인자는 request
    # posts/index.html을 template으로 활용해서 응답
    # rendering 할 때 필요한 Data - dictionary
    # context = {
    #     # 'post': '나의 첫 #Django Project! :)',
    #     'post': {
    #         'author': 'sohyeong',
    #         'body': '샘플 게시물 테스트'
    #     },
    #     'numbers': [1, 5, 2, 3, 4],
    #     'number': 1,
    #     'list': [1, 2, 3]
    # }
    posts = Post.objects.all()
    context = { 'posts': posts }
    # 세 번째 인자: template에 전달할 변수
    return render(request, 'posts/index.html', context)

def detail(request, post_id):
    post = Post.objects.get(id=post_id)
    context = { 'post': post }
    return render(request, 'posts/detail.html', context)

@login_required
def new(request):
    # if not request.user.is_authenticated:   # 로그인을 하지 않았다면
    #     return redirect('accounts:login')

    return render(request, 'posts/new.html')

@login_required
def create(request):
    # if not request.user.is_authenticated:
    #     return redirect('accounts:login')
        
    # author = request.POST['author']
    user = request.user
    body = request.POST['body']

    image = None    # => null
    if 'image' in request.FILES:    # image라는 key가 있으면
        image = request.FILES['image']
        
    # post = Post(author=author, body=body, created_at=timezone.now())
    # post = Post(user=user, body=body, created_at=timezone.now())
    post = Post(user=user, body=body, image=image, created_at=timezone.now())
    post.save()

    return redirect('posts:detail', post_id=post.id)

@login_required
def edit(request, post_id):
    try:
        post = Post.objects.get(id=post_id, user=request.user)
    except Post.DoesNotExist:   # 게시물을 못 찾은 예외
        return redirect('posts:index')

    content = { 'post': post }
    return render(request, 'posts/edit.html', content)

@login_required
def update(request, post_id):
    try:
        post = Post.objects.get(id=post_id, user=request.user)
    except Post.DoesNotExist:
        return redirect('posts:index')

    # post.author = request.POST['author']
    post.body = request.POST['body']

    if 'image' in request.FILES:
        post.image = request.FILES['image']
        
    post.save()

    return redirect('posts:detail', post_id=post.id)

@login_required
def delete(request, post_id):
    try:
        post = Post.objects.get(id=post_id, user=request.user)
    except Post.DoesNotExist:
        return redirect('posts:index')

    post.delete()

    return redirect('posts:index')

@login_required
def like(request, post_id):
# post 방식 검증
    if request.method == 'POST':
        try:
            post = Post.objects.get(id=post_id)

            if request.user in post.liked_users.all():
                post.liked_users.remove(request.user)   # 중간 테이블 함수 사용
            else:
                post.liked_users.add(request.user)  # 중간 테이블 함수 사용

            return redirect('posts:detail', post_id=post.id)

        except Post.DoesNotExist:
            pass
# get 방식
    return redirect('posts:index')
from django.shortcuts import render, redirect
from django.views.generic.base import View
from .models import Post, Likes
from .form import CommentsForm
from django.urls import reverse

class PostView(View):
    #вывод записи
    def get(self, request):
        posts = Post.objects.all()
        return render(request, 'blog/blog.html', {'post_list':posts})


class PostDetail(View):
    #отдельная страница для записи
    def get(self, request, pk):
        post= Post.objects.get(id=pk)
        return render(request, 'blog/blog_details.html', {'post':post})
    

class AddComments(View):
    #добавление комментарий
    def post(self, request, pk):
        form = CommentsForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.post_id = pk
            form.save()
            return redirect(f'/{pk}')
        
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

class AddLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            Likes.objects.get(ip=ip_client, post_id = pk)
            return redirect(f'/{pk}')
        except:
            new_like = Likes()
            new_like.ip = ip_client
            new_like.post_id=int(pk)
            new_like.save()
            return redirect(f'/{pk}')
        
class DisLike(View):
    def get(self, request, pk):
        ip_client = get_client_ip(request)
        try:
            # Ищем лайк, который мы хотим удалить
            lik = Likes.objects.get(ip=ip_client, post_id=pk)
            lik.delete()
        except Likes.DoesNotExist:
            # Если лайка не существует, ничего не делаем
            pass
        return redirect(f'/{pk}')
        


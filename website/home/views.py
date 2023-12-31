from django.shortcuts import redirect, render
from django.contrib import messages
from .models import PostModel
from .models import SliderModel
from .models import AtolyeModel

def home (request):
    sliderImages = SliderModel.objects.all()
    return render(request,"index.html",{'slider': sliderImages , 'navbar': 'home'})

def bgIndex (request):
    atolye = AtolyeModel.objects.all()
    return render(request,"bg-index.html",{'atolye': atolye ,'navbar': 'bg-home'})

def about(request):
    return render(request,"about.html",{'navbar': 'about'})

def blog(request):
    posts = PostModel.objects.all() 
    return render(request,"blog/blog.html", {'posts': posts ,'navbar': 'blog'})

def admin_media_detail(request,pk):
    post = PostModel.objects.get(id=pk)
    return render(request, "blog/post-detail.html", {'post': post,'navbar': 'blog'})

def contact(request):
    return render(request,"contact.html",{'navbar': 'contact'})

def atolye_iletisim(request):
    return render(request,"bg-contact.html",{'navbar': 'atolye_iletisim'})



#### burada fotoğrafları teker teker açan html sayfaları üret pk mantığıyla (admin için yap bunu)
####



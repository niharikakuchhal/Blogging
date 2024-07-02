from django.shortcuts import render, redirect
from .form import *
from django.contrib.auth import logout, login, authenticate

def logout_view(request):
    logout(request)
    return redirect('/')

def home(request):
    context = {'blogs': BlogModel.objects.all()}
    return render(request, 'home.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('loginUsername')
        password = request.POST.get('loginPassword')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'login.html', {'error': 'Invalid email or password'})
    return render(request, 'login.html')
    

def blog_detail(request, slug):
    context = {}
    try:
        blog_obj = BlogModel.objects.filter(slug=slug).first()
        context['blog_obj'] = blog_obj
    except Exception as e:
        print(e)
    return render(request, 'blog_detail.html', context)

def see_blog(request):
    context = {}
    try:
        blog_objs = BlogModel.objects.filter(user = request.user)
        context['blog_objs'] = blog_objs
    except Exception as e:
        print(e)
    return render(request, 'see_blog.html', context)

def add_blog(request):
    context = {'form': BlogForm()}
    try:
        if request.method == 'POST':
            form = BlogForm(request.POST) 
            image = request.FILES['image']
            title = request.POST.get('title')
            user = request.user
           
            if form.is_valid():
               content = form.cleaned_data['content']
            BlogModel.objects.create(
               user = user, title=title,
               content = content, image = image
            )
            return redirect('see-blog')
            # return render(request, 'add_blog.html', context)

    except Exception as e:
        print(e)
    return render(request, 'add_blog.html', context)

def blog_delete(request, id):
    try:
        blog_obj = BlogModel.objects.get(id=id)

        if blog_obj.user == request.user:
            blog_obj.delete()

    except Exception as e:
        print(e)
    return redirect('see_blog')

def blog_update(request, slug):
    context = {}
    try:

        blog_obj = BlogModel.objects.get(slug = slug)
        
        if blog_obj.user != request.user:
            return redirect('/')
        
        # initial_dict = {'content':blog_obj.content}
        # form = BlogForm(initial=initial_dict)

        # if request.method == 'POST':
        #     form = BlogForm(request.POST) 
        #     image = request.FILES['image']
        #     title = request.POST.get('title')
        #     user = request.user
           
        #     if form.is_valid():
        #        content = form.cleaned_data['content']
        #        blog_obj = BlogModel.objects.create(
        #         user = user, title=title,
        #        content = content, image = image
        #        )

        if request.method == 'POST':
            form = BlogForm(request.POST, request.FILES, instance=blog_obj)
            if form.is_valid():
                form.save()
                return redirect('see_blog')
        else:
            form = BlogForm(instance=blog_obj)

        context['blog_obj'] = blog_obj
        context['form'] = form
    except Exception as e:
        print(e)
    
    return render(request, 'update_blog.html', context)

def register_view(request):
    return render(request, 'register.html')


def verify(request, token):
    try:
        profile_obj = Profile.objects.filter(token = token).first()

        if profile_obj:
            profile_obj.is_verified = True
            profile_obj.save()
        
        return redirect('/login/')
    
    except Exception as e:
        print(e)

    return redirect('/')
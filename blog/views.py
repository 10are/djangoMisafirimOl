from django.shortcuts import redirect, render

from blog.models import BlogModel

def index(request):
    blogs = BlogModel.objects.all()
    return render(request,'blog/index.html',{'blogs':blogs})


def createblog(request):
    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        blog = BlogModel(
            username= request.user,
            title=title,
            body=body
        )
        blog.save()
        return redirect("http://127.0.0.1:8000/myblog/")
    return render(request,'blog/form.html')

def myblog(request):
    blogs = BlogModel.objects.filter(username=request.user)
    return render(request,'blog/index.html',{'blogs':blogs})


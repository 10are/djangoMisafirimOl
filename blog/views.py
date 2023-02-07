from django.shortcuts import redirect, render
from blog.models import blog, City, District

def index(request):
    blogs = blog.objects.all()
    return render(request,'blog/index.html',{'blogs':blogs})


def createblog(request):
    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        city = request.POST.get('city')
        district = request.POST.get('district')
        blog = blog(
            username= request.user,
            title=title,
            body=body,
            city=City.objects.get(id=city),
            district=District.objects.get(id=district)

        )
        blog.save()
        return redirect("http://127.0.0.1:8000/myblog/")
    cities = City.objects.all()
    return render(request,'blog/form.html', {'cities': cities})

def myblog(request):
    blogs = blog.objects.filter(username=request.user)
    return render(request,'blog/index.html',{'blogs':blogs})

def city_blog(request, city_id):
    city = City.objects.get(id=city_id)
    blogs = blog.objects.filter(city=city)
    return render(request, 'blog/index.html', {'blogs': blogs})


def district_blogs(request, district_id):
    district = District.objects.get(id=district_id)
    blogs = blog.objects.filter(district=district)
    return render(request, 'blog/index.html', {'blogs': blogs})
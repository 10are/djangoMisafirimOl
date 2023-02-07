from django.shortcuts import redirect, render
from blog.models import blog as Blog, City, District

def index(request):
    blog = Blog.objects.all()
    return render(request,'blog/index.html',{'blogs':blog})


def createblog(request):
    cities = City.objects.all()
    districts = District.objects.none()

    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        city = request.POST.get('city')
        district = request.POST.get('district')
        blog = Blog.objects.all(
            username= request.user,
            title=title,
            body=body,
            city=City.objects.get(id=city),
            district=District.objects.get(id=district)

        )
        blog.save()
        return redirect("http://127.0.0.1:8000/myblog/")

    city_id = request.GET.get('city')
    if city_id:
        districts = District.objects.filter(city_id=city_id)

    return render(request,'blog/form.html', {'cities': cities, 'districts': districts})

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



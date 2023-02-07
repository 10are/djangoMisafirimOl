from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name='districts')
 
    def __str__(self):
        return self.name



class blog(models.Model):
    username = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    body = models.CharField(max_length=150)
    pub_date = models.DateTimeField(auto_now=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    district = models.ForeignKey(District, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.username + ' ' + self.title

    class Meta:
        ordering = ['-pub_date']

cities = [   
     "City 1", 
     "City 2",
     "City 3",
     "City 4",
     "City 5",
]

for city in cities:
    c, created = City.objects.get_or_create(name=city)
    if created:
        c.save()

districts = [
    ["District 1", "City 1"],
    ["District 2", "City 2"],
    ["District 3", "City 3"],
    ["District 4", "City 4"],
    ["District 5", "City 5"],
    ["District 6", "City 1"],
    ["District 7", "City 2"],
    ["District 8", "City 1"],
    ["District 9", "City 2"],
]

for district in districts:
    city = City.objects.get(name=district[1])
    District.objects.create(name=district[0], city=city)







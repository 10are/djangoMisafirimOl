from django.db import models

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name

class District(models.Model):
    name = models.CharField(max_length=100)
    city = models.ForeignKey(City, on_delete=models.CASCADE)

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
     "City a", 
     "City b",
     "City c",
     "City d",
     "City f",
]

for city in cities:
    c, created = City.objects.get_or_create(name=city)
    if created:
        c.save()

districts = [
    ["District a", "City a"],
    ["District a", "City a"],
    ["District a", "City b"],
    ["District a", "City b"],
    ["District b", "City c"],
    ["District b", "City d"],
    ["District c", "City d"],
    ["District c", "City d"],
    ["District d", "City d"],
]
for district in districts:
    city, created = City.objects.get_or_create(name=district[1])
    District.objects.create(name=district[0], city=city)





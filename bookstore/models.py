from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} {self.surname}"


class Store(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)

    def __str__(self):
        return f"{self.name} | {self.address}"


class Publisher(models.Model):
    name = models.CharField(max_length=100)
    year = models.IntegerField()
    store = models.OneToOneField(Store, primary_key=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    pages = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    publisher = models.ManyToManyField(Publisher)
    pubdate = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} | {self.price} | {self.author}"

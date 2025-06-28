from django.db import models
from django.utils.text import slugify
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to="categories/",default="default_category.png",blank=True)
    
    def __str__(self):
        return self.name
class Author(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100,null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    photo = models.ImageField(upload_to="authors/", default="default_author.png", blank=True)

    def get_absolute_url(self):
        return reverse("author_detail", kwargs={"slug": self.slug})
    def save(self):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save()
    def __str__(self):
        return self.name

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author,null=True,on_delete=models.SET_NULL)
    slug = models.SlugField(blank=True,null=True)
    description = models.TextField()
    image = models.ImageField(upload_to="books/")
    price = models.DecimalField(max_digits=10, decimal_places=2)
    pages = models.IntegerField()
    published_date = models.DateField()
    category = models.ForeignKey(Category,null=True,on_delete=models.SET_NULL)
    
    class Meta:
        unique_together = ("slug", "published_date")

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.slug})

    def save(self,*args,**kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

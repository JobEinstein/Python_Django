from django.db import models

# Create your models here.
# 登录用户类


class User(models.Model):
    """登录用户类"""
    name = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    def __str__(self):
        return str(self.name, self.password)


class Blog(models.Model):
    """docstring for Blog"""
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self, arg):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    def __str__(self):
        return self.name


class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):
        return self.headline

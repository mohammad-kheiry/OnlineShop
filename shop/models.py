from django.db import models

from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_number = models.IntegerField()
    
    def __str__(self):
        return self.user.username


class Brand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Color(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='products')
    color = models.ForeignKey(Color, on_delete=models.SET_NULL, null=True, blank=True)
    category = models.ForeignKey(ProductCategory,on_delete=models.CASCADE, related_name='products')

    def __str__(self):
        return self.name

class ProductComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    created_at = models.DateTimeField(auto_now_add=True)


class Cart(models.Model):
    customer = models.OneToOneField(Customer, on_delete=models.CASCADE, related_name='cart')
    products = models.ManyToManyField(Product, blank=True)


class BlogCategory(models.Model):
    name = models.CharField(max_length=10)

    def __str__(self):
        return self.name


class Blog(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blogs')
    category = models.ForeignKey(BlogCategory, on_delete=models.CASCADE, related_name='blogs')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class BlogComment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='comments')
    created_at = models.DateTimeField(auto_now_add=True)

class BlogTag(models.Model):
    name = models.CharField(max_length=100)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, related_name='tags')

    def __str__(self):
        return self.name


class BlogReview(models.Model):
    name = models.CharField(max_length=100)
    blog = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='reviews')

    def __str__(self):
        return self.name

from django.contrib import admin

from .models import (Customer, Brand, Color, ProductCategory, Product, 
                    ProductComment, Review, Cart, BlogCategory,  Blog, BlogComment,
                    BlogTag, BlogReview)




@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    pass

@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    pass

@admin.register(Color)
class CustomerAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductCategory)
class ProductCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductComment)
class ProductCommentAdmin(admin.ModelAdmin):
    pass

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    pass

@admin.register(Cart)
class CartAdmin(admin.ModelAdmin):
    pass

@admin.register(BlogCategory)
class BlogCategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    pass

@admin.register(BlogComment)
class BlogCommentAdmin(admin.ModelAdmin):
    pass

@admin.register(BlogTag)
class BlogTagAdmin(admin.ModelAdmin):
    pass

@admin.register(BlogReview)
class BlogReviewAdmin(admin.ModelAdmin):
    pass















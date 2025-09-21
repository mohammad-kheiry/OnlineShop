from audioop import avg
from django.shortcuts import get_objects_or_404, redirect
from django.urls import reverse
from django.views import generic, View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Avg

from .models import(
    Product, ProductComment, Review,
    Cart, Blog, BlogComment, Customer
)

from .forms import ProductCommentForm, ReviewForm, BlogCommentForm

# Products

class ProductListView(generic.ListView):
    model = Product
    template_name = 'products/products_list.html'
    context_object_name = 'products'


class ProductDetailView(generic.DetailView):
    model = Product
    template_name = 'products/products_detail.html'
    context_object_name = 'product'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        product = self.object
        ctx['avg_rating'] = product.reviews.aggregate(avg=Avg('rating'))['avg'] or 0
        ctx['comments'] = product.comments.select_related('user').all()
        ctx['reviews'] = product.reviews.select_related('user').all()
        ctx['comment_form'] = ProductCommentForm()
        ctx['review_form'] = ReviewForm()
        return ctx

# Add comment / review

class ProductCommentCreateView(LoginRequiredMixin, generic.FormView):
    form_class = ProductCommentForm

    def form_valid(self, form):
        product = get_objects_or_404(Product, pk=self.kwargs['pk'])
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.product = product
        comment.save()
        return redirect('product-detail', pk=product.pk)


class ReviewCreateView(LoginRequiredMixin, generic.FormView):
    form_class = ReviewForm

    def form_valid(self, form):
        product = get_objects_or_404(Product, pk=self.kwargs['pk'])
        review = form.save(commit=False)
        review.user = self.request.user
        review.product = product
        review.save()
        return redirect('product-detail', pk=product.pk)

# Cart views

def _get_or_create_cart_for_user(user):
    customer, _ = Customer.objects.get_or_create(user=user, defaults={'address': ''})
    cart, _ = Cart.objects.get_or_create(customer=customer)
    return cart

class CartDetailView(LoginRequiredMixin, generic.TemplateView):
    template_name = 'cart/cart_detail.html'

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        cart = _get_or_create_cart_for_user(self.request.user)
        ctx['cart'] = cart
        ctx['products'] = cart.products.all()
        ctx['total_price'] = sum(p.price for p in ctx['products'])
        return ctx

class AddToCartView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        product = get_objects_or_404(Product, pk=self.kwargs['product_pk'])
        cart = _get_or_create_cart_for_user(request.user)
        cart.products.add(product)
        return redirect('cart-detail')


from django import forms
from .models import ProductComment, Review, BlogComment

class ProductCommentForm(forms.ModelsForm):
    class Meta:
        model = ProductComment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Your opinion about the product...'})
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'content']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'content': forms.Textarea(attrs={'rows': 3, 'placeholder': 'Description'})
        }

class BlogCommentForm(forms.ModelForm):
    class Meta:
        model = BlogComment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={'rows': 4, 'placeholder': 'Your opinion'})
        }


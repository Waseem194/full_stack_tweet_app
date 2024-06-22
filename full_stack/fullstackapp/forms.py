from django import forms
from .models import Tweet 

class TweetForm(forms.ModelForm):
    
    class Meta:
        model = Tweet
        fields = ["text","photo"]
        
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'})
    
    photo = forms.ImageField(
        widget=forms.ClearableFileInput(attrs={'class': 'form-control'})
    )

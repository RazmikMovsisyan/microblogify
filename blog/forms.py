from django import forms
from .models import Comment
from .models import Post
from allauth.account.forms import SignupForm

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'rows': 3,
                'maxlength': '1000',
                'placeholder': 'Leave a comment...',
            }),
        }

    
    # Set Limit on input
    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) > 1000:
            raise forms.ValidationError("Comment must be 1000 characters or fewer.")
        return content

# Sign up Form with first and last name

from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(
        max_length=30,
        label='First Name',
        widget=forms.TextInput(attrs={'placeholder': 'First Name'})
    )
    last_name = forms.CharField(
        max_length=30,
        label='Last Name',
        widget=forms.TextInput(attrs={'placeholder': 'Last Name'})
    )

    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

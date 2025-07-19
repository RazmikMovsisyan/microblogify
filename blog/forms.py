from django import forms
from allauth.account.forms import SignupForm

from .models import Comment, Post


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

    def clean_content(self):
        """
        Validates that the comment content does not exceed 1000 characters.
        """
        content = self.cleaned_data['content']
        if len(content) > 1000:
            raise forms.ValidationError(
                "Comment must be 1000 characters or fewer."
            )
        return content


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
        """
        Saves the first and last name on user creation.
        """
        user = super().save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

from django import forms
from .models import Comment

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
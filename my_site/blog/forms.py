from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        #fields = ["user_name", "user_email", "text"]
        #or do the exclude
        exclude = ["post"]
        labels = {
            "user_email" : "User Email",
            "user_name" : "Your Name",
            "text": "Your Comment"
        }



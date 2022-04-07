from .models import Projects, Votes, Comments
from django import forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['user','design','usability','content']


class RateForm(forms.ModelForm):
    class Meta:
        model = Votes
        exclude = ['user','project']  


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        exclude = ['user','pro_id']        



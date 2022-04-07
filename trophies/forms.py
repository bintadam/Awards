from .models import Projects

class PostForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['user','design','usability','content']


class RateForm(forms.ModelForm):
    class Meta:
        model = Votes
        exclude = ['user','project']        
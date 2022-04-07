from .models import Projects

class PostForm(forms.ModelForm):
    class Meta:
        model = Projects
        exclude = ['user','design','usability','content']
from django import forms
from photo.models import Album


class AlbumModelForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('title', 'description', )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }

from django import forms
from .models import Album


class AlbumModelForm(forms.ModelForm):
    class Meta:
        model = Album
        fields = ('title', 'description', )

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.TextInput(attrs={'class': 'form-control'}),
        }


class PhotoForm(forms.Form):
    title = forms.CharField(
        max_length=30,
        widget=forms.TextInput(
            attrs={'class': 'form-control',}
        )
    )
    description = forms.CharField(
        max_length=80,
        widget=forms.TextInput(
            attrs={'class': 'form-control',}
        )
    )
    img = forms.ImageField(
        widget=forms.FileInput()
    )


from django import forms


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
from django import forms
class Subscribe(forms.Form):
    Name = forms.CharField(widget=forms.TextInput(attrs={ 'placeholder':'Your name*'}))
    Email = forms.EmailField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Your Email*'}))
    Message = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Your Message*'}))
    def __str__(self):
        return self.Email
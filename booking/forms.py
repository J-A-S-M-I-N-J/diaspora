from django import forms


class Booking(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    message = forms.CharField(widget=forms.Textarea(), label='Message', max_length=1000)

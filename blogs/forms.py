from django import forms

class postform(forms.Form):
    heading = forms.CharField()
    image = forms.ImageField(required=False)
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'text', 'rows':'2','cols':'60', 'placeholder':'Write here ...'}))
    
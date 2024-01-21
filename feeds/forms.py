from django import forms

class postform(forms.Form):
    text = forms.CharField(
        widget=forms.Textarea(attrs=
                {'class':'text', 
                'rows':'2',
                'cols':'60', 
                'placeholder':'Write here ...',
                'name': 'text'}))
    image = forms.ImageField(required=False,)
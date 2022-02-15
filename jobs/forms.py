from django import forms

class EmailJobForm(forms.Form):
    name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'class':'height60', 'placeholder': 'First Name'}))
    # email = forms.EmailField()
    to = forms.EmailField(widget=forms.TextInput(attrs={'class':'height60', 'placeholder':'sample@email.com'}))
    comments = forms.CharField(required=False, widget=forms.Textarea(attrs={'class':'textarea-height'}))


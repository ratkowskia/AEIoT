from django import forms


class AlgorithmDetailsForm(forms.Form):
    name = forms.CharField(max_length=100)
    semantics = forms.CharField(max_length=100)
    source_code = forms.CharField(widget=forms.Textarea)
    version = forms.EmailField()

class ProfileForm(forms.Form):
    username = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()

    def save(self):
        return

from django import forms


class AlgorithmDetailsForm(forms.Form):
    name = forms.CharField(max_length=100)
    semantics = forms.CharField(max_length=100)
    source_code = forms.CharField(widget=forms.Textarea)
    version = forms.EmailField()

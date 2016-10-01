from django import forms
from .models import Supplier, Consumer

class AlgorithmDetailsForm(forms.Form):
    name = forms.CharField(max_length=100)
    semantics = forms.CharField(max_length=100)
    source_code = forms.CharField(widget=forms.Textarea)
    version = forms.EmailField()



class ProfileForm(forms.Form):
    username = forms.CharField(max_length=100)
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    as_supplier = forms.ModelChoiceField(queryset=Supplier.objects.all(), required=False)
    as_consumer = forms.ModelChoiceField(queryset=Consumer.objects.all(), required=False)


    def save(self):
        return



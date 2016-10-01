# Copyright 2015 Google Inc. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django.http import HttpResponse
from .models import Choice, Question, Algorithm, Supplier
from .forms import AlgorithmDetailsForm, ProfileForm
from django.shortcuts import render,get_object_or_404
from django.http import Http404, HttpResponseRedirect
# need to upgrade django to 1.10, workaround instead of upgrade
#  http://stackoverflow.com/questions/38940996/importerror-no-module-named-urls-while-following-django-tutorial
from django.core.urlresolvers import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
#from django.contrib.auth.models import User
#from django.views.generic.list import ListView







class AlgorithmUpdate(generic.UpdateView):
    template_name = 'aeiot/alg_detail.html'
    model = Algorithm

    fields = ['name', 'semantics', 'source_code', 'version', 'supplier', 'input_format', 'output_format']

class AlgorithmCreate(generic.CreateView):
    template_name = 'aeiot/alg_detail.html'
    model = Algorithm

    fields = ['name', 'semantics', 'source_code', 'version', 'supplier', 'input_format', 'output_format']

class AlgorithmDelete(generic.DeleteView):
    model = Algorithm
    success_url = reverse_lazy('aeiot:index')

class AlgorithmsView(generic.ListView):

    model = Algorithm
    template_name='aeiot/alg_list.html'


    def get_context_data(self, **kwargs):
        context = super(AlgorithmsView, self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context

class ProfileUpdate(generic.FormView):
    template_name = 'aeiot/profile.html'
    form_class = ProfileForm
    success_url = reverse_lazy('aeiot:profile-update')
    #model = User
    #fields = ['username', 'first_name', 'last_name', 'email', 'company_name']

    '''def get_object(self, queryset=None):
        obj = User.objects.get(username=self.request.user)
        return obj'''

    '''def get_context_data(self, **kwargs):
        context = super(ProfileUpdate, self).get_context_data(**kwargs)
        context['form'].base_fields['login'].initial = "test"
        form = self.get_form(self.get_form_class())
        form.data['login']="AR"

        return context '''
    def get_initial(self):
        user = User.objects.get(username=self.request.user)
        self.initial['username'] = user.username
        self.initial['first_name'] = user.first_name
        self.initial['last_name'] = user.last_name
        self.initial['email'] = user.email
        try:
            self.initial['as_supplier'] = Supplier.objects.get(user_id=user.pk)
        except ObjectDoesNotExist:
            self.initial['as_supplier'] = None
        return self.initial


    def form_valid(self, form):
        #form.data
        user = User.objects.get(username=self.request.user)
        user.username = self.request.POST["username"]
        user.first_name = self.request.POST["first_name"]
        user.last_name = self.request.POST["last_name"]
        user.email = self.request.POST["email"]
        supplier_id = self.request.POST["as_supplier"]
        try:
            supplier = Supplier.objects.get(user_id=user)
            supplier.user_id=None
            supplier.save()
        except ObjectDoesNotExist:
            supplier_id = supplier_id

        if supplier_id != "":

            supplier=Supplier.objects.get(pk=int(supplier_id))
            supplier.user_id=user
            supplier.save()
        user.save()

        form.save()
        return super(ProfileUpdate, self).form_valid(form)

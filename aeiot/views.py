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
from .models import Choice, Question, Algorithm
from django.shortcuts import render,get_object_or_404
from django.http import Http404, HttpResponseRedirect
# need to upgrade django to 1.10, workaround instead of upgrade
#  http://stackoverflow.com/questions/38940996/importerror-no-module-named-urls-while-following-django-tutorial
from django.core.urlresolvers import reverse
from django.views import generic
#from django.views.generic.list import ListView






class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by('-pub_date')[:5]

class AlgorithmDetailView(generic.UpdateView):
    template_name = 'aeiot/alg_detail.html'
    model = Algorithm
    fields = ['name', 'semantics', 'source_code', 'version']


class AlgorithmsView(generic.ListView):

    model = Algorithm
    template_name='aeiot/alg_list.html'

    def get_context_data(self, **kwargs):
        context = super(AlgorithmsView, self).get_context_data(**kwargs)
        #context['now'] = timezone.now()
        return context

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'



def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('aeiot:results', args=(question.id,)))
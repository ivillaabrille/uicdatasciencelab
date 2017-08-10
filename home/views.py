from django.views import generic
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from .models import NewsAndUpdate, Message
from django.views import generic
from django.views.generic import View
from .forms import MessageForm
from django.core.urlresolvers import reverse

def IndexView(request):
    template = 'home/index.html'
    neu = NewsAndUpdate.objects.filter(NU_Category='News') | NewsAndUpdate.objects.filter(NU_Category='Event') | NewsAndUpdate.objects.filter(NU_Category='Update').order_by('-NU_Posted', '-id')
    pa = NewsAndUpdate.objects.filter(NU_Category='Project') | NewsAndUpdate.objects.filter(NU_Category='Article').order_by('-NU_Posted', '-id')
    context = {'n': neu, 'p': pa}
    return render(request, template, context)
'''
    nfilter={
        '{0}__{1}'.format('NU_Category', 'iexact'): 'news',
    }
    news = NewsAndUpdate.objects.filter(**nfilter).order_by('-NU_Posted', '-id')[:1]
    efilter={
        '{0}__{1}'.format('NU_Category', 'iexact'): 'event',
    }
    event = NewsAndUpdate.objects.filter(**efilter).order_by('-NU_Posted', '-id')[:1]
    ufilter={
        '{0}__{1}'.format('NU_Category', 'iexact'): 'update',
    }
    update = NewsAndUpdate.objects.filter(**ufilter).order_by('-NU_Posted', '-id')[:1]
    pfilter={
        '{0}__{1}'.format('NU_Category', 'iexact'): 'project',
    }
    project = NewsAndUpdate.objects.filter(**pfilter).order_by('-NU_Posted', '-id')[:1]
    afilter={
        '{0}__{1}'.format('NU_Category', 'iexact'): 'article',
    }
    article = NewsAndUpdate.objects.filter(**afilter).order_by('-NU_Posted', '-id')[:1]
    context = {'n': news, 'e': event, 'u': update, 'p': project, 'a': article}
    return render(request, template, context)
'''


class NewsView(generic.ListView):
    template_name = 'home/news.html'
    context_object_name = 'all_newsandupdate'

    def get_queryset(self):
        combined_queryset = NewsAndUpdate.objects.filter(NU_Category='News') | NewsAndUpdate.objects.filter(NU_Category='Event') | NewsAndUpdate.objects.filter(NU_Category='Update')
        return combined_queryset.order_by('-NU_Posted', '-id')

class NewsDetailView(generic.DetailView):
    model = NewsAndUpdate
    template_name = 'home/newsdetail.html'

class ResearchView(generic.ListView):
    template_name = 'home/research.html'
    context_object_name = 'research'

    def get_queryset(self):
        combined_queryset = NewsAndUpdate.objects.filter(NU_Category='Project') | NewsAndUpdate.objects.filter(NU_Category='Article')
        return combined_queryset.order_by('-NU_Posted', '-id')

class ResearchDetailView(generic.DetailView):
    model = NewsAndUpdate
    template_name = 'home/researchdetail.html'

def ConnectView(request):
    if request.method == 'POST':
        form = MessageForm(data=request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.save()
            return HttpResponseRedirect(reverse('home:success'))
    else:
        form = MessageForm()

    context = {'form': form}
    return render(request, 'home/connect.html', context)

def TeamView(request):
    return render(request, 'home/team.html')

def SuccessView(request):
    return render(request, 'home/success.html')

'''
class IndexView(generic.ListView):
    template_name = 'home/index.html'
    context_object_name = 'all_newsandupdate'

    def get_queryset(self):
        nufilter = {
            '{0}__{1}'.format('NU_Category', 'iexact'): 'project',
        }
        return NewsAndUpdate.objects.exclude(**nufilter).order_by('-NU_Posted', '-id')

    def get_context_data(self, *args, **kwargs):
        context = super(IndexView, self).get_context_data(*args, **kwargs)

        pfilter = {
            '{0}__{1}'.format('NU_Category', 'iexact'): 'project',
        }
        context['project'] = NewsAndUpdate.objects.filter(**pfilter).order_by('-NU_Posted', '-id')
        return context
'''

'''
class ConnectView(generic.ListView):
    template_name = 'home/connect.html'
    context_object_name = 'all_newsandupdate'

    def get_queryset(self):
        return NewsAndUpdate.objects.all().order_by('id')
'''
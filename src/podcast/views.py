# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from podcast.models import PodCast

def pod(request):

    podcast = PodCast.objects.all().order_by('-dat_publicacao')
  
    return render_to_response('pod.html', locals(), context_instance=RequestContext(request))

# Create your views here.

# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext
from dirigente.models import Dirigente

def dirigente(request):

    dirigentes = Dirigente.objects.all()
  
    return render_to_response('dirigente.html', locals(), context_instance=RequestContext(request))

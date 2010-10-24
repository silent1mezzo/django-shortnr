import base64
from django.template.context import RequestContext
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.sites.models import Site
from models import ShortenedUrl
from forms import ShortenerForm

def shorten_url(request, template_name='shortnr/index.html', reverse_url='shorten_url'):    
    context = RequestContext(request)
    dict = {}
    if request.POST:
        form = ShortenerForm(request.POST)
        if form.is_valid():
            try:
                url = ShortenedUrl.objects.get(url=form.cleaned_data['url'])
                if (url.user is None and request.user.is_authenticated() == False) or (url.user == request.user): 
                    dict['shortened_url'] = url.short_url
                    dict['form'] = ShortenerForm()
                    return render_to_response(
                        template_name,
                        dict,
                        context,
                    )
                        
            except:
                print form.cleaned_data['url']
            url = form.save(commit=False)
            if request.user.is_authenticated():
                url.user = request.user
                reverse_url = 'manage_urls'
            url.save()
            url.shorten_url()
            
            dict['shortened_url'] = url.short_url
            dict['form'] = ShortenerForm()
            return render_to_response(
                template_name,
                dict,
                context,
            )
    else:
        form = ShortenerForm()
    
    dict['form'] = form
    
    return render_to_response(
        template_name,
        dict,
        context,
    )
   
 
def manage_urls(request, template_name='shortnr/manage.html'):
    context = RequestContext(request)
    dict = {}    
    
    dict['urls'] = ShortenedUrl.objects.filter(user=request.user)
    
    return render_to_response(
        template_name,
        dict,
        context,
    )
    
def view_url(request, url):
    context = RequestContext(request)
    dict = {}
    url = settings.SHORTEN_LINK_URL + url
    
    url = ShortenedUrl.objects.get(short_url=url)
    url.clicks = url.clicks + 1
    url.save()
    
    return HttpResponseRedirect(url.url)
    

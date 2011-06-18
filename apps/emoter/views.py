from django.shortcuts import render_to_response

from models import Tweet

def index(request):
    tweets = Tweet.objects.all().order_by('-pk')
    return render_to_response("emoter/index.html", {"tweets": tweets})
    
    

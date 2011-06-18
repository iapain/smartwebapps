from django.shortcuts import render_to_response

from models import Cluster, News

def index(request):
    clusters = Cluster.objects.all().order_by('-created')
    return render_to_response("news/index.html", {"clusters": clusters})
    
    
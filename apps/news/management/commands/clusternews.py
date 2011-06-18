from optparse import make_option
from django.core.management.base import BaseCommand, CommandError

from apps.news.models import News, Cluster
from apps.ai.clustering import Cluster as Clustering

class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--iteration',
            '-i',
            dest='iteration',
            default=10,
            help='Specify number of interations'),
        )
    help = 'Cluster news items'

    def handle(self, *args, **options):
        items = News.objects.all()[:1000]
        cluster = Clustering(items)
        for i in xrange(options.get('iteration')):
            print "Iteration %d ..." % i
            ret = cluster.kmeans()
            for item in ret:
                if len(item) > 1:
                    for i in item:
                        if not i.cluster is None:
                            for b in item:
                                if b.cluster is None:
                                    b.cluster = i.cluster
                                    b.save()
                            continue
                    if item[0].cluster is None:   
                        c = Cluster()
                        c.save()
                        for i in item:
                            if i.cluster is None:
                                i.cluster = c
                                i.save()
        

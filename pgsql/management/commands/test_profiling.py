# -*- coding: utf-8 -*-
from django.test.client import Client

from optparse import make_option

from django.core.management.base import BaseCommand

from django.utils.text import slugify
import cProfile
import datetime
import time

"""
This management command should work a little like a test or a shell,
allowing to test requests launched against a profiling server or using a
profiled test client, but running against a chosen database - not a test one.
"""


class Command(BaseCommand):
    help = 'Launches some queries'
    args = ''
    option_list = BaseCommand.option_list + (
        make_option(
            '--all',
            action='store_true',
            dest='all',
            default=False,
            help='Run all'),
        make_option(
            '--dest',
            action='store',
            dest='dest',
            default='profiling',
            help='Run all'),
        )

    def handle(self, *args, **options):
        # disable johnny cache
        try:
            from johnny.cache import disable
            disable()
        except:
            pass

        c = Client()

        collection_id = options.get('collection') or 2003
        if collection_id or options.get('all', False):

            urls = [
                u'/main/ping/',
            ]


#            cProfile.run(c.get(url))
            for url in urls:
                start = time.time()
                print "Test url: \n\t{}".format(url)
                cProfile.runctx("c.get('{}')".format(url), globals(), locals(), filename="{}/{}_{}.prof".format(options.get('dest'), slugify(url), start))
#        >>> response = c.get(url)
#        >>> response = c.post('/login/', {'username': 'john', 'password': 'smith'})
#        >>> response.status_code



        print "All done"


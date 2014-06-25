from django.test import TestCase
from models import JSONModel, JSONCharModel, CharModel
from profilehooks import profile
from profilehooks import timecall
from profilehooks import coverage
import time
import json

def timeit(method):

    def timed(*args, **kw):
        ts = time.time()
        result = method(*args, **kw)
        te = time.time()

        print '%r (%r, %r) %2.2f sec' % \
              (method.__name__, args, kw, te-ts)
        return result

    return timed


json_object = {'a':'stefano', 'b': {'c':'alberto', 'd': 128}}
json_object2 = {'a':'alberto', 'b': {'c':'stefano', 'd': 128}}

json_dump = json.dumps(json_object)
json_dump2 = json.dumps(json_object2)

ITERATIONS = 10000

class JSONTestCase(TestCase):
    def setUp(self):
#        Model.objects.create(fields=)
        pass

    @profile
#    @timeit
    def test_create_json(self):
        for i in range(ITERATIONS):
            instance = JSONModel(json=json_object)
            instance.save()

    @profile
#    @timeit
    def test_update_json(self):
        for i in range(ITERATIONS):
            JSONModel.objects.all().update(json=json_object2)

    @profile
#    @timeit
    def test_create_char(self):
        for i in range(ITERATIONS):
            instance = CharModel(json=json.dumps(json_object))
#            instance = CharModel(json=json_dump)
            instance.save()


    @profile
#    @timeit
    def test_update_char(self):
        for i in range(ITERATIONS):
            CharModel.objects.all().update(json=json.dumps(json_object2))
#            CharModel.objects.all().update(json=json_dump2)

    @profile
#    @timeit
    def test_create_jsonchar(self):
        for i in range(ITERATIONS):
            instance = JSONCharModel(json=json_object)
            instance.save()


    @profile
#    @timeit
    def test_update_jsonchar(self):
        for i in range(ITERATIONS):
            JSONCharModel.objects.all().update(json=json_object2)

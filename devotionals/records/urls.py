from django.conf.urls.defaults import *
from models import Record

#~ this should have a single url providing a date and recovery the matching records. 

urlpatterns = patterns('records.views',
    (r'^import/$', 'import_csv', {}, 'records_import'),
    (r'^words/$', 'count_words', {}, 'count_words'),
    (r'^recovery/(?P<year>\d+)/(?P<month>\d+)/(?P<day>\d+)/$', 'recovery_list', {}, 'recovery_list'),
)

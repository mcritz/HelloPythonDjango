from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^$', views.poll_index, name='Poll Index'),
	# ex: /polls/5/
	url(r'^(?P<question_id>[0-9]+)/$', views.poll_detail, name='Poll Detail'),
	# ex: /polls/5/results/
	url(r'^(?P<question_id>[0-9]+)/result[s]?/$', views.poll_result, name='results'),
	# ex: /polls/5/vote/
	url(r'^(?P<question_id>[0-9]+)/vote[s]?/$', views.poll_vote, name='vote'),
]
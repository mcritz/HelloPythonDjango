from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

from .models import Question

def poll_index(request) :
	recent_questions = Question.objects.order_by('-pub_date')[:5]
	template = loader.get_template('poll_list.html')
	context = RequestContext(request, {
		'recent_questions': recent_questions,
	})
	return HttpResponse(template.render(context))

def poll_detail(request, question_id) :
	response = "Poll %s"
	return HttpResponse(response % question_id)

def poll_result(request, question_id) :
	response = "%s: Results"
	return HttpResponse(response % question_id)

def poll_vote(request, question_id) :
	response = "%s: Vote"
	return HttpResponse(response % question_id)

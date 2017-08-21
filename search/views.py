from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse

from search.models import SearchSocialMedia
from django.views.generic import TemplateView
from django.urls import reverse

import django_tables2 as tables
from django.utils.safestring import mark_safe



def jobs(request):
    current_user = request.user.id
    ssms = SearchSocialMedia.objects.filter(user_id_id=current_user)

    for ssm in ssms:
        ssm.id = "<a href='search/results/{0}/'>{0}</a>".format(ssm.id)
        ssm = mark_safe(ssm);

    return render(request, 'pages/view_saved_searches.html', {'jobs': ssms},autoescape=False)
    #
    # html =
    # for ssm in ssms:
    #
    #
    # return render(request, 'your_template.html', {'h': h, 'var1': var1})
    #
    #
    # page = TemplateView.as_view(template_name='pages/search.html')
    # return render(request, 'polls/results.html', {'error': "Submission Submitted"})


def results(request, question_id):
    page = TemplateView.as_view(template_name='pages/search.html')
    return render(request, 'polls/results.html', {'error': "Submission Submitted"})

def submit(request):
    title = request.GET.get('title')
    keywords = request.GET.get('keywords')
    sites = request.GET.getlist('sites')
    current_user =  request.user.id

    str_sites = '\t'.join([str(x) for x in sites])




    if request.method == 'GET':
        ssm = SearchSocialMedia()
        ssm.title = title
        ssm.keywords = keywords
        ssm.sites = sites
        ssm.user_id_id = current_user
        #TODO VALIDATE
        ssm.save()

        return HttpResponse("THIS IS A GET REQUEST" + title+keywords+str_sites )


    if request.method == 'POST':
        return HttpResponse("THIS IS  POST REQUEST" + request.POST)
    return HttpResponse("THIS IS NOT POST REQUEST")

          #SearchSocialMedia

          # Always return an HttpResponseRedirect after successfully dealing
          # with POST data. This prevents data from being posted twice if a
          # user hits the Back button.
          #return HttpResponseRedirect(TemplateView.as_view(template_name='pages/search.html',args='HELLO'))


#Gotta submit the form
#Gotta give a message upon submission
#Gotta create a page wherey ou can see you submissiosn
#Gotta cerate a page wherea you an see the results of a job

#Job results page = save by tweet ID for tweets

#Job results page = save by reddit ID for reddit

#Create a celery task runner to run and update the database





#!/Users/sadkhin2/workspace/python/job/dj/bin/python

from django_extensions.management.jobs import BaseJob,HourlyJob
from search import models
import datetime
import json
import urllib.request
import requests




class Job(HourlyJob):
    """
    Loads jobs from SearchSocialMediaJobs
    Checks to see if job frequency has changed and updates the corresponding jobs in  SearchSocialMediaJobs
    #TODO Checks to see if sites wanted has changed
    #TODO Checks to see if keywords have changed
    """
    help = "Loads jobs from SSM for running against API"


    def add_job(self,ssm):
        #Add a job for each user submitted site
        for site in ssm.sites:
            ssmj = models.SearchSocialMediaJob()
            ssmj.searchjobs_id_id = ssm.id
            ssmj.keywords = ssm.keywords
            ssmj.site = site
            ssmj.frequency = ssm.frequency
            print ("Saving site",ssmj)
            ssmj.save()

    def update_job(self,ssm_id,ssm_freq,ssm_site=None,ssm_keywords=None):
        ssmjs = models.SearchSocialMediaJob.objects.filter(searchjobs_id_id=ssm_id)
        for ssmj in ssmjs:
            if ssmj.frequency != ssm_freq:
                ssmj.frequency = ssm_freq
                ssmj.save()

    

    def run_job(self,ssm):
        ssmjs = models.SearchSocialMediaJob.objects.filter(searchjobs_id_id=ssm.id)
        for ssmj in ssmjs:
            #last_run = ssmj.last_run
            #timeNow = datetime.datetime.now()
            #FMT = '%H:%M:%S'
            #tdelta = datetime.strptime(s2, FMT) - datetime.strptime(s1, FMT)
            #if tdelta > 5
            query = ssm.keywords
            request_url = "http://127.0.0.1:8000/twitter/?query="+query

            r = requests.get(request_url)
            data =  r.json() 
            print (data)

            id = ssmj.id
            ssmjr = models.SearchSocialMediaJobResult()
            #existing_json = ssmjr.results
            #existing_json += results
            ssmjr.searchsocialmediajob_id_id = id
            ssmjr.results = data
            ssmjr.save()



            
    def execute(self):
        # Get all jobs
        ssms = models.SearchSocialMedia.objects.all()
        ssmj_ids = models.SearchSocialMediaJob.objects.values_list('searchjobs_id_id',flat=True)    

        #Set default frequency
        for ssm in ssms:
            if not ssm.frequency or ssm.frequency =='unset':
                ssm.frequency='5m'
            #If it doesn't exist, create it
            if ssm.id not in ssmj_ids:
                self.add_job(ssm)
            #Update the frequency of the ssmj, in case the admins changed it
            self.update_job(ssm.id,ssm.frequency)
            self.run_job(ssm)
            
    



            #Change frequency in SearchSocialMediaJobs
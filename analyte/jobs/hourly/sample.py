from django_extensions.management.jobs import BaseJob,HourlyJob
from search import models





class Job(HourlyJob):
    """
    Loads jobs from SearchSocialMediaJobs
    Checks to see if job frequency has changed and updates the corresponding jobs in  SearchSocialMediaJobs
    #TODO Checks to see if sites wanted has changed
    #TODO Checks to see if keywords have changed
    """
    help = "My sample job."


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
        ssmj = models.SearchSocialMediaJob.objects.filter(searchjobs_id_id=ssm_id)
        if ssmj.frequency != ssm_freq:
            ssmj.frequency = ssm_freq
            ssmj.save()

            
    def execute(self):
        # Get all jobs
        ssms = models.SearchSocialMedia.objects.all()
        ssmj_ids = models.SearchSocialMediaJob.objects.values_list('searchjobs_id_id',flat=True)    

        #Set default frequency
        for ssm in ssms:
            if not ssm.frequency or ssm.frequency =='unset':
                ssm.frequency='hourly'
            #If it doesn't exist, create it
            if ssm.id not in ssmj_ids:
                self.add_job(ssm)
            #Update the frequency of the ssmj, in case the admins changed it
            self.update_job(ssm.id,ssm.frequency)
            




            #Change frequency in SearchSocialMediaJobs
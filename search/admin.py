from django.contrib import admin

# Register your models here.
#
from .models import SearchSocialMedia,SearchSocialMediaJob,SearchSocialMediaJobResult
admin.site.register(SearchSocialMedia)
admin.site.register(SearchSocialMediaJob)
admin.site.register(SearchSocialMediaJobResult)


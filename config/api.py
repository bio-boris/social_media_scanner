from django.http import HttpResponse,JsonResponse



def getSearches(query,default_count=3):
    import twitter

    key = 'HxC75XpsCm7ZASuxlROfneTP8'
    secret = 'ps108XgQ8fKl1o1SP0ATFN9WqXXFyaD8SjJn6e0Gy08pp2otOi'
    token = '364418406-qukuwMb8INFBu6O5B4n6NADa7v771O0ERu2Y9xaq'
    token_secret = 'xmgtzf0LW73c4n35CUfw7SUK2xy3aJ18DxlMqb7iYDzRN'

    api = twitter.Api(consumer_key=key,
                      consumer_secret=secret,
                      access_token_key=token,
                      access_token_secret=token_secret)
    searches = api.GetSearch(term=query, raw_query=None, geocode=None, since_id=None,
                             max_id=None, until=None, since=None, count=default_count, lang=None, locale=None,
                             result_type='mixed', include_entities=None)

    json_searches = []
    for search in searches:
        json_searches.append(search.AsJsonString())

    return json_searches




def twitter(request):
    query = request.GET.get('query');
    if query:
        return JsonResponse(getSearches(query),safe=False)
    else:
        return JsonResponse({'error':'no query given'})





from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic

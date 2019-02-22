from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
import json

from .models import Movies
from .forms import SearchForm

class SignUp(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'signup.html'
    

def _process_search(request_values):
    """
    Processes the search i.e. finds the movies as per the given
    criteria in "request_values" arg and returns a list of 
    matching movies.
    """
    
    # init a dict for filter input key value pairs
    filter_value_dict = {'title':None, 
                         'year':None, 
                         'actor':None, 
                         'director':None, 
                         'genre':None, 
                         'lang':None, 
                         'country':None, 
                         'plot': None, 
                        }
    
    # init a dict for mapping db keys to filter function used for that key
    filter_func_dict = {'movie_title':'icontains', 
                        'title_year':'exact', 
                        'actor_1_name':'icontains', 
                        'actor_2_name':'icontains', 
                        'actor_3_name':'icontains', 
                        'director_name':'icontains', 
                        'genres':'icontains', 
                        'language':'iexact', 
                        'country':'iexact', 
                        'plot_keywords':'icontains',
                        }
    
    # init kwarg dict to store applicable filter key values
    # to be used in django model objects filter
    kwargs = {}
    # save the input filter keys as a list
    filter_keys = list(filter_value_dict.keys())
    
    for fkey in filter_keys:
        # check if the input filter key exists in the request data
        # and set the corresponding key with the input value in the 
        # filter_value_dict
        try:
            filter_value_dict[fkey] = request_values[fkey]
        except KeyError:
            # if some filer key is not present in filter_value_dict
            # then remove it
            filter_value_dict.pop(fkey)
        else:
            # search for a partial match of input key in filter_func_dict keys
            # and save the function(db specific) keys
            filter_func_keys = list(filter(lambda k: fkey in k, list(filter_func_dict.keys())))
            # update the kwargs dict with vaild key__func: value entry
            for key in filter_func_keys:
                kwargs.update({f'{key}__{filter_func_dict[key]}': filter_value_dict[fkey]})
    
    # get the matching movies using the kwargs dict just compiled
    movies_by_filter = Movies.objects.filter(**kwargs)
    # convert to python list
    search_results = list(movies_by_filter)
    # return the search_results along with filter_value_dict
    # for use in browser display of search results
    return search_results, filter_value_dict

def index(request):
    """
    View for index - '/movies/' path, to work as the app home page.
    """
    
    # get the total movies in db
    movie_count = Movies.objects.count()
    # get the 5 latest movies in database as per their release year
    latest_movies = list(Movies.objects.order_by('title_year'))[-5:]
    
    context = {'movie_count': movie_count, 
               'latest_movies': latest_movies}
    
    return render(request, 'movies/index.html', context)

def detail(request, movie_idx):
    """
    View for detail - '/movies/<db index>', 
    here the user can view the movie's details in the browser.
    """
    
    # get the movie's db index
    movie_by_idx = Movies.objects.get(index=movie_idx)
    
    context = {'movie': movie_by_idx}
    
    return render(request, 'movies/detail.html', context)

def search(request):
    """
    View for search - '/movies/search/' (browser based) 
    and '/movies/search/?key=value' (for API, url based) searches.
    """
    
    # GET method signifies that this request is an API request, primarily
    # but an empty GET request implies that it is a non-API request.
    if request.method == 'GET':
        # a non-API request
        if request.GET == {}:
            # instantiate the search form and render it.
            form = SearchForm()
            return render(request, 'movies/search_form.html', {'form': form})
        
        # an API request
        # save the GET request data
        request_values = request.GET
        # get the search result
        search_results, _ = _process_search(request_values)
        # return the serialized json data as an HTTP response 
        return HttpResponse(json.dumps([x.info() for x in search_results]))
    
    # now the user has posted the search form data
    elif request.method == 'POST':
        # save the user search data
        form = SearchForm(request.POST)
        # check validity
        if form.is_valid():
            # clean and save the request data
            request_values = form.cleaned_data
            request_values = {key:value for key, value in request_values.items() if value}
        
        # get the search results and the data used for filtering
        search_results, filter_value_dict = _process_search(request_values)
        
        context = {'search_keys': filter_value_dict, 
                   'search_results': search_results}
        
        return render(request, 'movies/search.html', context)


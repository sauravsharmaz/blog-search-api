from drf_haystack.filters import (HaystackAutocompleteFilter,
                                  HaystackFacetFilter, HaystackHighlightFilter)
from drf_haystack.mixins import FacetMixin
from drf_haystack.viewsets import HaystackViewSet

from .models import Blog
from .serializers import BlogFacetSerializer, BlogSerializer

# Create your views here.


class BlogSearchAPI2(HaystackViewSet):

    # `index_models` is an optional list of which models you would like to include
    # in the search result. You might have several models indexed, and this provides
    # a way to filter out those of no interest for this particular view.
    # (Translates to `SearchQuerySet().models(*index_models)` behind the scenes.
    index_models = [Blog]

    serializer_class = BlogSerializer


class SearchBlogViewSet(FacetMixin, HaystackViewSet):

    index_models = [Blog]

    # This will be used to filter and serialize regular queries as well
    # as the results if the `facet_serializer_class` has the
    # `serialize_objects = True` set.
    serializer_class = BlogSerializer
    filter_backends = [HaystackHighlightFilter, HaystackAutocompleteFilter]

    # This will be used to filter and serialize faceted results
    facet_serializer_class = BlogFacetSerializer  # See example above!
    facet_objects_serializer_class = BlogFacetSerializer 
    facet_filter_backends = [HaystackFacetFilter]   # This is the default facet filter, and
                                                    # can be left out.
    facet_query_params_text = 'params' #Default is 'selected_facets'

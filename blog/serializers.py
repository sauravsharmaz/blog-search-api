from drf_haystack.serializers import HaystackSerializer, HaystackFacetSerializer
from .search_indexes import BlogIndex
from datetime import datetime, timedelta
class BlogSerializer(HaystackSerializer):
    
    class Meta:
        index_classes = [BlogIndex]
        fields = ['text', 'author']
    

class BlogFacetSerializer(HaystackFacetSerializer):

    serialize_objects = True  # Setting this to True will serialize the
                               # queryset into an `objects` list. This
                               # is useful if you need to display the faceted
                               # results. Defaults to False.
    class Meta:
        index_classes = [BlogIndex]
        fields = ["title", "text", "author", "pub_date"]
        field_options = {
            "title": {},
            "text": {},
            "author": {},
            "pub_date": {
                "start_date": datetime.now() - timedelta(days=3 * 365),
                "end_date": datetime.now(),
                "gap_by": "month",
                "gap_amount": 3
            }
        }
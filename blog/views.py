from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# from .models import Blog
from .serializers import BlogSerializer
from haystack.query import SearchQuerySet, AutoQuery, SQ

# Create your views here.

class BlogSearchAPI(APIView):

    def get(self, request):
        search_query = request.GET.get('q')
        if search_query is None:
            return Response({'message': 'query is required'}, status=status.HTTP_400_BAD_REQUEST)
        # import pdb; pdb.set_trace()
        search_results = SearchQuerySet().filter(
                    SQ(title=AutoQuery(search_query)) | SQ(text=AutoQuery(search_query))
                )
        # pdb.set_trace()
        print(search_results)
        serializer = BlogSerializer(search_results, many=True)
        return Response(data = serializer.data, status=status.HTTP_200_OK)
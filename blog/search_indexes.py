from haystack import indexes
from .models import Blog


class BlogIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    id = indexes.IntegerField(model_attr='id')
    title = indexes.CharField(model_attr='title')
    author = indexes.CharField(model_attr='author', faceted=True)
    pub_date = indexes.DateTimeField(model_attr='pub_date', faceted=True)

    def get_model(self):
        return Blog

    def index_queryset(self, using=None):
        """Used when the entire index for model is updated."""
        return self.get_model().objects.all()
from django.contrib.syndication.views import Feed
from django.template.defaultfilters import truncatewords
from .models import product
from django.urls import reverse

class LatestPostFeed(Feed):
    title = 'Product Services'
    link = "/drcomments/"
    description = 'Your products are safe in our hands'

    def items(self):
        return product.objects.all()[:3]

    def item_title(self,item):
        return item.name
    def item_description(self,item):
        return truncatewords (item.description,30)

    def item_link(self):
        return reverse ('home')



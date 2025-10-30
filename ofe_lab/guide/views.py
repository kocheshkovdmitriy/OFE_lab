from django.shortcuts import render
from django.views import generic

from guide import models


class ArticlesFromSection(generic.DetailView):
    template_name = 'guide/article.html'
    context_object_name = 'article'
    model = models.Article

    def get_context_data(self, **kwargs):
        return super(ArticlesFromSection, self).get_context_data(object=kwargs['object'],
                                                                 articles=models.Article.objects.filter(
                                                                     section=kwargs['object'].section
                                                                 ).order_by('priority'))



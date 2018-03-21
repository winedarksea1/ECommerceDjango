from django.views.generic import ListView, DetailView
from django.shortcuts import render, get_object_or_404
from django.http import Http404

from .models import Product
# Create your views here.

class ProductFeaturedListView(ListView):
    template_name = 'products/featured-list.html'

    def get_queryset(self, *args, **kwargs):
        request = self.request
        return Product.objects.featured()


class ProductFeaturedDetailView(DetailView):
    pass

class ProductListView(ListView):
    queryset = Product.objects.all()
    template_name = 'products/list.html'

    # def get_context_data(self, *args, **kwargs):
    #     context = super(ProductListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context


def product_list_view(request):
    queryset = Product.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, 'products/list.html', context)


class ProductDetailView(DetailView):
    queryset = Product.objects.all()
    template_name = 'products/detail.html'

    def get_object(self, *args, **kwargs):
        request = self.request
        pk = self.kwargs.get('pk')
        instance = Product.get_by_id(pk)
        if instance == None:
            exception_string = 'Could not find product with id: {0}'.format(pk)
            raise Http404(exception_string)
        return instance


def product_detail_view(request, pk=None, *args, **kwargs):

    instance = Product.objects.get_by_id(pk)
    if instance == None:
        exception_string = 'Could not find product with id: {0}'.format(pk)
        raise Http404(exception_string)

    context = {
        'object': instance
    }

    return render(request, 'products/detail.html', context)

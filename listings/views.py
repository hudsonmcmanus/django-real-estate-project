from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Listing
from .choices import *

def index(request):
    listings = Listing.objects.order_by('-list_date').filter(is_published=True)

    paginator = Paginator(listings, 6)
    page = request.GET.get('page')
    paged_listings = paginator.get_page(page)

    context = {
        'listings': paged_listings
    }

    return render(request, 'listings/listings.html', context)


def listing(request, listing_id):
    listing = get_object_or_404(Listing, pk=listing_id)

    context = {
        'listing': listing
    }

    return  render(request, 'listings/listing.html', context)


def search(request):
    queryset = Listing.objects.order_by('-list_date')

    #Keywords
    if 'keywords' in request.GET:
        keywords = request.GET['keywords']
        if keywords:
            queryset = queryset.filter(description__icontains=keywords, is_published=True)

    #City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset = queryset.filter(city__iexact=city, is_published=True)

    #Province
    if 'province' in request.GET:
        province = request.GET['province']
        if province:
            queryset = queryset.filter(province__iexact=province, is_published=True)

    #Bedroom
    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']
        if bedrooms:
            queryset = queryset.filter(bedrooms__lte=bedrooms, is_published=True)

    #Price
    if 'price' in request.GET:
        price = request.GET['price']
        if price:
            queryset = queryset.filter(price__lte=price, is_published=True)


    context = {
        'provinces': province_names,
        'price_choices': price_choices,
        'bedroom_choices': bedroom_choices,
        'listings': queryset,
        'values': request.GET,
    }

    return  render(request, 'listings/search.html', context)

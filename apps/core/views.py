from django.contrib import messages
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse

from apps.core.forms import VoteForm
from apps.core.services.show_detail import get_show_detail, get_show_reviews
from apps.core.services.show_list import get_show_list
from apps.core.services.show_vote import set_show_vote


def show_list(request):
    data = get_show_list()
    paginator = Paginator(data, 10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'page_obj': page_obj}
    return render(request, template_name="core/show_list.html", context=context)


def show_detail(request, pk):

    context = {'item': get_show_detail(pk),
               'reviews': get_show_reviews(pk)}
    return render(request, template_name="core/show_detail.html", context=context)


def show_vote(request, pk):
    form = VoteForm(request.POST)

    if form.is_valid():
        set_show_vote(obj_id=pk,
                      username=form.cleaned_data["username"],
                      password=form.cleaned_data["password"],
                      rating=form.cleaned_data["rating"])
        messages.success(request, 'Your review has been successfully sent!')
        return redirect(reverse('core:top-100'))

    messages.error(request, 'Failed. Please check your inputs again!')
    return redirect(reverse('core:show-detail', args=[pk]))


def show_discover(request, show_name=None, release_year=None, popularity=None):

    return render(request, template_name="core/show_discover.html")

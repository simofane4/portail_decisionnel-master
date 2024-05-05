from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect
import student as st
from forms import myForm
from untitled.traitement import mlpmethode
from untitled.traitement import svmmethode
from untitled.traitement import knnmethode
from untitled.traitement import cartmethode


def home(request):
    return render(request, 'index.html')


def mlp(request):
    return render(request, 'register.html')


def echec(request):
    return render(request, 'echec.html')


def success(request):
    return render(request, 'success.html')


def register(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = myForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            result = mlpmethode(form.cleaned_data['failure'], form.cleaned_data['fedu'], form.cleaned_data['schoolsup'],
                                form.cleaned_data['medu'], form.cleaned_data['goout'], form.cleaned_data['freetime'])
            # process the data in form.cleaned_data as required
            # ...
            print("===========================================")
            print(result)
            # redirect to a new URL:
            if result[0] == 1:
                return HttpResponseRedirect("/echec")
            else:
                return HttpResponseRedirect("/success")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = myForm()

    return render(request, 'name.html', {'form': form})


def svm_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = myForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            result = svmmethode(form.cleaned_data['failure'], form.cleaned_data['fedu'], form.cleaned_data['schoolsup'],
                                form.cleaned_data['medu'], form.cleaned_data['goout'], form.cleaned_data['freetime'])
            # process the data in form.cleaned_data as required
            # ...
            print("===========================================")
            print(result)
            # redirect to a new URL:
            if result[0] == 1:
                return HttpResponseRedirect("/echec")
            else:
                return HttpResponseRedirect("/success")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = myForm()

    return render(request, 'name_svm.html', {'form': form})


def knn_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = myForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            result = knnmethode(form.cleaned_data['medu'], form.cleaned_data['fedu'],
                                form.cleaned_data['relation_familiale'],
                                form.cleaned_data['freetime'], form.cleaned_data['goout'],
                                form.cleaned_data['consomation_alcool'], form.cleaned_data['sante'],
                                form.cleaned_data['age'],
                                form.cleaned_data['absences'], form.cleaned_data['mjob'],
                                form.cleaned_data['fjob'], form.cleaned_data['raison'])
            # process the data in form.cleaned_data as required
            # ...
            print("===========================================")
            print(result)
            # redirect to a new URL:
            if result[0] == 1:
                return HttpResponseRedirect("/echec")
            else:
                return HttpResponseRedirect("/success")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = myForm()

    return render(request, 'name_knn.html', {'form': form})
#def cartmethode(failures, Fedu, schoolsup, Medu,goout,freetime):
def cart_view(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = myForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            result = cartmethode(form.cleaned_data['failure'], form.cleaned_data['fedu'],
                                form.cleaned_data['schoolsup'],
                                form.cleaned_data['medu'], form.cleaned_data['goout'],
                                form.cleaned_data['freetime'])
            # process the data in form.cleaned_data as required
            # ...
            print("===========================================")
            print(result)
            # redirect to a new URL:
            if result[0] == 1:
                return HttpResponseRedirect("/echec")
            else:
                return HttpResponseRedirect("/success")
    # if a GET (or any other method) we'll create a blank form
    else:
        form = myForm()

    return render(request, 'name_cart.html', {'form': form})

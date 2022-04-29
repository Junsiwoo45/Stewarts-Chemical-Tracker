from django.shortcuts import render
from .forms import RegistrationForm
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import LawnItem
from .models import PestItem
from .models import TreeItem
from .forms import Advice
from django.core.paginator import Paginator
from django.template import loader
# Create your views here.


def thankyouadvice(request):
    return render(request, 'stewarts/thankyouadvice.html')

def home(request):
    return render(request, 'stewarts/home.html')

def lawn(request):
    return render(request, 'stewarts/lawn.html')

def pest(request):
    return render(request, 'stewarts/pest.html')

def tree(request):
    return render(request, 'stewarts/tree.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome {username}! Your account has been created.')
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'stewarts/register.html', {'form': form})


@login_required
def profilepage(request):
    return render(request, 'stewarts/profile.html')


def lawn_list(request):
    lawn_object = LawnItem.objects.all()
    lawn_name = request.GET.get('lawn_name')
    if lawn_name != '' and lawn_name is not None:
        lawn_object = lawn_object.filter(name__icontains=lawn_name)
    paginator = Paginator(lawn_object, 2)
    page = request.GET.get('page')
    lawn_object = paginator.get_page(page)
    return render(request, 'stewarts/lawndetail.html', {'lawn_object': lawn_object})


def tree_list(request):
    tree_object = TreeItem.objects.all()
    tree_name = request.GET.get('tree_name')
    if tree_name != '' and tree_name is not None:
        tree_object = tree_object.filter(name__icontains=tree_name)
    paginator = Paginator(tree_object, 2)
    page = request.GET.get('page')
    tree_object = paginator.get_page(page)
    return render(request, 'stewarts/treedetail.html', {'tree_object': tree_object})


def pest_list(request):
    pest_object = PestItem.objects.all()
    pest_name = request.GET.get('pest_name')
    if pest_name != '' and pest_name is not None:
        pest_object = pest_object.filter(name__icontains=pest_name)
    paginator = Paginator(pest_object, 2)
    page = request.GET.get('page')
    pest_object = paginator.get_page(page)
    return render(request, 'stewarts/pestdetail.html', {'pest_object': pest_object})


def inputlawn(request):
    if request.method == 'POST':
        gallon = request.POST.get('gallon')
        squareft = request.POST.get('squareft')
        total = (int(gallon) / int(squareft)) * 5
        return render(request, 'stewarts/inputlawn.html', {'total': total})
    return render(request, 'stewarts/inputlawn.html')

def inputpest(request):
    if request.method == 'POST':
        gallon = request.POST.get('gallon')
        squareft = request.POST.get('squareft')
        total = (int(gallon) / int(squareft)) * 10
        return render(request, 'stewarts/inputpest.html', {'total': total})
    return render(request, 'stewarts/inputpest.html')


def inputtree(request):
    if request.method == 'POST':
        gallon = request.POST.get('gallon')
        squareft = request.POST.get('squareft')
        total = (int(gallon) / int(squareft)) * 20
        return render(request, 'stewarts/inputtree.html', {'total': total})
    return render(request, 'stewarts/inputtree.html')


def adviceform(request):
    form = Advice(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('thankyouadvice')

    return render(request, 'stewarts/advice-form.html', {'form': form})
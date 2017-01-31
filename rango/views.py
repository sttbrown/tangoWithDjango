from django.shortcuts import render

from django.http import HttpResponse

from rango.models import Category

from rango.models import Page

from rango.forms import CategoryForm

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]

    viewed_list = Page.objects.order_by('-views')[:5]

    context_dict = {'categories': category_list, 'viewed': viewed_list}

    #return HttpResponse("Rango says give me a biscuit <br/> <a href='/rango/about/'>About</a>")
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    #return HttpResponse("This is the about page <br/> <a href='/rango/'>Home</a>")
    return render(request, 'rango/about.html')


def show_category(request, category_name_slug):
    context_dict= {}

    try:
        category = Category.objects.get(slug=category_name_slug)

        pages = Page.objects.filter(category=category)

        context_dict['pages'] = pages

        context_dict['category'] = category

        #maybe
       # context_dict['likes'] = likes


    except Category.DoesNotExist:
        context_dict['category']= None
        context_dict['pages']= None

    return render(request, 'rango/category.html', context_dict)


def add_category(request):
    form = CategoryForm()

    #HTTP?
    if request.method == 'POST':
        form = CategoryForm(request.POST)

        if form.is_valid():
            #save category
            form.save(commit=True)
            return index(request)
        else:
            print(form.errors)

    return render(request, 'rango/add_category.html', {'form':form})
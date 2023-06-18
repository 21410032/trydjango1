from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Article
from .forms import ArticleCreate
# Create your views here.
def articledetail_view(request,id=None):
    article_obj=None
    if id is not None:
     article_obj=Article.objects.get(id=id)
    context={
        "obj":article_obj
    }
    return render(request,'article/details.html',context=context)
@login_required
def article_create_view(request):
    form=ArticleCreate(request.POST or None)
    context={
        "form":form
    }
    if form.is_valid():
        obj=form.save()
        context["form"]=ArticleCreate()
    #   title=form.cleaned_data.get("title")
    #   content=form.cleaned_data.get("content")
    #   obj=Article.objects.create(title=title,content=content)
    #     context={
    #       "obj":obj,
    #        "created":True
    #    }
    return render(request,'article/create.html',context=context)    
# @login_required
# def article_create_view(request):
#     form=ArticleCreate(request.POST)
#     context={
#         "form":form
#     }
#     if form.is_valid():
#       title=form.cleaned_data.get("title")
#       content=form.cleaned_data.get("content")
#       obj=Article.objects.create(title=title,content=content)
#         context={
#           "obj":obj,
#            "created":True
#        }
#     return render(request,'article/create.html',context=context)
    
def article_search_view(request):
    query_dict=request.GET
    querydict=query_dict.get("q")
    obj=None
    if querydict is not None:
     obj=Article.objects.get(id=querydict)
    context={"obj":obj}
    return render(request,'article/search.html',context=context)
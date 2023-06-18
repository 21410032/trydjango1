"""
To render html webpages
"""
from django.http import HttpResponse
import random
from articles.models import Article
# from django.template.loader import render_to_string
# name="tinky"  #hard coded
# # numberid = random.randint(0,4) #pseudo random
# # from the database??
# # obj=Article.objects.get(id=numberid)

# # Django templates

# def home_view(request):
#  numberid = random.randint(0,4) #pseudo random
#  obj=Article.objects.get(id=numberid)
#  context = {
#     "title":obj.title,
#     "content":obj.content
#  }
#  Httpopt=render_to_string("home_view.html",context=context)

#  """
#  take in a request(django sends a request)
#  RETURN HTML as a response (we pick to return the response)
#  """
#  return HttpResponse(Httpopt)



# Another way


from django.template.loader import get_template
name="tinky"  #hard coded
# numberid = random.randint(0,4) #pseudo random
# from the database??
# obj=Article.objects.get(id=numberid)

# Django templates

def home_view(request,*args,**kwargs):
 numberid = random.randint(0,3) #pseudo random
 obj=Article.objects.get(id=numberid)
 objlist=[22,32,45,67,765]
 obj_queryset=Article.objects.all()
 print(id)
 context = {
    'obj_queryset':obj_queryset,
    "objlist":objlist,
    "title":obj.title,
    "content":obj.content,
    "id":obj.id
 }
 opt=get_template("home_view.html")
 Httpopt=opt.render(context=context)

 """
 take in a request(django sends a request)
 RETURN HTML as a response (we pick to return the response)
 """
 return HttpResponse(Httpopt)
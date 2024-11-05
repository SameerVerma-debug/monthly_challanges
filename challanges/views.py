from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.template import loader
# Create your views here.

month_challange_mapper = {
    "january": "January Challange",
    "february": "February Challange",
    "march": "March Challange",
    "april": "April Challange",
    "may": "May Challange",
    "june": "June Challange",
    "july": "July Challange",
    "august": "August Challange",
    "september": "September Challange",
    "october": "October Challange",
    "november": "November Challange",
    "december": None,
}

def create_index_page_response():
  # print("----",base_url)
  response = ""
  for month in month_challange_mapper.keys():
    month_path = reverse("month-challange",args=[month])
    temp = f"<li><a href='{month_path}'>{month.capitalize()}</a></li>\n"
    response += temp
  
  response = "<ul>\n" + response + "\n</ul>"
  return response

def index(request):
    # response = create_index_page_response()
    # return HttpResponse(response)
    return render(request,"challanges/index.html",{
      "months":[month for month in month_challange_mapper.keys()]
    })


def month_challange(request, month):
    try:
        challange_text = month_challange_mapper[month.lower()]
        
        #convert html document to a string
        # response_string = loader.render_to_string("challanges/challange.html")
        # return HttpResponse(response_string)
        
        #render (shortcut for above steps)
        return render(request,"challanges/challange.html",{
          "month_challange": challange_text,
          "month_name":month
        })
    except:
        # not_found_response = loader.render_to_string("404.html")
        # return HttpResponseNotFound(not_found_response)
        
        raise Http404() #raises an 404 exception and also look for 404.html file to send as a response


def month_challange_by_num(request, month):
    try:
        months = list(month_challange_mapper.keys())
        if month < 1 or month > 12:
            raise Exception()
        redirect_month = months[month-1]
        redirect_path = reverse("month-challange", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        not_found_response = loader.render_to_string("404.html")
        return HttpResponseNotFound(not_found_response)

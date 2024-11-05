from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
# Create your views here.

month_challange_mapper = {
    "january": 1,
    "february": 2,
    "march": 3,
    "april": 4,
    "may": 5,
    "june": 6,
    "july": 7,
    "august": 8,
    "september": 9,
    "october": 10,
    "november": 11,
    "december": 12,
}

month_wise_challange = ["Not a Valid Month", "january Challange", "february Challange", "march Challange", "april Challange", "may Challange", "june Challange",
                        "july Challange", "august Challange", "september Challange", "october Challange", "november Challange", "december challange"]

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
    response = create_index_page_response()
    return HttpResponse(response)


def month_challange(request, month):
    try:
        month_num = month_challange_mapper[month]
        challange = month_wise_challange[month_num]
    except:
        return HttpResponseNotFound("Not a valid month number")
    return HttpResponse(challange)


def month_challange_by_num(request, month):
    # try:
    #     challange = month_wise_challange[month]
    # except:
    #     return HttpResponseNotFound("Not a valid month number")
    # return HttpResponse(challange)

    try:
        months = list(month_challange_mapper.keys())
        if month < 1 or month > 12:
            raise Exception()
        redirect_month = months[month-1]
        redirect_path = reverse("month-challange", args=[redirect_month])
        return HttpResponseRedirect(redirect_path)
    except:
        return HttpResponseNotFound("Not a valid month")

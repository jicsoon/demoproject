from django.shortcuts import render

from .models import Visitor
from .forms import VisitorForm
from django.http import JsonResponse
from django.template.loader import render_to_string



def register(request):
    form = VisitorForm()
    context = {'form':form}
    return render(request,'ajax_crud/register.html',context)

def createVisitor(request):
    form = VisitorForm()
    context = {'form':form}
    html_form = render_to_string('ajax_crud/register.html',context,request =request)
    return JsonResponse({'html_form':html_form})


def visitor_list(request):
    visitors = Visitor.objects.all()
    context = {'visitors': visitors}
    return render(request,'ajax_crud/visitor_list.html',context)



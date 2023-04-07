from django.shortcuts import render, redirect
from django.views.generic.edit import FormView,CreateView
from django.views.generic.list import ListView
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.views.generic import TemplateView
"Local"
from mainapp.forms import CalculationResultForm
from mainapp.models import CalculationResult

class HomePageView(TemplateView):
    template_name = "index.html"

def calculation_method(request):
    data = CalculationResult.objects.last()
    context = {
        'data': data
    }
    return render(request, "calculation.html", context)

    



def calc_formula(request):
    if request.method == 'POST':
        form = CalculationResultForm(request.POST)

        if form.is_valid():
            
            return HttpResponseRedirect('/thanks/')
    else:
        form = CalculationResultForm()
    context = {
        "form": form
    }
    return render(request, "calculate.html", context)

def check_post(request):
    if request.method == 'POST':
        print(True)
        x1 = request.POST.get('x1')
        x2 = request.POST.get('x2')
        x3 = request.POST.get('x3')
        y1 = request.POST.get('y1')
        y2 = request.POST.get('y2')
        y3 = request.POST.get('y3')
        z1 = request.POST.get('z1')
        z2 = request.POST.get('z2')
        z3 = request.POST.get('z3')
        r1 = request.POST.get('r1')
        r2 = request.POST.get('r2')
        r3 = request.POST.get('r3')
        obj = CalculationResult.objects.create(
            x1=x1, x2=x2, x3=x3,
            y1=y1, y2=y2, y3=y3,
            z1=z1, z2=z2, z3=z3, 
            r1=r1, r2=r2, r3=r3
        )
        # success("Request data submitted")
        return redirect('success-page')
        # return render(request, "")
    else:
        print(False)
    return HttpResponse("Not found")

def success_page(request):
    return HttpResponse("Hammasi yaxshi")


class CalculationResultView(FormView):
    form_class = CalculationResultForm
    template_name = "calculate copy.html"
    success_url = "/thanks/"

    
    def post(self):
        pass
    
    

    
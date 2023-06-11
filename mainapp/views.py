from django.shortcuts import render, redirect
from django.views.generic.edit import FormView,CreateView
from django.views.generic.list import ListView
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.template import loader
from django.views.generic import TemplateView
from django.views.generic.edit import DeleteView
from plotly.offline import plot
from plotly.graph_objs import Scatter

"Local"
from mainapp.forms import CalculationResultForm
from mainapp.models import CalculationResult, ImageClass, WisdomWords
"Built-in"
import random
import numpy as np 
import plotly.graph_objs as go  



def vector_plot(tvects,is_vect=True,orig=[0,0,0]):
    """Plot vectors using plotly"""

    if is_vect:
        if not hasattr(orig[0],"__iter__"):
            coords = [[orig,np.sum([orig,v],axis=0)] for v in tvects]
        else:
            coords = [[o,np.sum([o,v],axis=0)] for o,v in zip(orig,tvects)]
    else:
        coords = tvects

    data = []
    for i,c in enumerate(coords):
        X1, Y1, Z1 = zip(c[0])
        X2, Y2, Z2 = zip(c[1])
        vector = go.Scatter3d(x = [X1[0],X2[0]],
                              y = [Y1[0],Y2[0]],
                              z = [Z1[0],Z2[0]],
                              marker = dict(size = [0,5],
                                            color = ['blue'],
                                            line=dict(width=5,
                                                      color='DarkSlateGrey')),
                              name = 'Vector'+str(i+1))
        data.append(vector)

    layout = go.Layout(
             margin = dict(l = 4,
                           r = 4,
                           b = 4,
                           t = 4)
                  )
    fig = go.Figure(data=data,layout=layout)
    k = data
    return plot(fig, output_type='div')

"Static Pages"
class HomePageView(TemplateView):
    template_name = "homepage.html"
class AboutPageView(TemplateView):
    template_name = "about.html"



"Dinamic Pages"

def calc_inaccuracy(request):
    d = CalculationResult.objects.last()
    ins = CalcClass(x1=d.x1, x2=d.x2, x3=d.x3, x4=d.x4,
                    y1=d.y1, y2=d.y2, y3=d.y3, y4=d.y4,
                    z1=d.z1, z2=d.z2, z3=d.z3, z4=d.z4,
                    r1=d.r1, r2=d.r2, r3=d.r3, r4=d.r4,
                    rkv1=d.rkv1, rkv2=d.rkv2, rkv3=d.rkv3, rkv4=d.rkv4                      
                        )
    index = ins.get_4x_index_r()
    ls_ins =[value for value in ins.get_4x_index_r().values()]
    comp = [ value for value in ins.get_algebraic_complement().values()]
    D_A = ins.d_koeff()
    err_values = [ value for value in ins.calc_inverse_matrix().values()] 
    context = {'ls_ins': ls_ins,
               'index': index,
               'da':D_A,
               'comp':comp,
               'err': err_values,
               
               }
    return render(request, 'inaccuracy.html', context)
    


class AnswersDeleteView(DeleteView):
    model = CalculationResult
    success_url = "/"
    template_name = "confirm_delete_answer.html"

def differ3_4(request):
    d = CalculationResult.objects.last()
    ins = CalcClass(x1=d.x1, x2=d.x2, x3=d.x3, x4=d.x4,
                    y1=d.y1, y2=d.y2, y3=d.y3, y4=d.y4,
                    z1=d.z1, z2=d.z2, z3=d.z3, z4=d.z4,
                    r1=d.r1, r2=d.r2, r3=d.r3, r4=d.r4,
                    rkv1=d.rkv1, rkv2=d.rkv2, rkv3=d.rkv3, rkv4=d.rkv4                      
                    )
    ans3 = ins.calc_3x()
    ans32 = ins.calc_3x_r()
    ans4 = ins.calc_4x()
    ans42 = ins.calc_4x_r()
    ansb = ins.formula_fc()
    # ansb2 = ins.formula_fc()

    context = {
        'ans3': ans3,
        'ans4': ans4,
        'ans3_r': ans32,
        'ans4_r': ans42,
        'ansb': ansb,
    }
    return render(request, 'difference.html', context)

def coor_3(request):
    d = CalculationResult.objects.last()
    ins = CalcClass(x1=d.x1, x2=d.x2, x3=d.x3, x4=d.x4,
                    y1=d.y1, y2=d.y2, y3=d.y3, y4=d.y4,
                    z1=d.z1, z2=d.z2, z3=d.z3, z4=d.z4,
                    r1=d.r1, r2=d.r2, r3=d.r3, r4=d.r4,
                    rkv1=d.rkv1, rkv2=d.rkv2, rkv3=d.rkv3, rkv4=d.rkv4                      
                        )
    ls_ins =[value for value in ins.get_3x_index().values()]
    xyz = ins.calc_3x()
    print(ins.get_3x_index())
    print(ins.calc_3x())
    p0 = [d.x1-xyz[0], d.y1-xyz[1], d.z1-xyz[2]]
    p1 = [d.x2-xyz[0], d.y2-xyz[1], d.z2-xyz[2]]
    p2 = [d.x3-xyz[0], d.y3-xyz[1], d.z3-xyz[2]]
    content = {
        'd' : d,
        'ls_ins' : ls_ins,
        'xyz' : xyz,
        'div': vector_plot([p0, p1, p2], orig=[xyz[0], xyz[1], xyz[2]]),
        # 'div2': vector_plot([p0, p1, p2], orig=[xyz[3], xyz[4], xyz[5]])
        
        
    }
    return render(request, "3coor.html", content)

def coor_4(request):
    d = CalculationResult.objects.last()
    if d.x4 == '':
        return HttpResponse('404.html')
    ins = CalcClass(x1=d.x1, x2=d.x2, x3=d.x3, x4=d.x4,
                        y1=d.y1, y2=d.y2, y3=d.y3, y4=d.y4,
                        z1=d.z1, z2=d.z2, z3=d.z3, z4=d.z4,
                        r1=d.r1, r2=d.r2, r3=d.r3, r4=d.r4,
                        rkv1=d.rkv1, rkv2=d.rkv2, rkv3=d.rkv3, rkv4=d.rkv4                      
                        )
    ls_ins = [value for value in ins.get_4x_index().values()]
    print(ins.get_4x_index())
    xyz = ins.calc_4x()
    p0 = [d.x1-xyz[0], d.y1-xyz[1], d.z1-xyz[2]]
    p1 = [d.x2-xyz[0], d.y2-xyz[1], d.z2-xyz[2]]
    p2 = [d.x3-xyz[0], d.y3-xyz[1], d.z3-xyz[2]]
    p3 = [d.x4-xyz[0], d.y4-xyz[1], d.z4-xyz[2]]
    context={
        'd' : d,
        'ls_ins' : ls_ins,
        'root' : xyz,
        "div": vector_plot([p0, p1, p2, p3], orig=[xyz[0], xyz[1], xyz[2]])
    }
    return render(request, 'coor4.html', context)

def homepage_view(request):
    data = ImageClass.objects.first()
    wword = WisdomWords.objects.all()
    print(random.choice(wword))
    rword = random.choice(wword)
    print(data.image.url)
    context = {
        'data': data,
        'word': rword,
    }
    return render(request, "homepage.html", context)


def calculation_method(request):
    data = CalculationResult.objects.last()
    context = {
        'data': data
    }
    return render(request, "calculation.html", context)


"""Lokal"""
from .formula import CalcClass
# user uchun formulalar tarixini ko'rsatish
def get_history(request):
    id = request.user.id
    dat = ImageClass.objects.get(id=1)
    # data = CalculationResult.objects.filter(user_id=id)
    data = CalculationResult.objects.order_by('-id')
    ls_res=[]
    ls_koef =[]
    indexs=[]
    for d in  data:
        ins = CalcClass(x1=d.x1, x2=d.x2, x3=d.x3, x4=d.x4,
                        y1=d.y1, y2=d.y2, y3=d.y3, y4=d.y4,
                        z1=d.z1, z2=d.z2, z3=d.z3, z4=d.z4,
                        r1=d.r1, r2=d.r2, r3=d.r3, r4=d.r4,
                        rkv1=d.rkv1, rkv2=d.rkv2, rkv3=d.rkv3, rkv4=d.rkv4                      
                        )
        
        ls_res.append([d, ins.calc_3x(),  ins.get_3x_index()] )
    images = ImageClass.objects.all()
    context = {
        'data': data,
        'img':dat,
        'ls':ls_res,
        'images': images,
        'indexs':indexs,
    }
    return render(request, "history.html", context)

def calc_formula(request):
    if request.method == 'POST':
        form = CalculationResultForm(request.POST)
        if form.is_valid():
            form.save()
            d = CalculationResult.objects.last()
            ls_res=[]
            
            ins = CalcClass(x1=d.x1, x2=d.x2, x3=d.x3, x4=d.x4,
                                y1=d.y1, y2=d.y2, y3=d.y3, y4=d.y4,
                                z1=d.z1, z2=d.z2, z3=d.z3, z4=d.z4,
                                r1=d.r1, r2=d.r2, r3=d.r3, r4=d.r4                      
                                )
            ls_res = (ins.get_4x_index())
            context={
                "ls" : ls_res
            }

            return render(request, "result.html", context)
    else:
        form = CalculationResultForm()
    context = {
        "form": form
    }
    return render(request, "calculate.html", context)

import os

def check_post(request):
    if request.method == 'POST':
        print(True)
        x1 = request.POST.get('x1')
        x2 = request.POST.get('x2')
        x3 = request.POST.get('x3')
        x4 = request.POST.get('x4')
        y1 = request.POST.get('y1')
        y2 = request.POST.get('y2')
        y3 = request.POST.get('y3')
        y4 = request.POST.get('y4')
        z1 = request.POST.get('z1')
        z2 = request.POST.get('z2')
        z3 = request.POST.get('z3')
        z4 = request.POST.get('z4')
        r1 = request.POST.get('r1')
        r2 = request.POST.get('r2')
        r3 = request.POST.get('r3')
        r4 = request.POST.get('r4')
        rkv1 = request.POST.get('rkv1')
        rkv2 = request.POST.get('rkv2')
        rkv3 = request.POST.get('rkv3')
        rkv4 = request.POST.get('rkv4')
        if x4 == '':
            x4 = 0
            y4 = 0
            z4 = 0
            r4 = 0
            rkv1 = 0
            rkv2 = 0
            rkv3 = 0
            rkv4 = 0

            obj = CalculationResult.objects.create(
                x1=x1, x2=x2, x3=x3, 
                y1=y1, y2=y2, y3=y3, 
                z1=z1, z2=z2, z3=z3,  
                r1=r1, r2=r2, r3=r3, 
            )
        else:
            obj = CalculationResult.objects.create(
                x1=x1, x2=x2, x3=x3, x4=x4, rkv1=rkv1,
                y1=y1, y2=y2, y3=y3, y4=y4, rkv2=rkv2,
                z1=z1, z2=z2, z3=z3, z4=z4, rkv3=rkv3, 
                r1=r1, r2=r2, r3=r3, r4=r4, rkv4=rkv4,
            )
        d = CalculationResult.objects.last()
        ls_res=[]
        
        ins = CalcClass(x1=d.x1, x2=d.x2, x3=d.x3, x4=d.x4, 
                            y1=d.y1, y2=d.y2, y3=d.y3, y4=d.y4,
                            z1=d.z1, z2=d.z2, z3=d.z3, z4=d.z4,
                            r1=d.r1, r2=d.r2, r3=d.r3, r4=d.r4,
                            rkv1=d.rkv1, rkv2=d.rkv2, rkv3=d.rkv3, rkv4=d.rkv4                     
                            )
        ls_res = (ins.calc_3x())
        s = CalcClass(x1=d.x1, x2=d.x2, x3=d.x3, x4=d.x4,
                            y1=d.y1, y2=d.y2, y3=d.y3, y4=d.y4,
                            z1=d.z1, z2=d.z2, z3=d.z3, z4=d.z4,
                            r1=d.r1, r2=d.r2, r3=d.r3, r4=d.r4,
                            rkv1=d.rkv1, rkv2=d.rkv2, rkv3=d.rkv3, rkv4=d.rkv4                       
                            )
        # fig_address = s.get_graph(x=ls_res[0], y=ls_res[1], z=ls_res[2])
        # fig_address = s.get_graph(x=ls_res[0], y=ls_res[1], z=ls_res[2])
        # d.img = fig_address
        # d.save()
        # img = CalculationResult.objects.last()
        # images = ImageClass.objects.last()
        # # print(fig_address)
        # context={
        #     "ls" : ls_res,
        #     "img" : img,
        #     "x": round(ls_res[0]),
        #     "y": round(ls_res[1]),
        #     "z": round(ls_res[2]),
        #     "figaddress": "ig_address",
        #     "images": images,
        #     "d": d
        # }
        # return render(request, "result.html", context)
        ls_ins =[value for value in ins.get_3x_index().values()]
        xyz = ins.calc_3x()
        print(ins.get_3x_index())
        print(ins.calc_3x())
        p0 = [d.x1-xyz[0], d.y1-xyz[1], d.z1-xyz[2]]
        p1 = [d.x2-xyz[0], d.y2-xyz[1], d.z2-xyz[2]]
        p2 = [d.x3-xyz[0], d.y3-xyz[1], d.z3-xyz[2]]
        content = {
            'd' : d,
            'ls_ins' : ls_ins,
            'xyz' : xyz,
            'div': vector_plot([p0, p1, p2], orig=[xyz[0], xyz[1], xyz[2]]),
            # 'div2': vector_plot([p0, p1, p2], orig=[xyz[3], xyz[4], xyz[5]])


        }
        return render(request, "result.html", content)

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
    
    

    
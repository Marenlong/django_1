# -*- coding: utf-8 -*-
# __author__:花衬衫
# 2022/3/28 16:48
from django.http import HttpResponse
from django.shortcuts import render

# def hello(request):
#     return HttpResponse("Hello world ! ")
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, HttpResponse
from TestModel.My_Forms import EmpForm
from TestModel import models
from django.core.exceptions import ValidationError
# Create your views here.

def runoob(request):
    print("======   ")
    context          = {}
    context['hello'] = 'Hello World!'
    return render(request, 'runoob.html', context)

    # views_list = ["菜鸟教程1", "菜鸟教程2", "菜鸟教程3"]
    # return render(request, "runoob.html", {"views_list": views_list})

def runroob2(request):
    name = request.body
    print(name)
    return HttpResponse('')


def add_emp(request):
    if request.method == "GET":
        form = EmpForm()
        return render(request, "add_emp.html", {"form": form})
    else:
        form = EmpForm(request.POST)
        if form.is_valid():  # 进行数据校验
            # 校验成功
            data = form.cleaned_data  # 校验成功的值，会放在cleaned_data里。
            data.pop('r_salary')
            print(data)

            models.Emp.objects.create(**data)
            return HttpResponse(
                'ok'
            )
            # return render(request, "add_emp.html", {"form": form})
        else:
            print(form.errors)    # 打印错误信息
            clean_errors = form.errors.get("__all__")
            print(222, clean_errors)
        return render(request, "add_emp.html", {"form": form, "clean_errors": clean_errors})
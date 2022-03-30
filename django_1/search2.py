# -*- coding: utf-8 -*-
# __author__:花衬衫
# 2022/3/29 9:56
# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.decorators import csrf


# 接收POST请求数据
def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request, "post.html", ctx)
from time import mktime
from datetime import datetime

import pytz
from django.shortcuts import render, redirect
from .models import RSS as RSStable
from django.contrib import messages
from django.http import QueryDict
from django.contrib.auth.decorators import login_required
from django.http import Http404


from .RSS import RSS


# Create your views here.


@login_required()
def index(request):
    """ 首页 """

    datas = RSStable.objects.filter(owner=request.user)
    rdata = {"datas": datas}

    if datas:
        rss = RSS(datas[0].link)
        rdata["rss"] = rss
        rdata["link"] = datas[0].link
        for e in rss.feed["entries"]:
            tz = pytz.timezone('Asia/Shanghai')
            dtime = datetime.fromtimestamp(mktime(e['updated_parsed']))
            bjdtime = dtime.astimezone(tz)
            e["created"] = bjdtime.strftime("%Y-%m-%d %X %Z")

    return render(request, 'index.html', rdata)


@login_required()
def link(request):
    """ feeds link """
    if request.method == "GET":
        # 获取links
        link = request.GET.get("url")

        print(link)
        rss = RSS(link)
        if rss.ok:
            datas = RSStable.objects.filter(owner=request.user)

            rdata = {"datas": datas, "rss": rss, "link": link}
            for e in rss.feed["entries"]:
                tz = pytz.timezone('Asia/Shanghai')
                dtime = datetime.fromtimestamp(mktime(e['updated_parsed']))
                bjdtime = dtime.astimezone(tz)
                e["created"] = bjdtime.strftime("%Y-%m-%d %X %Z")

            return render(request, 'index.html', rdata)

    elif request.method == "POST":
        # 添加links
        link = request.POST.get("link")

        oldRss = RSStable.objects.filter(link=link, owner=request.user)
        if oldRss:
            messages.error(request, "RSS已经存在")
            return redirect("index")

        rss = RSS(link)
        if rss.ok:
            rsstable = RSStable(link=link, title=rss.title)
            rsstable.owner = request.user
            rsstable.save()

            return redirect("index")
        else:
            messages.error(request, "不支持的RSS链接")

            return redirect("index")
    elif request.method == "DELETE":
        delete = QueryDict(request.body)
        print(1)
        link = delete["link"]
        rss = RSStable.objects.filter(link=link)
        rss.delete()

        return redirect("index")

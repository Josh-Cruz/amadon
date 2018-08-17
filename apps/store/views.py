# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect




def index(request):
    if request.method == 'POST':
        return redirect('/process/')
    return render(request, "store/index.html")


def process(request):
    if request.method == 'POST':
        item_map = {
            "robes": 39.99,
            "lightsaber": 1399.99,
            "holocron": 3999.99,
            "manuscript": 299.99,
                    }
        if not request.POST['item'] in item_map:
            print "nothign there...."
        else:
            item = item_map[request.POST['item']]
            count = float(request.POST['quantity'])
            request.session['order_total'] =  count * item
            if "item_count" not in request.session:
                request.session['item_count'] = int(count)
            else:
                request.session['item_count'] += int(count) 
            if "total" not in request.session:
                request.session['total'] = request.session['order_total']
            else:
                request.session['total'] += request.session['order_total']
        return redirect('/checkout/')
    else:
        return redirect('/')



def checkout(request):
    if request.method == 'POST' or "GET":
        return render(request, "store/checkout.html")

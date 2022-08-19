from django.shortcuts import render


def index(request):
    template = "base.html"
    context = {
        "page_obj": "page_obj",
        "values": "valu",
        "max_order": "max_order",
        "min_order": "min_order",
        "sum_order": "sum_order",
        "sum_cost": "sum_cost",
    }
    return render(request, template, context)

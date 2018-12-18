# all the api should be written here
from akf_app.model_form import getAggregate
from akf_app import model_form
from django.shortcuts import redirect, render
from akf_app.util import show_msg_dialog
from django.utils.html import format_html
from django.http import JsonResponse
import json


def get_aggregate(req):
    if req.method == 'GET':
        name = req.GET.get('name')
        type = req.GET.get('type')
        if type == 'district':
            if name != '' and name != None:
                rval = model_form.getAggregate(name, type)
                if rval == 0:
                    info = show_msg_dialog('info', 'no record found')
                    return render(req, 'aggregate.html', {'msg':format_html(info)})
                elif rval == -20:
                    error = show_msg_dialog('error', 'oops something went wrong')
                    return render(req, 'aggregate.html', {'msg':format_html(error)}) 
                elif rval != -20 and rval != None:
                    rval['region'] = type
                    rval['temp'] = rval.get(type)
                    print('success')
                    return JsonResponse(rval,safe=False)
#                     return render(req, 'aggregate.html', rval)
                     
        elif type == 'block':
            if name != '' and name != None:
                rval = model_form.getAggregate(name, type)
                if rval == 0:
                    info = show_msg_dialog('info', 'no record found')
                    return render(req, 'aggregate.html', {'msg':format_html(info)}) 
                elif rval == -20:
                    error = show_msg_dialog('error', 'oops something went wrong')
                    return render(req, 'aggregate.html', {'msg':format_html(error)})
                elif rval != -20 and rval != None:
                    rval['region'] = type
                    rval['temp'] = rval.get(type)
                    return JsonResponse(rval,safe=False)
#                     return render(req, 'aggregate.html', rval)
                 
        elif type == 'cluster':
            if name != '' and name != None:
                rval = model_form.getAggregate(name, type)
                if rval == 0:
                    info = show_msg_dialog('info', 'no record found')
                    return render(req, 'aggregate.html', {'msg':format_html(info)})
                elif rval == -20:
                    error = show_msg_dialog('error', 'oops something went wrong')
                    return render(req, 'aggregate.html', {'msg':format_html(error)}) 
                elif rval != -20 and rval != None:
                    rval['region'] = type
                    rval['temp'] = rval.get(type)
                    return JsonResponse(rval,safe=False)
#                     return render(req, 'aggregate.html', rval)
                 
        elif type == 'gram_panchayat':
            if name != '' and name != None:
                rval = model_form.getAggregate(name, type)
                if rval == 0:
                    info = show_msg_dialog('info', 'no record found')
                    return render(req, 'aggregate.html', {'msg':format_html(info)}) 
                elif rval == -20:
                    error = show_msg_dialog('error', 'oops something went wrong')
                    return render(req, 'aggregate.html', {'msg':format_html(error)}) 
                elif rval != -20 and rval != None:
                    rval['region'] = type
                    rval['temp'] = rval.get(type)
#                     return render(req, 'aggregate.html', rval)
                    return JsonResponse(rval,safe=False)
        else:
            error = show_msg_dialog('error', 'empty values sent')
            return render(req, 'aggregate.html', {'msg':format_html(error)})           

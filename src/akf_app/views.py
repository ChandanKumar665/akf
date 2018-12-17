from akf_app import model_form
from django.shortcuts import render, redirect
from django.utils.html import format_html
from akf_app.util import show_msg_dialog
from akf_app.util import getTable


def show(req):
    rval = model_form.index()
    if rval != -20 and rval != None:
        # displaying student data in table format
        table_html = getTable([
                                {'id':'student_table'},
                                {'header':[
                                            'District',
                                            'Block',
                                            'Cluster',
                                            'Name Of School',
                                            'Grama Panchayat',
                                            'Addition',
                                            'Subtraction',
                                            'Multiplication',
                                            'Division'
                                           ]
                                },
                                {'content':rval}
                            ])
        return render(req, 'index.html', {'student_data':format_html(table_html), 'msg':''})
    elif rval == -20:
        error = show_msg_dialog('error', 'oops something went wrong')
        return render(req, 'index.html', {'msg':format_html(error)})


def url_submit(req):
    if req.method == 'POST':
        req_url = req.POST.get('url')
        if req_url != '' and req_url != None:
            rval = model_form.url_submit_record(req_url)
            if rval == 1:
#                 success_msg = show_msg_dialog('success', 'Data stored successfully')
                return redirect('index')
            elif rval == -20:
                error = show_msg_dialog('error', 'oops something went wrong')
                return render(req, 'index.html', {'msg':format_html(error)})
            elif rval == -9:
                error = show_msg_dialog('error', 'invalid link')
                return render(req, 'index.html', {'msg':format_html(error)})
            elif rval == -3:
                error = show_msg_dialog('error', 'Empty values sent')
                return render(req, 'index.html', {'msg':format_html(error)})
        else:
            error = show_msg_dialog('error', 'looks an invalid link')
            return render(req, 'index.html', {'msg':format_html(error)})       

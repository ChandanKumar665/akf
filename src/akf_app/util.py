# All utility functions will be created here


def getTable(tablelist=[]):
    tableresult = ''
    _id = 'id='
    if tablelist == None:
        return tableresult
    for data in tablelist:
        if data.get('id'):
                _id += data.get('id')
                continue
        elif data.get('header'):
            tableresult += '<table class="table" ' + _id + '><thead class="thead-dark"></tr>'
            for item in data['header']:
                tableresult += '<th>' + item + '</th>'
            tableresult += '</tr></thead>'          
        elif data.get('content'):
            tableresult += '<tbody>'
            for obj in data['content']:
                tableresult += '<tr>'
                for x in obj.values():
                    tableresult += '<td>' + str(x) + '</td>'
                tableresult += '</tr>'    
            tableresult += '</tbody></table>'
                                
    return tableresult    


def dictfetchall(cursor):
#     d = cursor.description 
#     return [dict(zip([col[0] for col in d], row)) for row in cursor.fetchall()]
    i = 0
    j = 0
    dict_obj = ''
    result = []
    temlist = []
    col = cursor.description
    val = cursor.fetchall()
    while i < len(val):
        j = 0
        for obj in col:
            temlist.append((obj[0], val[i][j]))
            j += 1
        i += 1
        dict_obj = dict(temlist)
        result.append(dict_obj)
    return result    


def show_msg_dialog(type='success', body=''):
    if type == 'success':
        msg = '''
        <div class="alert alert-success alert-dismissible">
            <button type="button" class="close" data-dismiss="alert">&times;</button>
            <strong>Success! </strong>''' + body + '''
        </div>
        '''
        return msg
    elif type == 'error':
        msg = '''
        <div class="alert alert-danger alert-dismissible">
            <button type="button" class="close" data-dismiss="alert">&times;</button>
            <strong>''' + body + '''</strong>
        </div>'''
        return msg
    elif type == 'info':
        msg = '''
        <div class="alert alert-info alert-dismissible">
            <button type="button" class="close" data-dismiss="alert">&times;</button>
            <strong>''' + body + '''</strong>
        </div>
        '''
        return msg
    

# All the business logic should be written here for clean
# code and for effective readability of the application
from akf_app.models import Student_Report
from akf_app.util import dictfetchall
from django.db import connection
import urllib.request
import csv
import sys
from datetime import datetime, date


def index():
    query = '''
            select
                srp.id,
                gi.district,
                gi.block,
                gi.cluster,
                gi.gram_panchayat,
                srp.school_name,
                srp.addition,
                srp.subtraction,
                srp.product,
                srp.division
            from
                student_report as srp
            left join
                geo_information as gi
            on
                gi.id = srp.district_id                    
        '''
    try:
        # creating cursor object
        cursor = connection.cursor()
        # preparing the query
        cursor.execute(query)
        # converting to list of student_report object
        student_obj_list = dictfetchall(cursor)
        student_list = []
        for obj in student_obj_list:
            student_list.append({'district':obj['district'],
                                'block':obj['block'],
                                'cluster':obj['cluster'],
                                'school_name':obj['school_name'],
                                'gram_panchayat':obj['gram_panchayat'],
                                'addition':obj['addition'],
                                'subtraction':obj['subtraction'],
                                'product':obj['product'],
                                'division':obj['division']
                                })
        if len(student_list) >= 1:     
            return student_list
        return []
    except Exception as e:
        return -20
    finally:
        cursor.close()
        connection.close()
        
 
def get_distric_id(name=''):
    try:
        inner_query = 'select id from geo_information where district = %s'
        cursor = connection.cursor()
        cursor.execute(inner_query, [name])
        datalist = dictfetchall(cursor)
        if datalist[0] != None:
            d_id = datalist[0].get('id')
            return d_id 
    except Exception as e:
        print(e)
        return -20
    finally:
        cursor.close()
        connection.close()

            
def url_submit_record(req_url):
    row = []
    name = ''
    table = ''
    columns = ''
    try:
#         raw_url = req_url.replace('github.com', 'raw.githubusercontent.com')
        name = req_url.split('/')[-1]
        csv_file = urllib.request.urlopen(req_url).read().decode('utf-8').split('\n')
    #     parsing the csv data
        csv_data = csv.reader(csv_file)
    #     stroring all the csv file data in list
        for obj in csv_data:
            row.append(obj)
    except Exception as e:
        return -9        
#   storing the list data in db
    if name == 'boundaries.csv':
        table = 'geo_information'
        columns = ' (district,block,cluster,gram_panchayat,created_time,updated_time)'
        query = 'insert into ' + table + columns + ' values'
        data = []
        for obj in row[1:len(row) - 1]:
            query += '(%s,%s,%s,%s,%s,%s),';
            data.append(obj[0])
            data.append(obj[1])
            data.append(obj[2])
            data.append(obj[3])
            data.append(datetime.utcnow())
            data.append(datetime.utcnow())
        final_query = query[0:len(query) - 1]
        try:
            cursor = connection.cursor()
            cursor.execute(final_query, data)
            if cursor.rowcount >= 1:
                # means data has been inserted successfully
                return 1
            else:
                return 0
        except Exception as e:
            print(e)
            return -20
        finally:
            cursor.close()
            connection.close()            
    elif name == 'gp_contests.csv':
        table = 'student_report'
        columns = ' (school_name,addition,subtraction,product,division,district_id,created_time,updated_time)'
        query = 'insert into ' + table + columns + ' values'
        data = []
        for obj in row[1:len(row) - 1]:
            query += '(%s,%s,%s,%s,%s,%s,%s,%s),'
            district_id = get_distric_id(obj[0])
            data.append(obj[3])
            data.append(obj[5])
            data.append(obj[6])
            data.append(obj[7])
            data.append(obj[8])
            data.append(district_id)
            data.append(datetime.utcnow())
            data.append(datetime.utcnow())
        final_query = query[0:len(query) - 1] 
        try:
            cursor = connection.cursor()
            cursor.execute(final_query, data)
            if cursor.rowcount >= 1:
                # means data has been inserted successfully
                return 1
            else:
                return 0
            
        except Exception as e:
            print(e)
            return -20
        finally:
            cursor.close()
            connection.close()
    else:
        return -9 

 
def getAggregate(name='', type=''):
    if name != '' and type != '':
        query = '''select 
                        {},
                        cast(avg(sr.addition) as char)as avg_addition,
                        cast(avg(sr.subtraction) as char)as avg_sub,
                        cast(avg(sr.product)as char)as avg_mult,
                        cast(avg(sr.division)as char)as avg_div  
                    from 
                        student_report as sr
                    left join
                        geo_information as gi
                    on
                        gi.id = sr.district_id
                    where
                       {} = %s
                    group by 
                        {}
                '''.format(type, type, type)
        data = [name]
        try:
            cursor = connection.cursor()
            cursor.execute(query, data)
            if cursor.rowcount == 1:
                datalist = dictfetchall(cursor)
                if datalist[0] != None:
                    return datalist[0]
            else:
                return 0
        except Exception as e:
            print(e)
            return -20
        finally:
            cursor.close()
            connection.close()    
    else:
        return -9
             

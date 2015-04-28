from django.shortcuts import render
from django.shortcuts import HttpResponse   
from django.template import RequestContext  #getting request context in your templates.
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from lxml import etree
from lxml import html

from textblob import Word
from collections import OrderedDict
from django.utils import simplejson

import jsonpickle   
import newspaper    #extract the newspaper article.
import csv  #import for read and write the csv

import urllib2  ##for fetching thr urls version two
import urllib   #for fetching thr urls version one 
 
import time
import csv      # for read and write the csv file
import json 

# Create your views here.

def first_page(request):     
    return render_to_response('pin_app/search_pincode.html')

def search_pincode(request):
    total_search =[]
    f = open('all_india_pin_code.csv', 'rb')
    reader = csv.reader(f)
    if request.method == 'GET':
        pin_requested = request.GET.get('pin_text')
        for row in reader:
            if pin_requested in row:
                
                office_name = row[0]
                pincode = row[1]
                office_type = row[2]
                deliverystatus = row[3]
                divisionname = row[4]
                regionname = row[5]
                circlename = row[6]
                taluk = row[7]
                districtname = row[8]
                statename = row[9]
                total_search.append({'office_name':office_name, 'pincode':pincode , 'office_type':office_type,\
                                     'deliverystatus':deliverystatus,'divisionname':divisionname,\
                                     'regionname':regionname,'circlename':circlename,'taluk':taluk,\
                                     'districtname':districtname,'statename':statename})
#                 total_search.append(row)
    
    context_dict = {'total_search':total_search}
    
    return render_to_response('pin_app/search_pincode.html',context_dict,context_instance=RequestContext(request))

def add_entry(request):
    f = open('all_india_pin_code.csv', 'rb')
    reader = csv.reader(f)
    if request.method == 'GET':
        data = request.GET.get('check_dict')
        json_data = json.JSONDecoder(object_pairs_hook=OrderedDict).decode(data)
        
        new_pin = json_data.get('data_add')
        
        total_search =[]

        for row in reader:
            
            if new_pin in row:
                
                office_name = row[0]
                pincode = row[1]
                office_type = row[2]
                deliverystatus = row[3]
                divisionname = row[4]
                regionname = row[5]
                circlename = row[6]
                taluk = row[7]
                print taluk
                districtname = row[8]
                statename = row[9]
                total_search.append({'office_name':office_name, 'pincode':pincode , 'office_type':office_type,\
                                     'deliverystatus':deliverystatus,'divisionname':divisionname,\
                                     'regionname':regionname,'circlename':circlename,'taluk':taluk,\
                                     'districtname':districtname,'statename':statename})
#                 total_search.append(row)
    
    context_dict_new = {'total_search':total_search}
    updated_new = jsonpickle.encode(context_dict_new)
    print updated_new
    return HttpResponse(updated_new,content_type="application/json")

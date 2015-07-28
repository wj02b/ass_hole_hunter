#!/usr/bin/env python
#coding=utf-8

#from libs.Threads import ThreadPool
#from libs.color import *
#import libs.socks as socks
import urllib2
import random
import time
import re
import os


def url_head(url):
    try:
        resp = req.head(url)
    except KeyboardInterrupt:
        raise
    except Exception,e:
        resp = None
    return resp

def url_get(url):
    return urllib2.urlopen(url)

def url_Get(req,url,**kwargs):
    """ 
    HTTP GET REQUESTS.
    """
    try:
        resp = req.get(url,**kwargs)

    except KeyboardInterrupt:
        raise

    except Exception, e:
        resp = None
    return resp



def url_post(url,value):
    data = urllib.urlencode(value)
    headers = { 'User-Agent' : 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/31.0.1271.64 Safari/537.11' }
    res = urllib2.Request(url,data,headers)
    try:
        resp = urllib2.urlopen(res)
    except:
        resp = None
    return resp

def url_upload(url,value):
    cookies = cookielib.CookieJar()
    opener  = urllib2.build_opener(urllib2.HTTPCookieProcessor(cookies),MultipartPostHandler.MultipartPostHandler)
    opener.open(url, value)

def url_proxy(url,port_type):
    if port_type=="http":
        proxy_port = xxx
    else:
        proxy_port = xxx    
    conn = httplib.HTTPConnection(proxy_host, proxy_port)
    resp = conn.getresponse()
    if resp.status == 200:
        resp = resp.read()
    else:
        resp = None
    return resp


def key_find(url,value):
    return re.findall(url,value)


def run_payload(payload,arr):
    if len(payload) > 0 and payload != None:
        color.echo("Start exploit...",RED)
        #code=open("modules/"+payload+".py").read()
        #exec(code)
        #module_path = os.path.join("modules",payload+".py")
        #sys.path.append(module_path)
        #plugin_info, resp = 
        plugin=__import__("modules."+payload, fromlist=[payload])
        plugin.exploit(arr)

#!/usr/bin/python
print '\r'
print 'Spuddle - Anonymous Traffic Sender (made by Fanis Siampos)'
print ' _______  _______  __   __  ______   ______   ___      _______ '
print '|       ||       ||  | |  ||      | |      | |   |    |       |'
print '|  _____||    _  ||  | |  ||  _    ||  _    ||   |    |    ___|'
print '| |_____ |   |_| ||  |_|  || | |   || | |   ||   |    |   |___ '
print '|_____  ||    ___||       || |_|   || |_|   ||   |___ |    ___|'
print ' _____| ||   |    |       ||       ||       ||       ||   |___ '
print '|_______||___|    |_______||______| |______| |_______||_______|'
                                                               
from bs4 import BeautifulSoup 
import urllib2
import urllib
import sys
import time
import random
import re
import os

useragent = ['Mozilla/4.0 (compatible; MSIE 5.0; SunOS 5.10 sun4u; X11)',
		   'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.2.2pre) Gecko/20100207 Ubuntu/9.04 (jaunty) Namoroka/3.6.2pre',
		   'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Avant Browser;',
		   'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT 5.0)',
		   'Mozilla/4.0 (compatible; MSIE 7.0b; Windows NT 5.1)',
		   'Mozilla/5.0 (Windows; U; Windows NT 6.0; en-US; rv:1.9.0.6)',
		   'Microsoft Internet Explorer/4.0b1 (Windows 95)',
		   'Opera/8.00 (Windows NT 5.1; U; en)',
		   'amaya/9.51 libwww/5.4.0',
		   'Mozilla/4.0 (compatible; MSIE 5.0; AOL 4.0; Windows 95; c_athome)',
		   'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',
		   'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
		   'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.0; ZoomSpider.net bot; .NET CLR 1.1.4322)',
		   'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; QihooBot 1.0 qihoobot@qihoo.net)',
		'Mozilla/4.0 (compatible; MSIE 5.0; Windows ME) Opera 5.11 [en]']
		
print '\r'
link_invation = raw_input("Enter the URL that you want to visit anonymously: ")
print '\r'
referer = raw_input("Enter a Referer URL (optional): ")
print '\r'
cookie = raw_input("Enter a Cookie (optional): ")
print '\r'



timeset = time.strftime("%d-%m-%Y")


try: 
  print 'Retrieving Proxy List ...'
  print '\r'
  
  
  pagex = urllib2.urlopen('http://checkerproxy.net/' + timeset).read()
  soupx = BeautifulSoup(pagex)
  spansx = soupx.find_all('li', text=True)
 
  
  
  
  
  for spanx in spansx:
    try:
      xx = spanx.get_text().strip()
      print "Identity Used:",xx.split(":")[0]
      proxyx = urllib2.ProxyHandler({'http':xx})
      openerx = urllib2.build_opener(proxyx)
      openerx.addheaders = [('User-agent', random.choice(useragent)),
						('Referer', referer), ('Accept-Encoding', 'gzip,deflate')]
      urllib2.install_opener(openerx)
      fx=urllib2.urlopen(link_invation,timeout=20)
    
      if link_invation in fx.read():
         print "[*] URL Visited Successfully ..."
         print "\r"
      else:
         print "[*] Failure on Visit ..."
         print "\r"
    except:
      print "[!] Proxy Error or Connection Timeout"
      print "\r"
      pass
      
except:
  print "[!] Unexpected Error. Please Wait ..."
  print "\r"




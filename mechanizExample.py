#!/usr/bin/python
# -*- coding: utf-8 -*-

#a simple example with mechanize for python

import mechanize #pip install mechanize
import cookielib
              

def myPage(myUrl):
    # create a new mechanize Browser
    browser = mechanize.Browser()
    
    # Cookie Jar (to stock cookies if you want to make an autentification
    #for example)
    cj = cookielib.LWPCookieJar()
    browser.set_cookiejar(cj)
    
    # Browser options
    browser.set_handle_equiv(True)
    browser.set_handle_gzip(True)
    browser.set_handle_redirect(True)
    browser.set_handle_referer(True)
    browser.set_handle_robots(False)
    
    # Follows refresh 0 but not hangs on refresh > 0
    browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)
    
    # enable debug messages, just uncomment to enable
    #browser.set_debug_http(True)
    #browser.set_debug_redirects(True)
    #browser.set_debug_responses(True)
    
    # User-Agent (cause some website doesn't respond to python default user agent)
    browser.addheaders = [('User-agent', 'Mozilla/5.0 (Windows NT 5.1; rv:9.0.1) Gecko/20100101 Firefox/9.0.1')]
    
    #disable proxy (intranet access)
    browser.set_proxies(proxies={}) 
   
    #open url
    req = browser.open(myUrl)
    
    #select login form
    browser.select_form(name = 'login')
    
    #fill login form and submit
    browser.form['user']='me'
    browser.form['passwd']='mypass'
    browser.submit()
    
    #return page content
    return browser.response().read()
    
def usage(argv):
    print "Usage : " + argv[0] + " <your url here>"

def main():
    #test if we have an argument, else display usage and exit
    if len(sys.argv) != 2:
        usage(sys.argv)
        exit(0)
    else:
        myUrl = sys.argv[1]   
    
    myPage = getMyUrl(myUrl)

if __name__ == "__main__":
    main()

#!/usr/bin/env python
'''
"THE FINLAYDAG33K LICENSE" (Revision 2), Based on the "BEERWARE LICENSE":
<Aroop "FinlayDaG33k" Roelofs> wrote this file.
As long as you retain this notice you can do whatever you want with this stuff.
If we meet some day, you should buy me a drink.
Hugs are mandatory when meeting me!
Aroop "FinlayDaG33k" Roelofs Can NOT be held liable for any damages done!
'''
import urllib2
import re

CFAPI_ZONE = "" # Paste your Zone ID here
CFAPI_DOMAIN_TYPE = "" # Paste your Domain Type here (A, CNAME etc.)
CFAPI_DOMAIN_NAME = "" # Paste your Domain you want to edit (for example `www.finlaydag33k.nl`)
CFAPI_EMAIL = "" # Paste your account email here
CFAPI_KEY = "" # paste your Global API Key here


def get_external_ip():
    site = urllib2.urlopen("http://checkip.dyndns.org/").read()
    grab = re.findall('([0-9]+\.[0-9]+\.[0-9]+\.[0-9]+)', site)
    address = grab[0]
    return address

updateURL = "https://api.cloudflare.com/client/v4/zones/" +CFAPI_ZONE + "/dns_records?type="+ CFAPI_DOMAIN_TYPE + "&name=" + CFAPI_DOMAIN_NAME + "&content=" + get_external_ip()
req = urllib2.Request(updateURL)
req.add_header('X-Auth-Email', CFAPI_EMAIL)
req.add_header('X-Auth-Key', CFAPI_KEY)
resp = urllib2.urlopen(req)
content = resp.read()
### Still gonna do some checks here later, but the basic functionality is there!

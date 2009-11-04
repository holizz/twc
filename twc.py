#!/usr/bin/env python

import json
import re
import sys
import urllib2

friends = 'http://twitter.com/friends/ids.json?screen_name=%s'
followers = 'http://twitter.com/followers/ids.json?screen_name=%s'
show = 'http://twitter.com/users/show.json?user_id=%s'

def get(f, u):
    return set(json.load(urllib2.urlopen(f%u)))

def to_screen_name(u):
    return json.load(urllib2.urlopen(show%u))['screen_name']

if len(sys.argv) == 1:
    print """Examples:
twc followers@holizz \& friends@holizz
twc 'followers@holizz | followers@harrym | followers@dextrousweb'"""
else:
    args = " ".join(sys.argv[1:])

    args = re.sub('(\w+)@(\w+)', 'get(\\1,"\\2")', args)

    exec("users = "+args)

    sys.stderr.write("Total: %s\n" % len(users))

    for u in users:
        print to_screen_name(u)

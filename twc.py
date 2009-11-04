#!/usr/bin/env python

import json
import sys
import urllib2

friends = 'http://twitter.com/friends/ids.json?screen_name=%s'
followers = 'http://twitter.com/followers/ids.json?screen_name=%s'
show = 'http://twitter.com/users/show.json?user_id=%s'

def get(f, u):
    return set(json.load(urllib2.urlopen(f%u)))

def to_screen_name(u):
    return json.load(urllib2.urlopen(show%u))['screen_name']


users = get(friends,'holizz') & get(followers,'holizz')

sys.stderr.write("Total: %s\n" % len(users))

for u in users:
    print to_screen_name(u)

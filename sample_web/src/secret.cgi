#!/usr/bin/env python2.7

print "Content-Type: text/plain"
print

import re
import cgi

note_id = cgi.FieldStorage()["note_id"].value
assert re.match(r'[0-9a-f]+\Z', note_id)

mydir = '/opt/ctf/sample_web/rw/';
with open(mydir + note_id, 'r') as f:
    print f.read()

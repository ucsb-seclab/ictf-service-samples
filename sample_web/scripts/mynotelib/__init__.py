# This "library" is how we interact with the service
# You could have something more complicated here :)

import re
import requests

class WrongPassword(Exception):
    pass

def read_note(ip, port, note_id, password):
    # We read that note, knowing the password (in other words, we're benign traffic)
    # Whatever the patch, this must still work!
    r = requests.post('http://'+ip+':'+str(port)+'/read.php', data={
        'note_id': note_id,
        'password': password,
        })

    # You should now verify that the request was successful...
    assert r.status_code == 200

    # ... and give us the flag (we'll make sure the value is correct)
    if re.search(r'Wrong password', r.text):
        raise WrongPassword
    m = re.search(r'Your note was: ([A-Za-z0-9]+)', r.text)
    return m.group(1)


def write_note(ip, port, content, password):
    # We create a new note with the specified password and content
    # Returns the assigned note_id
    r = requests.post('http://'+ip+':'+str(port)+'/write.php', data={
        'password': password,
        'content': content,
        })

    # You should now verify that the request was successful...
    assert r.status_code == 200
    assert re.search(r'Your note is safe with us', r.text)

    # ... and get the flag_id and token, if the service is in charge of generating them 
    # In this example, we need to get the flag_id ("note ID" in this example).
    m = re.search(r'this note ID: ([0-9a-f]+)', r.text)
    return m.group(1)

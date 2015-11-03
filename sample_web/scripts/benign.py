# In this example, we use a (rather stupid) library to interact with the service
from mynotelib import *
import random
import string
# To create random strings
POSSIBILITIES = string.ascii_uppercase + string.digits + string.ascii_lowercase

def benign(ip, port):
    # There should be some other benign traffic to your service.
    # It helps determine if the service is functional or not, and makes it
    # harder to fingerprint flag-related traffic.
    #
    # In this case, I was lazy and I'm just creating a dummy note.

    password = ''.join(random.choice(POSSIBILITIES) for x in range(20))
    content = ''.join(random.choice(POSSIBILITIES) for x in range(20))
    while True: # Safety over all :D
        wrong_password = ''.join(random.choice(POSSIBILITIES) for x in range(20))
        if wrong_password != password: break

    # Let's write it...
    note_id = write_note(ip, port, content, password)

    # And let's check that we can read it...
    assert read_note(ip, port, note_id, password) == content

    # ... but just with the right password (in normal operation)
    # Note that we interpret _any_ exception as a sign that the service is not behaving correctly.
    # In this case, the WrongPassword exception is in fact expected.
    try:
        read_note(ip, port, note_id, wrong_password)
        raise "WTF? Notes can be read with wrong passwords even without vulnerabilities?"
    except WrongPassword:
        # All is good! Let's not pass this exception to the checking code
        pass

    # Nothing to return, if we got here without exceptions we assume that everything worked :)

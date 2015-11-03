# In this example, we use a (rather stupid) library to interact with the service
from mynotelib import write_note

import random
import string

# To create random strings
POSSIBILITIES = string.ascii_uppercase + string.digits + string.ascii_lowercase

def set_flag(ip, port, flag):
    # We create a new note with the flag as content

    # Note that in this example the _service_ generates the flag_id (note_id).
    # We still generate the token (password) ourselves.
    password = ''.join(random.choice(POSSIBILITIES) for x in range(20))
    content = flag

    # You should verify that the request was successful and get the flag_id and token, if the service is in charge of generating them
    # (The "library" does that for us, in this case.)
    note_id = write_note(ip, port, content, password)

    return {
            'FLAG_ID': note_id,
            'TOKEN': password,  # benign (get_flag) will know this, exploits will not
            }

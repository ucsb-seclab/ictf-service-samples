# In this example, we use a (rather stupid) library to interact with the service
from mynotelib import read_note

def get_flag(ip, port, flag_id, token):
    # We read that note, knowing the password (in other words, we're benign traffic)
    # Whatever the patch, this must still work!
    note_id = flag_id
    password = token

    # You should verify that the request was successful.
    # (The "library" does that for us, in this case.)
    content = read_note(ip, port, note_id, password)

    # And give us the flag (we'll make sure the value is correct)
    return { 'FLAG': content }

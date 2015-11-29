import random
import string
import socket
import sys
import pexpect
import pexpect.fdpexpect

# To create random strings
POSSIBILITIES = string.ascii_uppercase + string.digits + string.ascii_lowercase

def set_flag(ip, port, flag):
    # We create a new note with the flag as content
    note_id = random.randint(0,4294967295) # Well, hopefully should not collide
    password = ''.join(random.choice(POSSIBILITIES) for x in range(20))
    content = flag

    # Interaction with the service
    # Try to be robust, services will not always answer immediately
    conn = socket.create_connection((ip,port))
    c = pexpect.fdpexpect.fdspawn(conn.fileno())

    c.expect("Hi! Welcome to our note storage service")
    c.expect("Want to \(R\)ead or \(W\)rite a note?") # Note: these are RegExps!

    c.sendline("W")

    c.expect("Please type: note_id password content")
    c.expect("The note_id is an number. No extra whitespace!")
    c.sendline("{} {} {}".format(note_id, password, content))

    c.expect("Your note is safe with us! Bye!")
    c.close()
    conn.close()

    return {
            'FLAG_ID': note_id, # Unique id for each flag
            'TOKEN': password,  # benign (get_flag) will know this, exploits will not
            }


if __name__ == "__main__":
    print set_flag("127.0.0.1", 6666, sys.argv[1] if len(sys.argv)>1 else "FLG1234567890")

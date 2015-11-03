import random
import string
import socket
import sys
import pexpect
import pexpect.fdpexpect

# To create random strings
POSSIBILITIES = string.ascii_uppercase + string.digits + string.ascii_lowercase

def benign(ip, port):
    # There should be some other benign traffic to your service.
    # It helps determine if the service is functional or not, and makes it
    # harder to fingerprint flag-related traffic.
    #
    # In this case, I was lazy and I'm just creating a dummy note.

    note_id = random.randint(0,4294967295) # Well, hopefully should not collide
    password = ''.join(random.choice(POSSIBILITIES) for x in range(20))
    content = ''.join(random.choice(POSSIBILITIES) for x in range(20))

    if ip:
        conn = socket.create_connection((ip,port))
        c = pexpect.fdpexpect.fdspawn(conn.fileno())
    else:
        # Makes it easier to test locally
        c = pexpect.spawn("../src/sample_py")
        c.logfile = sys.stdout
    c.expect("Hi! Welcome to our note storage service")
    c.expect("Want to \(R\)ead or \(W\)rite a note?")
    c.sendline("W")
    c.expect("Please type: note_id password content")
    c.expect("The note_id is an number. No extra whitespace!")
    c.sendline("{} {} {}".format(note_id, password, content))
    c.expect("Your note is safe with us! Bye!")
    c.close()
    if ip: conn.close()

    while True: # Safety over all :D
        wrong_password = ''.join(random.choice(POSSIBILITIES) for x in range(20))
        if wrong_password != password: break
    if ip:
        conn = socket.create_connection((ip,port))
        c = pexpect.fdpexpect.fdspawn(conn.fileno())
    else:
        # Makes it easier to test locally
        c = pexpect.spawn("../src/sample_py")
        c.logfile = sys.stdout
    c.expect("Hi! Welcome to our note storage service")
    c.expect("Want to \(R\)ead or \(W\)rite a note?")
    c.sendline("R")
    c.expect("Please type: note_id password");
    c.sendline("{} {}".format(note_id, wrong_password))
    c.expect("Wrong password!")
    c.close()
    if ip: conn.close()
    
    if ip:
        conn = socket.create_connection((ip,port))
        c = pexpect.fdpexpect.fdspawn(conn.fileno())
    else:
        # Makes it easier to test locally
        c = pexpect.spawn("../src/sample_py")
        c.logfile = sys.stdout
    c.expect("Hi! Welcome to our note storage service")
    c.expect("Want to \(R\)ead or \(W\)rite a note?")
    c.sendline("R")
    c.expect("Please type: note_id password")
    c.sendline("{} {}".format(note_id, password))
    c.expect("Note content: ")
    retrieved_content = c.readline().strip()
    assert content == retrieved_content
    c.close()
    if ip: conn.close()

    # Nothing to return, if we got here without exceptions we assume that everything worked :)


if __name__ == "__main__":
    benign(None, None)

import socket
import sys
import pexpect
import pexpect.fdpexpect

def get_flag(ip, port, flag_id, token):
    # We read that note, knowing the password (in other words, we're benign traffic)
    # Whatever the patch, this must still work!
    note_id = flag_id
    password = token

    # Interaction with the service
    # Try to be robust, services will not always answer immediately
    if ip:
        conn = socket.create_connection((ip,port))
        c = pexpect.fdpexpect.fdspawn(conn.fileno())
    else:
        # Makes it easier to test locally
        c = pexpect.spawn("../src/sample_py")
        c.logfile = sys.stdout

    c.expect("Hi! Welcome to our note storage service")
    c.expect("Want to \(R\)ead or \(W\)rite a note?") # Note: these are RegExps!

    c.sendline("R")

    c.expect("Please type: note_id password")
    c.sendline("{} {}".format(note_id, password))

    c.expect("Note content: ")
    content = c.readline().strip()
    c.close()
    if ip: conn.close()

    return { 'FLAG': content }


if __name__ == "__main__":
    print get_flag(None, None, sys.argv[1], sys.argv[2])

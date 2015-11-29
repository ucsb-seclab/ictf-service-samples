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
    conn = socket.create_connection((ip,port))
    c = pexpect.fdpexpect.fdspawn(conn.fileno())

    c.expect("Hi! Welcome to our note storage service")
    c.expect("Want to \(R\)ead or \(W\)rite a note?") # Note: these are RegExps!

    c.sendline("R")

    c.expect("Please type: note_id password")
    c.sendline("{} {}".format(note_id, password))

    c.expect("Note content: ")
    c.expect("\n"); content = c.before.strip()
    c.close()
    conn.close()

    return { 'FLAG': content }


if __name__ == "__main__":
    print get_flag("127.0.0.1", 6666, sys.argv[1], sys.argv[2])

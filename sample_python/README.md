This is a sample service written in Python. Feel free to use it as starting point for your code :)

Run `make` to create a bundle you can submit.


Files
=====

  - `service/`: the service meat -- only these files get on the VM and are seen by players, put in everything that is needed!
  - `scripts/`: benign functionality for your service (flag setting / retrieval), and exploit samples.
  - `src/`: submit this as your source (note: this is just for organizers' reference).


Recommendations for Python
==========================

Same deal as in C, flush your output buffers and make sure you read all data!

Either do `sys.stdout.flush()` or reopen stdout specifying it should not be buffered (`os.fdopen(sys.stdout.fileno(), 'w', 0)`).
Input is best done in full lines.

Alternatively, use `socket.fromfd()`, `sendall()`, and loop around `recv()` until you receive a terminator. `pwntools`' tubes (or `pexpect`) may be useful. If necessary, you can also use `shutdown()` and `setsockopt()` (see `man tcp`).

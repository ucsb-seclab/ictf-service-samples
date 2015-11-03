This is a sample web service. Feel free to use it as starting point for your code :)

Same deal as the others, but different languages.
The benign functionality is in PHP. The "secret" exploit command is a Python CGI program. Note that CGI programs can be anything that is executable.
The flag and exploit scripts use `requests` and `pwntools`, and a "fake" library.

Run `make` to create a bundle you can submit.


Files
=====

  - `service/`: the service meat -- only these files get on the VM and are seen by players, put in everything that is needed!
  - `scripts/`: benign functionality for your service (flag setting / retrieval), and exploit samples.
  - `src/`: submit this as your source (note: this is just for organizers' reference).


Recommendations for web services
================================

To keep things simple, we are _not_ providing a separate database service. All data must go in the `rw` directory, and is handled directly by each service.

You can either create separate files (like in this example) or use SQLite or any format of your choice.
As usual, be sure to handle multiple access in a sane way (for SQLite, see https://www.sqlite.org/faq.html#q5).

If you use CGI, you should also read this file for the "bare" C and Python samples.

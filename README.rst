================
stackoverflow.py
================

stackoverflow.py is a simple command line script to fetch the first
answer from the first stackoverflow page found for a given query.

Exemple::
    $ stackoverflow.py python get machine hostname
    http://stackoverflow.com/questions/8263192/python-on-linux-get-host-name-in-etc-hostname
    http://stackoverflow.com/questions/4271740/how-can-i-use-python-to-get-the-system-hostname
    http://stackoverflow.com/questions/166506/finding-local-ip-addresses-using-pythons-stdlib

                Try os.uname().  According to the doc, it is the second position in the tuple returned.

    But, as the doc itself states, the "better way to get the hostname is socket.gethostname() or even socket.gethostbyaddr(socket.gethostname())."

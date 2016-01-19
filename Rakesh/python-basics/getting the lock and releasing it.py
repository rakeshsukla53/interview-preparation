
import threading

# Make a lock
lock = threading.Lock()

# old-way to use a lock

lock.acquire()

try:
    print "Critical Section 1"
    print "Critical Section 2"
finally:
    lock.release()

# New way to do in Python

with lock:  # this is amazing context-managers
    print "Critical Section 1"
    print "Critical Section 2"


with ignored(OSError):
    os.remoe(.....)

# rather than using try and except block you can use ignore































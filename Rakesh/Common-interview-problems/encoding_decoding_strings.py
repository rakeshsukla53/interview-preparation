__author__ = 'rakesh'

#logic jus make sure you have end keyword after after word, and then do accordingly

def encode(strs):
    return ''.join(s.replace('|', '||') + ' | ' for s in strs)

def decode(s):
    return [t.replace('||', '|') for t in s.split(' | ')[:-1]]



print encode('Rakesh Ranjan Sukla')

print decode('R | a | k | e | s | h |   | R | a | n | j | a | n |   | S | u | k | l | a |')


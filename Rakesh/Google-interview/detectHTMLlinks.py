__author__ = 'rakesh'

import re

N = input()

for line in range(N):

    html = raw_input()
    match = re.search(r'href=[\'"]?([^\'" >]+)', html)
    firstString = re.search(r'href=(.*)</a>', html)
    match1 = re.search(r'">(.*)</a>', firstString.group())

    if match:

        print match.group().split('href="')[1],match1.group().split('">')[1].split('</a>')[0]



'''
r'...' is a "raw" string. It stops you having to worry about escaping characters quite as much as you normally would. (\ especially -- in a raw string a \ is just a \. In a regular string you'd have to do \\ every time, and that gets old in regexps.)

"href=[\'"]?" says to match "href=", possibly followed by a ' or ". "Possibly" because it's hard to say how horrible the HTML you're looking at is, and the quotes aren't strictly required.

Enclosing the next bit in "()" says to make it a "group", which means to split it out and return it separately to us. It's just a way to say "this is the part of the pattern I'm interested in."

"[^\'" >]+" says to match any characters that aren't ', ", >, or a space. Essentially this is a list of characters that are an end to the URL. It lets us avoid trying to write a regexp that reliably matches a full URL, which can be a bit complicated.
'''







__author__ = 'rakesh'


def isAnagram(s, t):

    if sorted(s) == sorted(t):

        return True

    else:

        return False


print isAnagram("car", "tar")





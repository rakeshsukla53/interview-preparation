__author__ = 'rakesh'

def generateParenthesis(n):
    def generate(p, left, right, parens=[]):
        if left: generate(p + '(', left - 1, right)
        if right > left: generate(p + ')', left, right - 1)
        if not right: parens += p,
        return parens
    return generate('', 3, 3)

generateParenthesis(3)

#this method is absolutely amazing



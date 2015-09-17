__author__ = 'rakesh'

N = raw_input()

phoneNumbers = []

for i in range(int(N)):

    phone = raw_input()

    if len(phone) == 10:
        phoneNumbers.append(int(phone))

    if len(phone) > 10:
        phone = phone[len(phone) - 10:]
        phoneNumbers.append(int(phone))

def wrapper(func):

    newPhone = func(phoneNumbers)

    newPhone = map(str, newPhone)
    for i in newPhone:

        print "+91" + " " + i[0:5] + " " + i[5:]

@wrapper
def sortPhone(phoneNumbers):

    phoneNumbers.sort()

    return phoneNumbers

#why we want to use decorators
# Decorators allow you to easily modify the output of a function without actually changing the function. You have to think about code-reuse, not jus about solving the problem.
#
# In this specific example, you might have two different decorators for normalising the phone numbers in two different formats, but you would not need to change your "sorting" function or any other phone number function you might have.
#
# If you think about it from HTML, you might have a decorator that puts "{}" around the output from a function, and another one that puts "{}" around the output. That way to make the output of a function bold you would just have to put the [@bold](/bold) decorator at the beginning of the function.



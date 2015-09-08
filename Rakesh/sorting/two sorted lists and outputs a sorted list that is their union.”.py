__author__ = 'rakesh'

#Write a function that takes in two sorted lists and outputs a sorted list that is their union.

def answer(list1, list2):

    len1 = len(list1)
    len2 = len(list2)

    final_list = []
    j = 0
    k = 0

    for i in range(len1+len2):

        if k == len1:
            final_list.append(list2[j])
            j += 1
            continue

        if j == len2:
            final_list.append(list1[k])
            k += 1
            continue

        if list1[k] < list2[j]:
            final_list.append(list1[k])
            k += 1

        else:
            final_list.append(list2[j])
            j += 1

    return final_list


print answer([1, 2 , 17, 18, 100, 101, 102, 104, 105, 106, 10000], [3, 3, 4, 5, 15, 19, 20, 101, 2002, 20203202])



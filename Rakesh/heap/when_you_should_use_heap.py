
# Your book is wrong! As you demonstrate, a heap is not a sorted list (though a sorted list is a heap). What is a heap? To quote Skiena's Algorithm Design Manual
#
#     Heaps are a simple and elegant data structure for efficiently supporting the priority queue operations insert and extract-min. They work by maintaining a partial order on the set of elements which is weaker than the sorted order (so it can be efficient to maintain) yet stronger than random order (so the minimum element can be quickly identified).
#
# Compared to a sorted list, a heap obeys a weaker condition the heap invariant. Before defining it, first think why relaxing the condition might be useful. The answer is the weaker condition is easier to maintain. You can do less with a heap, but you can do it faster. A heap has three operations:
#
#     Find-Minimum is O(1)
#     Insert O(log n)
#     Remove-Min O(log n)
#
# Crucially Insert is O(log n) which beats O(n) for a sorted list.
#
# What is the heap invariant? "A binary tree where parents dominate their children". That is, "p ≤ c for all children c of p". Skiena illustrates with pictures and goes on to demonstrate the algorithm for inserting elements while maintaining the invariant. If you think a while, you can invent them yourself. (Hint: they are known as bubble up and bubble down)
#
# The good news is that batteries-included Python implements everything for you, in the heapq module. It doesn't define a heap type (which I think would be easier to use), but provides them as helper functions on list.
#
# Moral: If you write an algorithm using a sorted list but only ever inspect and remove from one end, then you can make the algorithm more efficient by using a heap.
#
# For a problem in which a heap data structure is useful, read https://projecteuler.net/problem=500
#

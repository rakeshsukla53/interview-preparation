__author__ = 'rakesh'

'''

This is a general, non-Python-specific answer.
Algorithmic complexity comparison

       | Hash Table  |   Red-Black Tree    |
-------+-------------+---------------------+
Space  | O(n) : O(n) | O(n)     : O(n)     |
Insert | O(1) : O(n) | O(log n) : O(log n) |
Fetch  | O(1) : O(n) | O(log n) : O(log n) |
Delete | O(1) : O(n) | O(log n) : O(log n) |
       | avg  :worst | average  : worst    |

The problem with hash tables is that hashes can collide. There are various mechanisms to resolve collisions, e.g. open addressing or separate chaining. The absolute worst case is that all keys have the same hash code, in which case a hash table will degrade into a linked list.

In all other cases, a hash table is a great data structure that's easy to implement and delivers good performance. A downside is that implementations that can quickly grow the table and redistribute their entries will likely waste nearly as much memory as is actually being used.

RB-Trees are self-balancing and do not change their algorithmic complexity in a worst case. However, they are more difficult to implement. Their average complexities are also worse than that of a hash table.
Restrictions on keys

All keys in a hash table must be hashable and comparable for equality among each other. This is especially easy for strings or integers, but is also fairly straightforward to extend to user-defined types. In some languages like Java these properties are guaranteed by definition.

Keys in an RB-Tree must have a total order: each key must be comparable with any other key, and the two keys must either compare smaller, greater, or equal. This ordering equality must be equivalent to semantic equality. This is straightforward for integers and other numbers, also fairly easy for strings (the order need only be consistent and not externally observable, so the order does not need to consider locales[1]), but difficult for other types that have no inherent order. It is absolutely impossible to have keys of different types unless some comparison between them is possible.

[1]: Actually, I'm wrong here. Two strings may not be byte-equal but still be equivalent according to the rules of some language. See e.g. Unicode normalizations for one example where two equal strings are encoded differently. Whether Unicode character composition matters for your hash key is something that a hash table implementation cannot know.

One might think that a cheap solution for RB-Tree keys would be to first test for equality, then compare identity (i.e. compare pointers). However, this ordering would not be transitive: If a == b and id(a) > id(c), then it must follow that id(b) > id(c) as well, which is not guaranteed here. So instead, we might use the hash code of keys as the lookup keys. Here, the ordering works correctly, but we might end up with multiple distinct keys with the same hash code, which will be assigned to the same node in the RB tree. To solve these hash collisions we can use separate chaining just like with hash tables, but this also inherits the worst case behaviour for hash tables – the worst of both worlds.
Other Aspects

    I expect to a hash table to have better memory locality than a tree, because a hash table is essentially just an array.

    Entries in both data structures have a fairly high overhead:
        hash table: key, value, and next entry pointer in the case of separate chaining. Also storing the hash code can speed up resizing.
        RB-tree: key, value, colour, left child pointer, right child pointer. Note that while colour is a single bit, alignment issues could mean you'd still be wasting enough space for nearly a whole pointer, or even nearly four pointers when only power-of-two sized memory blocks can be allocated. In any case, an RB-tree entry consumes more memory than a hash table entry.

    Insertions and deletions in an RB-tree involve tree rotations. These aren't really costly, but do involve an overhead. In a hash, insertion and deletion are no more expensive than a simple access (although resizing a hash table upon insertion is an O(n) endeavour).

    Hash tables are inherently mutable, whereas an RB-tree could also be implemented in an immutable fashion. However, this is rarely useful.

'''
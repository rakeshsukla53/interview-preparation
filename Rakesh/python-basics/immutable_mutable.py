#
#
# Immutable:
#
#     numbers: int, float, complex
#     immutable sequences: str, tuples, bytes, frozensets
#
# Mutable: everything else,
#
#     mutable sequences: list, byte array
#     set type: sets
#     mapping type: dict
#     classes, class instances
#     etc.
#
# And a trick is to use id()built-in function. For instance,
#
# Using on integer:
#
# >>> n = 1
# >>> id(n)
# **704
# >>> n += 1
# >>> n
# 2
# >>> id(n)
# **736
#
# Using on list:
#
# >>> m = [1]
# >>> id(m)
# **416
# >>> m.append(2)
# >>> m
# [1, 2]
# >>> id(m)
# **416
#

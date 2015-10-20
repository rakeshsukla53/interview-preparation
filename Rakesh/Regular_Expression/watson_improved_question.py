__author__ = 'rakesh'

from zlib import compress, decompress  # it is based on GNU zip

string = 'watson  Represents|watson represents|Watson represents a first step into cognitive systems, a new era of computing.|first step into  Cognitive|Cognitive Systems; a new era|what does watson represent'

print("Original length:", len(string))
compressed = compress(string)
print compressed
print("Compressed length:", len(compressed))
decompressed = decompress(compressed)
print("Decompressed is equal:", decompressed == string)


# calculate hash values of the given number and if the any of the number is not present in the hash table 
# we can definitely say that it is not in the set 
# there are two operations in bloom filters
# insert() and lookup()   
import math
import mmh3
from bitarray import bitarray

class BloomFilter(object):

    def __init__(self, num_items, fp_prob):
        # false positive probability in decimal
        self.fp_prob = fp_prob
        # calculate number of bitarray size using formula
        self.size_of_bitarray = self.get_size(num_items, fp_prob) 
        # calculate number of hash functions to use following formula
        self.num_hash = self.get_hash_count(self.size_of_bitarray, num_items)
        # initialize the bit array
        self.bit_array = bitarray(self.size_of_bitarray)
        # initialize to zero
        self.bit_array.setall(0)

    # function to add elements to hash functions
    def add(self, item):
        # calculate for each hash function values
        for i in range(self.hash_count):
            # calculate the hash values and mark as 1
            digest = mmh3.hash(item, i) % self.size_of_bitarray
            # mark as came
            self.bit_array[digest] = True

    # function to check whether the element is already there or not
    def check(self, item):
        # check each hash value is present in the bitarray if one is missing 
        # that means there is no chance to that element to be in the stream
        for i in range(self.hash_count):
            digest = mmh3.hash(item, i) % self.size_of_bitarray
            if self.bit_array[digest] == False:
                return False
        
        return True

    

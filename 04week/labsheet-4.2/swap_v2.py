#!/usr/bin/env python3

from swap_v2_042 import swap_unique_keys_values


def main():
    my_dict = {'a' : 4, 'b' : 7, 'c' : 10, 'd' : 7}
    new_dict = swap_unique_keys_values(my_dict)
#    print (new_dict)
    print(sorted(new_dict.items()))

if __name__ == '__main__':
    main()

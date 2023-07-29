#!/usr/bin/python3
"""
UTF-8 Validation
"""


def validUTF8(data):
    '''Determines if a given data set represents a valid UTF-8 encoding

    Returns a bool representing True or False
    '''

    for i in range(len(data)):
        byte = data[i]
        byte_num = 0

        if byte <= 255:
            if byte & 128 == 0:
                byte_num = 1
            elif byte & 224 == 192:
                byte_num = 2
            elif byte & 240 == 224:
                byte_num = 3
            elif byte & 248 == 240:
                byte_num = 4
            else:
                return False
        else:
            return False

        j = 1
        while j < byte_num:
            if (j + i) >= byte_num:
                return False
            elif data[i + j] & 192 != 128:
                return False
            j += 1
        i = i + byte_num

    return True

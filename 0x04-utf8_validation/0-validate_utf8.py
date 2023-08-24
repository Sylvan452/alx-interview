#!/usr/bin/python3
"""This contains a function that performs UTF-8 Validation"""


def validUTF8(data):
    """Determines if a given data set
    represents a valid utf-8 encoding
    """
    number_bytes = 0

    point_1 = 1 << 7
    point_k2 = 1 << 6


    for i in data:

        mask_byte = 1 << 7

        if number_bytes == 0:

            while mask_byte & i:
                number_bytes += 1
                mask_byte = mask_byte >> 1

            if number_bytes == 0:
                continue

            if number_bytes == 1 or number_bytes > 4:
                return False

        else:
            if not (i & point_1 and not (i & point_2)):

                return False

        number_bytes -= 1

    if number_bytes == 0:
        return True

    return False


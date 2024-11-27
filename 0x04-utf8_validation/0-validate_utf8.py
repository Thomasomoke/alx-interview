#!/usr/bin/python3
"""
A method that determines if a given data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Validate if the given data set represents a valid UTF-8 encoding.

    Args:
        data (list): A list of integers representing bytes.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """
    num_bytes = 0

    for byte in data:
        # Use only the 8 least significant bits
        byte &= 0xFF

        if num_bytes == 0:
            # Determine UTF-8 byte length
            if (byte & 0b10000000) == 0:
                continue
            elif (byte & 0b11000000) == 0b11000000:
                num_bytes = 1
            elif (byte & 0b11100000) == 0b11100000:
                num_bytes = 2
            elif (byte & 0b11110000) == 0b11110000:
                num_bytes = 3
            else:
                return False
        else:
            if (byte & 0b11000000) != 0b10000000:
                return False
            num_bytes -= 1

    return num_bytes == 0

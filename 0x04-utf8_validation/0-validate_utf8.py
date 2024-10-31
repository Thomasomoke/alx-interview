#!/usr/bin/python3


def validUTF8(data):
    """
    Determine if a given data set represents a valid
    """
    num_bytes = 0

    # Masks to check the first bits of each byte
    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        # Use only the 8 least significant bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine UTF-8 byte length
            if (byte & mask1) == 0:
                continue
            elif (byte & (mask1 | mask2)) == (mask1 | mask2):
                num_bytes = 1
            elif (byte & (mask1 | mask2 | (1 << 5))) == (
                mask1 | mask2 | (1 << 5)
            ):
                num_bytes = 2
            elif (byte & (mask1 | mask2 | (1 << 5) | (1 << 4))) == (
                mask1 | mask2 | (1 << 5) | (1 << 4)
            ):
                num_bytes = 3
            else:
                return False
        else:
            if (byte & (mask1 | mask2)) != mask1:
                return False
            num_bytes -= 1

    return num_bytes == 0


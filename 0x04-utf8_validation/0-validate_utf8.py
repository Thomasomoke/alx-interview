#!/usr/bin/python3
def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the first few bits of each byte
    mask1 = 1 << 7   # 10000000
    mask2 = 1 << 6   # 01000000

    for byte in data:
        # Only consider the 8 least significant bits of each integer
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine how many bytes the current UTF-8 character has
            if (byte & mask1) == 0:
                # 1-byte character (0xxxxxxx)
                continue
            elif (byte & (mask1 | mask2)) == (mask1 | mask2):
                # 2-byte character (110xxxxx)
                num_bytes = 1
            elif (byte & (mask1 | mask2 | (1 << 5))) == (mask1 | mask2 | (1 << 5)):
                # 3-byte character (1110xxxx)
                num_bytes = 2
            elif (byte & (mask1 | mask2 | (1 << 5) | (1 << 4))) == (mask1 | mask2 | (1 << 5) | (1 << 4)):
                # 4-byte character (11110xxx)
                num_bytes = 3
            else:
                # Invalid UTF-8 byte
                return False
        else:
            # The following bytes must be 10xxxxxx
            if (byte & (mask1 | mask2)) != mask1:
                return False
            num_bytes -= 1

    return num_bytes == 0

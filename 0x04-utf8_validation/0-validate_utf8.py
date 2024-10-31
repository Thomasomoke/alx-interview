#!/usr/bin/python3
def validUTF8(data):
    # Bytes in current UTF-8 character
    num_bytes = 0

    # Masks to check the first bits of each byte
    mask1 = 1 << 7   # 10000000
    mask2 = 1 << 6   # 01000000

    for byte in data:
        # Use only the 8 least significant bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine UTF-8 byte length
            if (byte & mask1) == 0:
                # 1-byte character
                continue
            elif (byte & (mask1 | mask2)) == (mask1 | mask2):
                # 2-byte character
                num_bytes = 1
            elif (byte & (mask1 | mask2 | (1 << 5))) == (
                mask1 | mask2 | (1 << 5)
            ):
                # 3-byte character
                num_bytes = 2
            elif (byte & (mask1 | mask2 | (1 << 5) | (1 << 4))) == (
                mask1 | mask2 | (1 << 5) | (1 << 4)
            ):
                # 4-byte character
                num_bytes = 3
            else:
                # Invalid byte
                return False
        else:
            # Following bytes must be 10xxxxxx
            if (byte & (mask1 | mask2)) != mask1:
                return False
            num_bytes -= 1

    return num_bytes == 0

#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Check if all boxes can be unlocked.
    Returns True if all boxes can be unlocked, False otherwise.
    """
    unlocked = {0}
    new_unlocked = set()

    while unlocked:
        box = unlocked.pop()
        for key in boxes[box]:
            if (key < len(boxes) and
                    key not in unlocked and
                    key not in new_unlocked):
                new_unlocked.add(key)

        if not new_unlocked:
            break

        unlocked.update(new_unlocked)
        new_unlocked.clear()

    return len(unlocked) == len(boxes)

#!/usr/bin/python3
"""Defines function that determines if all boxes can be opened
   from a list of lists
"""


def unlock(idx, keys=[]):
    """Unlocks a box with key

    Args:
        idx: The index/key of the box
        Key: A list of positive integers of keys to unlock boxes.

    Returns:
        bool: True if the box can be unlocked, False otherwise
    """
    if not keys:
        return False

    if idx in keys:
        keys.remove(idx)
        return True
    else:
        return False


def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.

    Args:
        boxes (list): A list of lists representing the boxes
        and their corresponding keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    keys = set(boxes[0])  # Store all keys in each box.

    unlockedAll = False

    # Iterate through the boxes
    for i in range(1, len(boxes) - 1):
        # Attempt to unlock each box with keys
        unlockedAll = unlock(i, keys)
        # If unlocked add new box keys to keys[]
        keys.update(boxes[i])

    return unlockedAll

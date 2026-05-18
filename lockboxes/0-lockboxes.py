#!/usr/bin/python3
"""
Module to solve the lockboxes problem.
"""


def canUnlockAll(boxes):
    """
    Determines if all the boxes can be opened.

    Args:
        boxes (list of lists): A list where each element is a list of keys
                              contained within that box.

    Returns:
        bool: True if all boxes can be opened, else False.
    """
    if not boxes:
        return False

    n = len(boxes)
    opened_boxes = {0}
    keys_stack = list(boxes[0])

    while keys_stack:
        key = keys_stack.pop()

        # Check if the key opens a valid box and if it hasn't been opened yet
        if key < n and key not in opened_boxes:
            opened_boxes.add(key)
            keys_stack.extend(boxes[key])

    return len(opened_boxes) == n

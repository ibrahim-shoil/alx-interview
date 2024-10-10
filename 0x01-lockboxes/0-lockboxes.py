#!/usr/bin/python3
"""Module to determine if all lockboxes can be opened."""

from typing import List


def canUnlockAll(boxes: List[List[int]]) -> bool:
    """Determines if all boxes can be opened.

    Args:
        boxes (List[List[int]]): A list of lists
        where each sublist contains keys to other boxes.

    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """
    n = len(boxes)
    opened = [False] * n  # Tracks which boxes are opened
    opened[0] = True  # The first box is initially unlocked
    keys = [0]  # Start with keys from the first box

    while keys:
        current_key = keys.pop()  # Get a key
        for key in boxes[current_key]:
            if key < n and not opened[key]:
                opened[key] = True
                keys.append(key)

    return all(opened)

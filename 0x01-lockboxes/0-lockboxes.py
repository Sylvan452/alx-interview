#!/usr/bin/python3
"""
    This defines a function that determines if a number of lists of lists can be
    opened by keys whose value is the number of the box
"""


def canUnlockAll(boxes):
    num_boxes = len(boxes)
    visited = [False] * num_boxes
    visited[0] = True

    queue = [0]
    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if not visited[key]:
                visited[key] = True
                queue.append(key)

    return all(visited)

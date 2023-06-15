#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary or len(a_dictionary) == 0:
        return None
    max_score = None
    max_key = None
    for key, val in a_dictionary.items():
        if max_score is None or max_score < val:
            max_score = val
            max_key = key
    return max_key

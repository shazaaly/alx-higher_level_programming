#!/usr/bin/python3
def best_score(a_dictionary):
    max_score = None
    for key, val in a_dictionary.items():
        if not val:
            return None
        elif max_score is None or max_score < val:
            max_score = val
    return max_score

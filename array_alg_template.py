#!/usr/bin/env python3

def two_pointer(arr):
    start, end = 0, len(arr) - 1
    while start <= end:
        if is_match_condiction():
            # Do something here.
            pass
        elif is_should_move_left:
            start += 1
        elif is_should_move_right:
            right -= 1


def sliding_window(arr):
    start = 0
    for end in range(len(arr)):
        # Do something at end.
        while is_endfail_condiction():
            # Do something at start.
            start += 1

def dynamic_programming_fibonacci(k):
    dp = [0 for _ in range(k)]
    dp[0], dp[1] = 1, 1
    for i in range(2, k):
        dp[i] = dp[i - 2] + dp[i - 1]
    return dp[-1]

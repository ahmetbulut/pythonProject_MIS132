# Computers are often used to automate repetitive tasks.
# Repeating identical or similar tasks without making errors
# is something that computers do well and people do poorly.
# In a computer program, repetition is also called iteration.
"""

Task:
1. start from a given number, and count down to zero.
2. at each step, print the current step number onto screen.

"""

# we do not know when to stop. we should: solved!
# i am repeating myself. that is not good: solved!
# parameter value is a string? should you do any type checks? we expect a number: deferred!

def countdown(n):
    while n > 0:
        print(n)
        n = n - 1

countdown(10)

def speedup():
    v = 0
    while v <= 100:
        print("current velocity:", v)
        v = v + 5
        if (v >= 20): break

speedup()
"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
q = set(range(1, 200))
# q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# Your code here
def sumdiff(q):
    # 1. declare hash tables for sums and diffs
    sum_table = {}
    diff_table = {}
    # 2. find all possible combinations of a + b
    for a in q:
        for b in q:
            if f(a)+f(b) in sum_table:
                # 3. put them in the table with sum used as key
                if (a, b) not in sum_table[f(a)+f(b)]:
                    # don't add the second element with same members i.e. (1,1)
                    sum_table[f(a)+f(b)].append((a, b))
            else:
                sum_table[f(a)+f(b)] = [(a, b)]
    # 4. find all possible combinations of c - d
    for c in q:
        for d in q:
            if f(c)-f(d) in diff_table:
                # 5. put them in the table with diff used as key
                if (c, d) not in diff_table[f(c)-f(d)]:
                    # don't add the second element with same members i.e. (1,1)
                    diff_table[f(c)-f(d)].append((c, d))
            else:
                diff_table[f(c)-f(d)] = [(c, d)]
    # 6. find tables intersection based on keys
    intersecting_keys = list(set(sum_table.keys()) & set(diff_table.keys()))
    for key in intersecting_keys:
        print(
            f"Following combinations of f(a)+f(b) {sum_table[key]} are equal to following combinations of f(c)-f(d){diff_table[key]} and are equal to {key}")


sumdiff(q)


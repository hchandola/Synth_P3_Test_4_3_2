from typing import List

def sat192(nums: List[int], super_factorials=[1, 2, 1]):
    for i, sf in enumerate(super_factorials):
        n = nums[i]
        for j in range(n, 0, -1):
            k = j ** (n - j + 1)
            assert sf % k == 0, f"{i} {sf} {j} {n}"
            sf //= k
        assert sf == 1
    return True
def sol192(super_factorials=[1, 2, 1]):
    """The super-factorial of n is n! (n-1)! (n-2)! ... 1!. Invert a given list of super-factorials.

    [1, 2, 2, 12] => [1, 2, 2, 3]
    """
    queue = set(super_factorials)
    cache = {}
    n = 1
    fact = 1
    s_fact = 1
    while queue:
        fact *= n
        s_fact *= fact
        if s_fact in queue:
            queue.remove(s_fact)
            cache[s_fact] = n
        n += 1
    return [cache[sf] for sf in super_factorials]
# assert sat192(sol192())

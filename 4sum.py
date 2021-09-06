import collections


def fourSum(nums, target):
    # Concept - We can solve it in using a hashmap where we can store the
    # pairs of sum and if we are able to find their remaining sum
    # similar to how to do it in 2 sum, we append it into our result

    # This would store the sum of two numbers and their indexes as a list of tuples
    hashmap = collections.defaultdict(list)

    # To avoid duplicates, we use set here
    result = set()

    for i in range(len(nums)):

        for j in range(i+1, len(nums)):

            # We already have our 2 numbers, look for the remaining two numbers which sum to target
            remaining = target - (nums[i] + nums[j])

            if remaining in hashmap:

                # Look for all the pairs are stored for this particular sum
                for pair in hashmap[remaining]:

                    x, y = pair

                    # Check if all 4 indexes are different
                    if (i != x and i != y) and (j != x and j != y):

                        temp = [nums[i], nums[j], nums[x], nums[y]]

                        temp.sort()
                        result.add(tuple(temp))
            # We add the sum and their indexes as list in hashmap here
            hashmap[nums[i] + nums[j]].append((i, j))

    return list(result)

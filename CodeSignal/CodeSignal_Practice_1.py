""" Given an integer n and an array a of length n, your task is to apply the following mutation to a:

    Array a mutates into a new array b of length n.
    For each i from 0 to n - 1, b[i] = a[i - 1] + a[i] + a[i + 1].
    If some element in the sum a[i - 1] + a[i] + a[i + 1] does not exist, it should be set to 0. For example, b[0] should be equal to 0 + a[0] + a[1].

Example

For n = 5 and a = [4, 0, 1, -2, 3], the output should be mutateTheArray(n, a) = [4, 5, -1, 2, 1].

    b[0] = 0 + a[0] + a[1] = 0 + 4 + 0 = 4
    b[1] = a[0] + a[1] + a[2] = 4 + 0 + 1 = 5
    b[2] = a[1] + a[2] + a[3] = 0 + 1 + (-2) = -1
    b[3] = a[2] + a[3] + a[4] = 1 + (-2) + 3 = 2
    b[4] = a[3] + a[4] + 0 = (-2) + 3 + 0 = 1

So, the resulting array after the mutation will be [4, 5, -1, 2, 1]. """

from collections import defaultdict


def mutateTheArray(n, a):
    res = []

    for i, no in enumerate(a):
        n1 = a[i-1] if 0 <= i-1 < n else 0
        n2 = a[i] if 0 <= i < n else 0
        n3 = a[i+1] if 0 <= i+1 < n else 0

        res.append(n1 + n2 + n3)

    return res


""" You are given two arrays of integers a and b of the same length, and an integer k. We will be iterating through array a from left to right, and simultaneously through array b from right to left, and looking at pairs (x, y), where x is from a and y is from b. Such a pair is called tiny if the concatenation xy is strictly less than k.

Your task is to return the number of tiny pairs that you'll encounter during the simultaneous iteration through a and b.

Example

    For a = [1, 2, 3], b = [1, 2, 3], and k = 31, the output should be
    countTinyPairs(a, b, k) = 2.

    We're considering the following pairs during iteration:
        (1, 3). Their concatenation equals 13, which is less than 31, so the pair is tiny;
        (2, 2). Their concatenation equals 22, which is less than 31, so the pair is tiny;
        (3, 1). Their concatenation equals 31, which is not less than 31, so the pair is not tiny.

    As you can see, there are 2 tiny pairs during the iteration, so the answer is 2. """


def countTinyPairs(a, b, k):
    res = 0

    arrLen = len(a)

    for i in range(arrLen):
        num = int(str(a[i]) + str(b[arrLen-i-1]))
        # print(f"a[i] = {a[i]}, b[arrLen-i-1] = {b[arrLen-i-1]}, num = {num}")

        if num < k:
            res += 1

    return res


""" Given an array of positive integers a, your task is to calculate the sum of every possible a[i] ∘ a[j], where a[i] ∘ a[j] is the concatenation of the string representations of a[i] and a[j] respectively.

Example

    For a = [10, 2], the output should be concatenationsSum(a) = 1344.
        a[0] ∘ a[0] = 10 ∘ 10 = 1010,
        a[0] ∘ a[1] = 10 ∘ 2 = 102,
        a[1] ∘ a[0] = 2 ∘ 10 = 210,
        a[1] ∘ a[1] = 2 ∘ 2 = 22.

    So the sum is equal to 1010 + 102 + 210 + 22 = 1344.

    For a = [8], the output should be concatenationsSum(a) = 88.

    There is only one number in a, and a[0] ∘ a[0] = 8 ∘ 8 = 88, so the answer is 88.

    For a = [1, 2, 3], the output should be concatenationsSum(a) = 198.
        a[0] ∘ a[0] = 1 ∘ 1 = 11,
        a[0] ∘ a[1] = 1 ∘ 2 = 12,
        a[0] ∘ a[2] = 1 ∘ 3 = 13,
        a[1] ∘ a[0] = 2 ∘ 1 = 21,
        a[1] ∘ a[1] = 2 ∘ 2 = 22,
        a[1] ∘ a[2] = 2 ∘ 3 = 23,
        a[2] ∘ a[0] = 3 ∘ 1 = 31,
        a[2] ∘ a[1] = 3 ∘ 2 = 32,
        a[2] ∘ a[2] = 3 ∘ 3 = 33.

    The total result is 11 + 12 + 13 + 21 + 22 + 23 + 31 + 32 + 33 = 198. """


def concatenationsSum(a):
    res = 0
    dict = defaultdict(int)

    for i in range(len(a)):
        str_no = str(a[i])
        str_len = len(str_no)
        dict[str_len] += 1

    for i in range(len(a)):
        for key, val in dict.items():
            res += a[i] * (val * pow(10, key))

        res += (a[i] * len(a))

    return res

    https://codereview.stackexchange.com/questions/225228/sum-of-all-possible-concatenations-of-array-values

    function concatenationsSum2(a) {
    var lowSum = 0;
    for (var i = 0; i < a.length; i++)
        lowSum += a[i];

    var sum = lowSum * a.length;

    for (var i = 0; i < a.length; i++) {
        var size = a[i].toString().length;
        var offset = iPower(10, size);
        sum = sum + lowSum * offset;
    }

    return sum;
}

function iPower(base, power) {
    var result = 1;
    for (var i = 1; i <= power; i++)
        result *= base;

    return result;
}

function concatenationsSum3(a) {
    var lowSum = 0;
    var offsetSum = 0;
    for (var i = 0; i < a.length; i++) {
        lowSum += a[i];

        var size = a[i].toString().length;
        var offset = iPower(10, size);
        offsetSum += offset;
    }

    return lowSum * a.length + lowSum * offsetSum;
}


""" You are implementing your own programming language and you've decided to add support for merging strings. A typical merge function would take two strings s1 and s2, and return the lexicographically smallest result that can be obtained by placing the symbols of s2 between the symbols of s1 in such a way that maintains the relative order of the characters in each string.

For example, if s1 = "super" and s2 = "tower", the result should be merge(s1, s2) = "stouperwer".
You'd like to make your language more unique, so for your merge function, instead of comparing the characters in the usual lexicographical order, you'll compare them based on how many times they occur in their respective strings (fewer occurrences means the character is considered smaller). If the number of occurrences are equal, then the characters should be compared in the usual lexicographical way. If both number of occurences and characters are equal, you should take the characters from the first string to the result.

Given two strings s1 and s2, return the result of the special merge function you are implementing.
 """


def mergeStrings(s1, s2):

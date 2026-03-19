# funkAmir.py

def most_frequent(arr):
    if not arr:
        return None

    freq = {}

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    return max(freq, key=freq.get)
def funk320QJK(arr):
    if len(arr) < 2:
        return None

    arr.sort()

    return arr[len(arr) - 2]
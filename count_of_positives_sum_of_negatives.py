def count_positives_sum_negatives(arr):
    negatives = 0
    positives = 0
    for i in arr:
        if i < 0:
            negatives += i  
        elif i > 0:
            positives += 1
    if not arr:
        return []
    else:
        return [positives, negatives]


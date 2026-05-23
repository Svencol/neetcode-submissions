from typing import List, Tuple


def sum_3_integers(triplet: List[int]) -> int:
    sum = 0
    for i in triplet:
        sum = sum + i
    return sum


def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
    sum = 1
    for i in box_dimensions:
        sum = sum * i
    return sum
  

# do not modify below this line
print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))
print(compute_volume((3, 2, 1)))
print(compute_volume((3, 9, 7)))

import mpi4py
import random

from mpi4py import MPI

# Defines a function returning a random int in the [1,6] interval.
def throw_dice(n=1, prnt=False) -> list:
    dice_values = []
    for i in range(n):
        dice_value = random.randint(1,6)
        dice_values.append(dice_value)

    if prnt:
        print(dice_values)

    return dice_values

#Community of porocesses.
comm = MPI.COMM_WORLD
# Ranks & Sizes.
rank = comm.Get_rank()
size = comm.Get_size()

# 0 - print & send to 3
if rank == 0:
    throw_dice(6, True)

# 1 - throw twice, print each time, sum, send sum to 3

# 2 - throw thrice, print each time, sum, send sum to 3

# 3 - sum of all received
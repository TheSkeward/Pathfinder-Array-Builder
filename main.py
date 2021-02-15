import itertools

PB_LOOKUP = {
    7: -4,
    8: -2,
    9: -1,
    10: 0,
    11: 1,
    12: 2,
    13: 3,
    14: 5,
    15: 7,
    16: 10,
    17: 13,
    18: 17,
}
MOD_LOOKUP = {
    7: -2,
    8: -1,
    9: -1,
    10: 0,
    11: 0,
    12: 1,
    13: 1,
    14: 2,
    15: 2,
    16: 3,
    17: 3,
    18: 4,
}
MIN_SUM = 8
DUMP_STAT = 1


def generate_arrays():
    arrays = sorted(
        list(set(tuple(sorted(t)) for t in itertools.product(range(7, 19), repeat=6)))
    )
    return arrays


def check_array_pb(array, available_points=15):
    return sum(PB_LOOKUP[stat] for stat in array) == available_points


def legal_arrays(arrays):
    return [array for array in arrays if check_array_pb(array)]


def check_array_sum(array, min_sum):
    return sum(MOD_LOOKUP[stat] for stat in array) >= min_sum


def min_sum_arrays(arrays, min_sum, dump_stat):
    return [array for array in arrays if check_array_sum(array[dump_stat:], min_sum)]


# def check_array_sum_of_squares(array, min_sum_of_squares)
#     return sum(PB_LOOKUP[stat]) for

print(f"All legal arrays: {legal_arrays(generate_arrays())}")
print(
    f"All arrays with min sum of at least {MIN_SUM}, counting {DUMP_STAT} dump stat(s):"
    f"{min_sum_arrays(legal_arrays(generate_arrays()), MIN_SUM, DUMP_STAT)} "
)

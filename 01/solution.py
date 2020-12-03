"""Solution for Day 01 of Advent of Code 2020."""

INPUT_PATH = 'input.txt'
GOAL_SUM = 2020

def part_1(numbers):
    """Return the product of _the_ pair of numbers that sums to 2020.
    
    Optimize this search by incrementing counters from both ends simultaneously.
    """
    answer = None
    i = 0
    j = len(numbers) - 1
    while answer is None:
        sum = numbers[i] + numbers[j]
        if sum == GOAL_SUM:
            answer = numbers[i] * numbers[j]
            break
        elif sum < GOAL_SUM:
            i += 1
        elif sum > GOAL_SUM:
            j -= 1

    return(answer)


def part_2(numbers):
    """Return the product of _the_ trio of numbers that sums to 2020.
    
    This function is not as well optimized. Basic pattern:
    1. increment i
    2. check all possible j (descending)
    3. check all possible l (ascending)
    """
    answer = None
    i = 0
    j = len(numbers) - 1
    while answer is None:
        two_sum = numbers[i] + numbers[j]

        # If all j above i have been checked, reset j and increment i.
        if j <= i:
            j = len(numbers) - 1
            i += 1

        # If the sum of 2 numbers >= goal, not a possible combo.
        if two_sum >= GOAL_SUM:
            j -= 1
            continue

        # Else, try to find a third possible number with this i,j.
        for l in range(len(numbers)):
            # Do not reuse numbers.
            if l == i or l == j:
                continue

            # All trios with l > j have already been checked.
            if l >= j:
                break

            # Check if sum is goal with current l.
            three_sum = two_sum + numbers[l]
            if three_sum == GOAL_SUM:
                answer = numbers[i] * numbers[j] * numbers[l]
                break
            # Else, if no valid trio here, modify i,j
            elif three_sum > GOAL_SUM:
                break
        j -= 1
    return answer


if __name__ == "__main__":
    # Read the input as a list of ints.
    with open(INPUT_PATH, 'r') as input_file:
        numbers = [int(n) for n in input_file.readlines()]

    # Sort the list for  O P T I M I Z A T I O N
    numbers.sort()

    solution_1 = part_1(numbers)
    print('Part #1: ' + str(solution_1))

    solution_2 = part_2(numbers)
    print('Part #2: ' + str(solution_2))

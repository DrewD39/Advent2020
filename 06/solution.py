
INPUT_PATH = 'input.txt'



def part_1(answers):
    answer_count = 0
    group_answers = set()
    answers.append('') # Always end with at least one blank line
    for person_answers in answers:
        person_answers = person_answers.rstrip()
        group_answers.update(set(person_answers))

        # Blank lines indicate the separation of groups.
        # Collect a full group before counting.
        if not person_answers:
            answer_count += len(group_answers)
            group_answers = set()
        
    print(answer_count)


def part_2(answers):
    answer_count = 0
    default_set = set('abcdefghijklmnopqrstuvwxyzX')
    group_answers = default_set.copy()
    answers.append('') # Always end with at least one blank line
    for person_answers in answers:
        person_answers = person_answers.rstrip()

        # Blank lines indicate the separation of groups.
        # Collect a full group before counting.
        if not person_answers:
            # Ignore sets of blank lines.
            if len(group_answers) <= 26:
                answer_count += len(group_answers)
            group_answers = default_set.copy()
            continue
        
        group_answers = group_answers.intersection(set(person_answers))
        
    print(answer_count)



if __name__ == "__main__":
    # Read the input as a list of strings.
    with open(INPUT_PATH, 'r') as input_file:
        input_lines = input_file.readlines()

    part_1(input_lines)

    part_2(input_lines)

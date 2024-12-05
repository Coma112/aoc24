from functools import cmp_to_key

def process_input(filename):
    with open(filename) as file:
        input_lines = file.read().splitlines()

    rules = []
    updates = []

    for line in input_lines:
        if line == '':
            continue
        if '|' in line:
            rule = tuple(line.split('|'))
            rules.append(rule)
        else:
            update = tuple(line.split(','))
            updates.append(update)

    lookups = [{page: idx for idx, page in enumerate(update)} for update in updates]

    return rules, updates, lookups

def count_updates(rules, updates, lookups):
    inorder_count = 0
    reorder_count = 0

    for update, lookup in zip(updates, lookups):
        if not check_reorder_conditions(update, lookup):
            inorder_count += middle_page(update)
        else:
            reorder_count += middle_page(sort_update(update))

    return inorder_count, reorder_count

def check_reorder_conditions(update, lookup):
    for (r1, r2) in rules:
        p1 = lookup.get(r1)
        p2 = lookup.get(r2)
        if p1 is not None and p2 is not None and p1 > p2:
            return True
    return False

def compare_rule(page1, page2):
    if (page1, page2) in rules:
        return -1
    if (page2, page1) in rules:
        return 1
    return 0

def sort_update(update):
    return sorted(update, key=cmp_to_key(compare_rule))

def middle_page(update):
    middle_pos = (len(update) - 1) // 2
    return int(update[middle_pos])

if __name__ == "__main__":
    filename = 'aoc2024/5/input.txt'
    rules, updates, lookups = process_input(filename)
    
    inorder, reorder = count_updates(rules, updates, lookups)

    print(f'\nIn order count:  {inorder}')
    print(f'Re-ordered count: {reorder}')

# Ocsmány egy kód de mukodik. Barki latja ezt nezze el.. nem szamit most a szepseg :(
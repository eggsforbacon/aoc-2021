from collections import defaultdict
from copy import copy
import math


def get_sequence():
    with open('data/polymer_template.txt', 'r') as raw:
        ruleset = [line.strip() for line in raw.readlines()]
        template = ruleset[0]
        ruleset = dict([[unit for unit in rules.split(' -> ')] for rules in ruleset[2:]])
    return template, ruleset


def map_insert(ruleset, pairs):
    new_pairs = copy(pairs)
    for pair in pairs:
        if pair in ruleset:
            occurrences = pairs[pair]
            new_pairs[pair] -= occurrences
            new_pairs[pair[0] + ruleset[pair]] += occurrences
            new_pairs[ruleset[pair] + pair[1]] += occurrences
    return new_pairs


def map_pairs(pairs):
    pair_count = defaultdict(int)
    for pair in pairs:
        if pair not in pair_count:
            pair_count[pair] = 0
        pair_count[pair] += 1
    return pair_count


def map_built_polymer(ruleset, template, times):
    n = 2
    pairs = [template[i:i+n] for i in range(0, len(template) - (n - 1), 1)] # List comprehensions are fucking amazing, but really slow, so this is only the 1st iter.
    pairs = map_pairs(pairs)
    for _ in range(times):
        pairs = map_insert(ruleset, pairs)
    return pairs


def get_values(pairs, template):
    monomers = {}
    for pair in pairs:
        mon1, mon2 = pair[0], pair[1]
        if mon1 not in monomers:
            monomers[mon1] = 0
        if mon2 not in monomers:
            monomers[mon2] = 0
        monomers[mon1] += pairs[pair]
        monomers[mon2] += pairs[pair]
    monomers[template[0]] + 1
    monomers[template[-1]] + 1
    return [val//2 for val in list(monomers.values())]


def fast(template, ruleset, times):
    pairs = map_built_polymer(ruleset, template, times)
    values = get_values(pairs, template)
    res = max(values) - min(values)
    print(res)


def main():
    times = 40
    template, ruleset = get_sequence()
    fast(template, ruleset, times)


if __name__ == '__main__':
    main()


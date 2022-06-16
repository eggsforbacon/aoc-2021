def get_sequence():
    with open('data/test/polymer_template.txt', 'r') as raw:
        ruleset = [line.strip() for line in raw.readlines()]
        template = ruleset[0]
        ruleset = [[unit for unit in rules.split(' -> ')] for rules in ruleset[2:]]
    return template, ruleset


def map_monomers(template):
    monomers = {}
    for monomer in template:
        if monomer not in monomers:
            monomers[monomer] = 0
        monomers[monomer] += 1
    return map_monomers


def make_pairs():
    pass


def insert(ruleset, pairs):

    for rule in ruleset:
        pair_if = rule[0]
        monomer = rule[1]
        split = pair_if.split() 
        triad = split[0] + monomer + split[1]


def main():
    template, ruleset = get_sequence()
    monomer_count = map_monomers(template)


if __name__ == '__main__':
    main()


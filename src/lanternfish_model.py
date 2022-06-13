from collections import defaultdict
from pprint import pprint


def initial():
    with open('data/lanternfish_pop0.txt', 'r') as raw:
        population = [int(fish) for fish in raw.read().split(',')]
        return population


def model_growth(initial_population, days):
    population = initial_population
    while days > 0:
        for timer in range(0, len(population)):
            if population[timer] == 0:
                population.append(8)
                population[timer] = 6
            else:
                population[timer] -= 1
        days -= 1
    return len(population)


def fast_model(initial_population, days):
    population = {}
    for timer in initial_population:
        if timer not in population:
            population[timer] = 0
        population[timer] += 1
    
    for day in range(days):
        default_population = defaultdict(int)

        for timer, count in population.items():
            if timer == 0:
                default_population[6] += count
                default_population[8] += count
            else:
                default_population[timer - 1] += count
            population = default_population
    
    return sum(population.values())




def simulate(days):
    fast = days >= 100
    population = initial()
    final_count = model_growth(population, days) if not fast else fast_model(population, days)
    print(f'After {days} days the total population will be of {final_count} fish')


def main():
    simulate(80)
    simulate(256)
    simulate(365)


if __name__ == '__main__':
    main()


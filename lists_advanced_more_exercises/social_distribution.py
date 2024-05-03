def max_number(list_population):
    rich_people = max(list_population)
    return rich_people


def possible_distribution(list_population, min_wealth_part):
    sum_of_min_wealth = len(list_population) * min_wealth_part
    sum_of_population = sum(list_population)
    if sum_of_min_wealth <= sum_of_population:
        return True
    else:
        return False


def distribute_the_wealth(list_population, min_wealth):
    if possible_distribution(list_population, min_wealth):
        for index, value in enumerate(list_population):
            if value < min_wealth:
                difference = min_wealth - value
                list_population[index] = min_wealth
                maximum_wealth = max_number(list_population)
                max_index = list_population.index(maximum_wealth)
                maximum_wealth -= difference
                list_population[max_index] = maximum_wealth
        print(list_population)
    else:
        print("No equal distribution possible")


if __name__ == "__main__":
    population = list(map(int, input().split(", ")))
    minimum_wealth = int(input())
    distribute_the_wealth(population, minimum_wealth)
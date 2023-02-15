import random
import matplotlib.pyplot as plt

# Function to create the
# random binary string
def rand_key(p, string_len):
    # Variable to store the
    # string
    keylist = []
    # Loop to find the string
    # of desired length

    for i in range(p):
        key1 = ""
        for _ in range(string_len):
            # randint function to generate
            # 0, 1 randomly and converting
            # the result into str
            temp = str(random.randint(0, 1))

            # Concatenation the random 0, 1
            # to the final result
            key1 += temp
        keylist.append(key1)

    return keylist


population = rand_key(30, 30)


def fitness_function(population):
    total = 0
    for part in population:
        total += part.count('1')
    return total


def select_top_candidates(population, fitness_function, x):
    population_fitness = [(individual, fitness_function(individual)) for individual in population]
    population_fitness.sort(key=lambda x: x[1], reverse=True)
    return [individual for (individual, fitness) in population_fitness[:x]]


scores = []

for _ in range(1000):
    for j in range(0, len(population), 2):

        child_string = list(population[j])
        child_string2 = list(population[j + 1])

        # mutation
        index = random.randint(0, len(population[0])-1)

        child_string[index] = '0' if child_string[index] == '1' else '1'
        child_string2[index] = '0' if child_string2[index] == '1' else '1'

        # crossover
        crossover = random.randint(0, len(population[0])-1)
        child_string = child_string[:crossover] + child_string2[crossover:]
        child_string2 = child_string2[:crossover] + child_string[crossover:]

        population.append("".join(child_string))
        population.append("".join(child_string2))

    total = fitness_function(population)
    scores.append(total)
    population = select_top_candidates(population, fitness_function, 30)
    print(population)



plt.xlabel("Generation number")
plt.ylabel("Generation_fitness")
plt.title("Generation fitness vs Generation number - Part 1")

plt.plot(list(range(1000)), scores)
plt.show()

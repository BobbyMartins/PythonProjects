import random
import string
import matplotlib.pyplot as plt



# Function to create the random string population
def rand_key(p, string_len):
    # Variable to store the
    # string
    keylist = []
    # Loop to find the string
    # of desired length

    for i in range(p):
        key1 = ""
        key1 = ''.join(random.choices(string.digits, k=string_len))
        keylist.append(key1)

    return keylist


population = rand_key(30, 30)
print(population)
target = "604572821184348851718928969314"


def fitness_function(population, target_string):
    total = 0
    for part in population:
        for i in range(len(part)):
            if part[i] == target_string[i]:
                total += 1
    return total


def select_top_candidates(population, fitness_function, x):
    population_fitness = [(individual, fitness_function(individual, target)) for individual in population]
    population_fitness.sort(key=lambda x: x[1], reverse=True)
    return [individual for (individual, fitness) in population_fitness[:x]]


scores = []

for _ in range(10000):

    for j in range(0, len(population), 2):
        child_string = list(population[j])
        child_string2 = list(population[j + 1])

        # mutation
        index = random.randint(0, len(population[0]) - 1)

        child_string[index] = str(random.randint(0, 9))
        child_string2[index] = str(random.randint(0, 9))

        # crossover
        crossover = random.randint(0, len(population[0]) - 1)
        child_string = child_string[:crossover] + child_string2[crossover:]
        child_string2 = child_string2[:crossover] + child_string[crossover:]

        population[j] = "".join(child_string)
        population[j + 1] = "".join(child_string2)

    total = fitness_function(population, target)
    scores.append(total)
    population = select_top_candidates(population, fitness_function, 30)
    #print("done")



plt.xlabel("Generation number")
plt.ylabel("Generation_fitness")
plt.title("Generation fitness vs Generation number - Part 1")

plt.plot(list(range(10000)), scores)
plt.show()

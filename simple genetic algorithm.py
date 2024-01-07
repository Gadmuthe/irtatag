import random

target = "Hello, World!"
population_size = 100
mutation_rate = 0.01

def generate_random_string(length):
    return ''.join(random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz ,!') for _ in range(length))

def calculate_fitness(text):
    return sum(1 for c1, c2 in zip(text, target) if c1 == c2)

population = [generate_random_string(len(target)) for _ in range(population_size)]

generation = 0
while True:
    generation += 1
    population = sorted(population, key=lambda x: calculate_fitness(x), reverse=True)
    if population[0] == target:
        break

    next_generation = population[:10] 
    for _ in range(population_size - 10):
        parent1, parent2 = random.choices(population[:50], k=2)
        child = ''.join(p1 if random.random() > mutation_rate else p2 for p1, p2 in zip(parent1, parent2))
        next_generation.append(child)
    
    population = next_generation

print(f"Generation: {generation}, Best string: {population[0]}")
import random


def stuff(x):
    return 2 ** x + x - 5  # The function to optimize


def fitness(x):
    ans = stuff(x)
    if ans == 0:
        return 9999  # Perfect solution
    else:
        return abs(1 / ans)  # Inverse of the absolute value


# Initialize solutions
solutions = [random.uniform(-10, 10) for _ in range(1000)]  # Random range for x

for i in range(10000):  # Number of generations
    rankedsolutions = []

    # Evaluate fitness for each solution
    for s in solutions:
        rankedsolutions.append((fitness(s), s))

    # Sort solutions by fitness
    rankedsolutions.sort()
    rankedsolutions.reverse()

    print(f"=== Gen {i} best solution ===")
    print(rankedsolutions[0])  # Best solution of the generation

    # Convergence check
    if rankedsolutions[0][0] > 999:
        break

    # Select the top 100 solutions
    bestsolutions = rankedsolutions[:100]

    # Extract elements for reproduction
    elements = [s[1] for s in bestsolutions]

    # Generate new solutions
    newGen = []
    for _ in range(1000):
        e = random.choice(elements) * random.uniform(0.99, 1.01)  # Mutation
        newGen.append(e)

    solutions = newGen  # Update solutions with the new generation

# youtube video i made explaining the code: https://youtu.be/Acz9ZVzUeIY?si=8u5iZvkfmI3F-JK8

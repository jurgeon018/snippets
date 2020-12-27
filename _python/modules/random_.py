import random

random.random()  # random float from 0 to 1
random.uniform(1, 10)  # random float from 1 to 10
random.randint(1, 6)  # random int from 1 to 6

# random choice from list or string, k - amount of choices
random.choice(['value1', 'value2', 'value3'], k=10, weight=[18, 18, 2])
random.shuffle([1, 2, 3, 4, 5, 6, 7, 8, ])
random.sample([1, 2, 3, 4, 5, 6, 7, 8, ], k=5)

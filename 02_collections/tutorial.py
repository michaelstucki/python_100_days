# day 4

from collections import namedtuple, defaultdict, Counter, deque
import random
import timeit

# namedtuple
User = namedtuple('User', 'name role')
user = User(name='bob', role='coder')
print(f'{user.name} is a {user.role}.')

# defaultdict
challenges_done = [('mike', 10), ('jill', 5), ('mike', 22), ('joe', 22), ('jill', 56)]
challenges = defaultdict(list)
for name, challenge in challenges_done:
    challenges[name].append(challenge)
print(challenges)

# Counter
words = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.".split(' ')

top = Counter(words).most_common(5)
print(top)

# deque
lst = list(range(10000000))
deq = deque(range(10000000))

def insert_and_delete(ds):
    for _ in range(10):
        index = random.choice(range(100))
        ds.remove(index)
        ds.insert(index, index)

time_list = timeit.timeit(stmt="insert_and_delete(ds)",
                          setup="ds=lst",
                          number=10,
                          globals=globals())
time_deque = timeit.timeit(stmt="insert_and_delete(ds)",
                          setup="ds=deq",
                          number=10,
                          globals=globals())

print(f'time: (list) {time_list}, (deque) {time_deque}, time_list/time_deque {time_list/time_deque}')


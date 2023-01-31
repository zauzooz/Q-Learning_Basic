import numpy as np
import pylab as pl
import pandas as pd
import pickle
from random import randint, choice

STATE = [i for i in range(20)]
pickle.dump(STATE, open('parameter/STATE', 'wb'))
ACTION = [i for i in range(10)]
pickle.dump(ACTION, open('parameter/ACTION', 'wb'))

"""
bảng REWARD:
             | action 0 | action 1 | action 2 | action 3 | ... |
    state 0  |          |          |          |          |     |
    ---------|----------|----------|----------|----------|-----|
    state 1  |          |          |          |          |     |
    ---------|----------|----------|----------|----------|-----|
    ...
    ---------|----------|----------|----------|----------|-----|
    state 9  |          |          |          |          |
    ---------|----------|----------|----------|----------|-----|
    ...      |          |          |          |          |     |

REWARD[state][action] == -1 tức là không có hành động nào ở đây,
nếu lớn hơn -1 thì tại đó có action và giá trị đó chính là reward.

"""
REWARD = []
for i in range(len(STATE)):
    x = [randint(-1, 2)+i*0 for i in ACTION]
    while (1 in x and 0 in x and -1 in x) == False:
        x = [randint(-1, 1)+i*0 for i in ACTION]
    REWARD.append(x)
df = pd.DataFrame(REWARD)
df.columns = [f'action_{i}' for i in ACTION]
df.index = [f'state_{i}' for i in STATE]
df.to_csv('parameter/REWARD.csv')
del df


"""
bảng TRANSITION:

             | action 0 | action 1 | action 2 | action 3 | ... |
    state 0  |          |          |          |          |     |
    ---------|----------|----------|----------|----------|-----|
    state 1  |          |          |          |          |     |
    ---------|----------|----------|----------|----------|-----|
    ...
    ---------|----------|----------|----------|----------|-----|
    state 9  |          |          |          |          |
    ---------|----------|----------|----------|----------|-----|
    ...      |          |          |          |          |     |
Giá trị tại TRAINSITION[state][action] trả về state tiếp theo.
"""
TRANSITION = []
for s in range(len(STATE)):
    action_list = [i for i in range(len(REWARD[s])) if REWARD[s][i] > -1]
    new_state_list = [-1 for i in range(len(REWARD[s]))]
    x = STATE.copy()
    for i in action_list:
        new_state_list[i] = choice(x)
        x.remove(new_state_list[i])
    del x
    TRANSITION.append(new_state_list)
df = pd.DataFrame(TRANSITION)
df.columns = [f'action_{i}' for i in ACTION]
df.index = [f'state_{i}' for i in STATE]
df.to_csv('parameter/TRANSITION.csv')
del df
import pandas as pd
import pickle
from random import choice

STATE = pickle.load(open('parameter\STATE','rb'))
ACTION = pickle.load(open('parameter\ACTION','rb'))
REWARD = pd.read_csv('parameter\REWARD.csv', index_col=0).values.tolist()
TRANSITION = pd.read_csv('parameter\TRANSITION.csv', index_col=0).values.tolist()
LEARNING_RATE = 0.1
DISCOUNT_FACTOR = 0.05

def QLearning(STATE, ACTION, REWARD, TRANSITION, LEARNING_RATE=0.1, DISCOUNT_FACTOR=0.05):
    """
    Q_TABLE
             | action 0 | action 1 | action 2 | action 3 | ... |
    state 0  |          |          |          |          |     |
    ---------|----------|----------|----------|----------|-----|
    state 1  |          |          |          |          |     |
    ---------|----------|----------|----------|----------|-----|
    ...
    ---------|----------|----------|----------|----------|-----|
    state 9  |          |          |          |          |
    ---------|----------|----------|----------|----------|-----|
    ...
    """
    Q_TABLE = []
    for state in STATE:
        Q_TABLE.append([0 for i in range(len(ACTION))])
    i = 0
    while i < 10000:
        s = STATE[0]
        while s != STATE[-1]:
            # chọn một hành động a cho state s
            a = choice([i for i in range(len(REWARD[s])) if REWARD[s][i] > -1])
            # nhận reward, xác định state mới s_new, tính Q
            r = REWARD[s][a]
            s_new = TRANSITION[s][a]
            Q_TABLE[s][a] = Q_TABLE[s][a] + LEARNING_RATE*(r + DISCOUNT_FACTOR * Q_TABLE[s_new][a] - Q_TABLE[s][a])
            # set s to new state           
            s = s_new
        i += 1
    print(i)
    return Q_TABLE

print('Đợi tao train tí xong ...')
df = pd.DataFrame(QLearning(
    STATE=STATE,
    ACTION=ACTION,
    REWARD=REWARD,
    TRANSITION=TRANSITION,
    LEARNING_RATE=LEARNING_RATE,
    DISCOUNT_FACTOR=DISCOUNT_FACTOR
))
df.columns=[f'action_{i}' for i in ACTION]
df.index=[f'state_{i}' for i in STATE]
df.to_csv('parameter\Q_TABLE.csv')
print("Xong rồi nè mày!!!")
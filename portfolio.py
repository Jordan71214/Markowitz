import pandas as pd
import copy
from gekko import GEKKO
import numpy as np

wb = pd.read_excel("Naive_S_P500.xlsx" , sheet_name=None)
ret = copy.deepcopy(wb["return"].drop(columns=["Unnamed: 0"]))
assets_obs = ret.iloc[:100, 1:397]
n = assets_obs.shape[1]

P = np.asmatrix(np.mean(assets_obs, axis=0))
w = np.asmatrix(np.random.dirichlet(np.ones(n),size=1))
C = np.cov(assets_obs.T)

m = GEKKO(remote=True)
w=m.Array(m.Var,n)
for i in w:
    i.value = 0
    i.lower=0
    i.upper=1

for i in range(n):
    m.Minimize(w[i] ** 2 * C.item(i, i) ** 2)
    for j in range(n):
        if i != j:
            m.Minimize(C.item(i, j)*w[i]*w[j])

m.Equation(m.sum([x for x in w]) == 1)
m.Equation(m.sum([P.item(i)*w[i] for i in range(n)]) >= 0.001)
m.solve()
print(len(w))
print('weight: ', [x.value for x in w])
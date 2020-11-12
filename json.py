# -*- coding: utf-8 -*-
"""
Created on Thu Oct 15 10:50:26 2020

@author: e393737
"""
import pandas as pd
import json
data = pd.read_csv("C://Users//e393737//.spyder-py3//Test1.csv")
df = pd.DataFrame(data)
df_test = pd.DataFrame(data)
lst = []
i = 0
while i < len(df_test):
    tup = tuple(df_test.iloc[i])
    lst.append(tup)
    i = i + 1


# Build a directed graph and a list of all names that have no parent
graph = {name: set() for tup in lst for name in tup}
has_parent = {name: False for tup in lst for name in tup}
for parent, child in lst:
    graph[parent].add(child)
    has_parent[child] = True

# All names that have absolutely no parent:
roots = [name for name, parents in has_parent.items() if not parents]

# traversal of the graph (doesn't care about duplicates and cycles)
def traverse(hierarchy, graph, names):
    for name in names:
        hierarchy[name] = traverse({}, graph, graph[name])
    return hierarchy

dct = traverse({}, graph, roots)
with open("dod.json","w") as outfile:
    json.dump(dct, outfile)

from platform import node
from os import pathsep,PathLike

def f(g,h,n):
    return g[n] + h[n]

def update(to_remove,to_add,m):
    to_remove.remove(m)
    to_add.append(m)

def a_star_imp(cost,heuristic,start,goal):
    path = []
    pathset = []
    open_list = [start]
    closed_list = []

    path_length = {}
    path_length[start] = 0
    parent_node = {}
    parent_node[start] = start

    while len(open_list) > 0:
        node = None
        for n in open_list:
            if node ==None or f(path_length,heuristic,n) <f(path_length,heuristic,node):
                node = n
        if node == None:
         break

        if node in goal:
            fv_n = f(path_length,heuristic,node)
            reconstruct = []

    ``````` aux = node
            while parent_node[aux] != aux:
                reconstruct.append(aux)
                aux = parent_node[aux]
            reconstruct.append(aux)
            reconstruct.reverse()

            pathset.append((reconstruct,fv_n))

            update(open_list,closed_list,node)
              

    path_cost = cost[node]

        for idx in range(0,len(path_cost)):
            weight = path_cost[idx]

            if weight>0:
                if idx not in open_list and idx not in closed_list:
                    open_list.append(idx)
                    parent_node[idx] = node
                    path_length[idx] = path_length[node] + weight

                else:
                    if path_length[idx] > path_length[node] + weight:
                        path_length[idx] = path_length[node] + weight
                        parent_node[idx] = node

                        if idx in closed_list:
                            update(closed_list,open_list,idx)

        update(closed_list,open_list,node)

    if len(pathset)>0:
        pathset = sorted(pathset,key=lambdax:x[1])
        path = pathset[0][0]
    else:
        path = []

    return path

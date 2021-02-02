import math


def heuristic_cost_estimate(current, task):   # 启发式距离：从当前点到目标点
    return distance_between(current, task)


def distance_between(n1, n2):     # 计算距离
    latA, longA = n1
    latB, longB = n2

    x = longB - longA
    y = latB - latA
    return math.hypot(x, y)     # 调用函数计算欧氏距离

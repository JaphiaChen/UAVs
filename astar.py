from distance_cal import  heuristic_cost_estimate
from heapq import heappush

Infinite = float('inf')


def astar (uav, task_list, no_fly_zones):
    path = []
    heappush(path, uav.position)  # 把首节点压入栈中
    while task_list:    # 还有待完成的任务
        nearest_neighbour = []
        nearest_distance = Infinite     # 最近的任务距离
        for neighbour in task_list:
            neighbour_distance = heuristic_cost_estimate(uav.position, neighbour)
            if neighbour_distance < nearest_distance:
                nearest_distance = neighbour_distance   # 更新最小的任务距离和最小距离任务
                nearest_neighbour = neighbour

        for id in no_fly_zones:     # 判断是否经过禁飞区
            zone_id = no_fly_zones[str(id)].across_no_fly_zone(uav.position, nearest_neighbour)
            if zone_id:
                nearest_neighbour = no_fly_zones[str(id)].mid_point(uav.position, nearest_neighbour)
                break
        path.append(nearest_neighbour)
        uav.position = nearest_neighbour
        if nearest_neighbour in task_list:
            task_list.remove(nearest_neighbour)
    return path
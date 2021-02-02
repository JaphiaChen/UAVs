from heapq import heappush

from class_definition import UAV
from class_definition import Target
from class_definition import No_fly_zone


def solve_info(in_stream1,in_stream2):
    uavs = {}
    no_fly_zones = {}

    # 此行是UAV信息项介绍
    _ = in_stream1.readline().strip()
    N = int(in_stream1.readline())       # UAV总数
    for _ in range(N):      # 循环从txt中读取信息，生成UAV类的多个实例
        items = in_stream1.readline().strip().split(',')     # 每行先读到items变量
        id = items[0]   # 首位是id
        position = float(items[1]), float(items[2])     # 第二、三位是position
        direction = float(items[3]), float(items[4])  # 第四、五位是direction
        cost = items[5]     # 第六位是cost
        uavs[id] = UAV(id, position, direction, [], cost, 0)

    # 此行是Target信息项介绍
    _ = in_stream2.readline().strip()
    for id in uavs:
        targets = {}
        M = int(in_stream2.readline()[0])       # Target总数
        for _ in range(M):      # 循环从txt中读取信息，生成Target类的多个实例
            items = in_stream2.readline().strip().split(',')     # 每行先读到items变量
            targets_id = items[0]   # 首位是id
            position = float(items[1]), float(items[2])     # 第二、三位是position
            reward = items[3]     # 第四位是reward
            targets[targets_id] = Target(targets_id, position, reward)
            heappush(uavs[str(id)].task_list, targets[str(targets_id)].position)

    # 此行是禁飞区信息项介绍
    _ = in_stream1.readline().strip()
    L = int(in_stream1.readline())       # 禁飞区总数
    for _ in range(L):      # 循环从txt中读取信息，生成Target类的多个实例
        item1 = in_stream1.readline().strip().split(',')     # 每行先读到items变量
        item2 = in_stream1.readline().strip().split(',')
        id = item1[0]
        zone_x = list(map(float,item1[1:]))     # 第二、三行是禁飞区
        zone_y = list(map(float,item2[1:]))
        no_fly_zones[id] = No_fly_zone(id, zone_x, zone_y)
    return uavs, no_fly_zones

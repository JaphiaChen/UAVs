import matplotlib.pyplot as plt
# 绘制起飞点和目标位置、禁飞区区域


def init_draw(uavs, no_fly_zones):
    uavs_x = []
    uavs_y = []
    targets_x = []
    targets_y = []
    for id in uavs:
        uavs_x.append(uavs[str(id)].position[0])
        uavs_y.append(uavs[str(id)].position[1])
        for tasks in uavs[str(id)].task_list:
            targets_x.append(tasks[0])
            targets_y.append(tasks[1])

    plt.plot(uavs_x, uavs_y, 'bo', markersize=10)
    plt.plot(targets_x, targets_y, 'rp', markersize=10)

    for id in no_fly_zones:
        x = no_fly_zones[str(id)].x
        y = no_fly_zones[str(id)].y
        plt.fill(x, y, facecolor='k')


# 绘制单无人机的航迹规划
def draw_one(path):
    line_x = []
    line_y = []
    for point in path:
        line_x.append(point[0])
        line_y.append(point[1])
    plt.plot(line_x, line_y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Path Finding')

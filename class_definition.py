from distance_cal import distance_between
Infinite = float('inf')


class Target:  # 目标信息
    def __init__(self, id, position, reward):
        self.id = id    # 目标编号
        self.position = position    # 目标位置，含x，y信息
        self.reward = reward
        self.have_been_suvellence = False   # 目标是否被监视
        self.have_been_attack = False  # 目标是否被打击
        self.have_been_verify = False  # 目标是否被核验


class UAV:  # 无人机信息
    def __init__(self, id, position, direction, task_list, cost, path_length):
        self.id = id   # 无人机编号
        self.position = position    # 无人机当前位置
        self.direction = direction    # 无人机方向，以向量形式表示，x，y轴均为0或1，方向可能值为0，45，90，135，180，225，270，315
        self.task_list = task_list    # 无人机执行任务列表
        self.cost = cost    # 无人机损毁时的损失价值
        self.path_length = path_length  # 无人机的行驶距离


class No_fly_zone:  # 禁飞区信息
    def __init__(self,id,x,y):
        self.id = id
        self.x = x
        self.y = y

    # 判断是否路过禁飞区
    # https://blog.csdn.net/qq_39627843/article/details/81170316?utm_medium=distribute.pc_relevant_download.none-task-blog-baidujs-2.nonecase&depth_1-utm_source=distribute.pc_relevant_download.none-task-blog-baidujs-2.nonecase
    def across_no_fly_zone(self, current, neighbour):
        across = False

        def cmulplify (A, B, C):  # 叉乘
            return (B[0]-A[0])*(C[1]-A[1])-(C[0]-A[0])*(B[1]-A[1])

        for num in range(len(self.x)-1):    # 逐线判断是否相交
            A = self.x[num], self.y[num]
            B = self.x[num+1], self.y[num+1]

            if min(A[0], B[0]) <= max(current[0],neighbour[0]) and \
            min(current[0], neighbour[0]) <= max(A[0], B[0]) and \
            min(A[1], B[1]) <= max(current[1], neighbour[1]) and\
            min(current[1], neighbour[1]) <= max(A[1], B[1]) and\
            cmulplify (A, B, current) * cmulplify(A, B, neighbour) < 0 and\
            cmulplify (current, neighbour, A) * cmulplify(current, neighbour, B) < 0:
                across = True
        if across:
            return self.id
        return False

    def mid_point(self, uav, nearest_neighbour):
        mid_point_distance = Infinite
        mid_point = []

        for num in range(len(self.x)):  # 逐点判断最优点
            temp = self.x[num], self.y[num]
            if self.across_no_fly_zone(temp, nearest_neighbour) or self.across_no_fly_zone(uav, temp):
                continue
            tentative_distance = distance_between(uav, temp)+distance_between(temp,nearest_neighbour)
            if tentative_distance < mid_point_distance:
                mid_point = temp
                mid_point_distance = tentative_distance
        return mid_point

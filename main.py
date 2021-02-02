import os
import unittest
import matplotlib.pyplot as plt
from information_input import solve_info
from astar import astar
from draw_map import init_draw
from draw_map import draw_one

__author__ = "JaphiaChen"
__version__ = "1.0"
__email__ = 'qiuzhuo196@gmail.com'
__date__ = "2021/2/1"


class Test(unittest.TestCase):     # testcase

    def test_solve(self):

        rootdir = os.path.dirname(__file__)
        with open(os.path.join(rootdir, 'UAVs_Targets_info.in.txt')) as inputFile:  # 打开输入信息txt
            uavs, no_fly_zones = solve_info(inputFile)
            init_draw(uavs, no_fly_zones)  # 画出原始地图
            for id in uavs:
                path = astar(uavs[str(id)], uavs[str(id)].task_list, no_fly_zones)  # 调用astar生成可行的路径
                draw_one(path)
            plt.show()


if __name__ == '__main__':
    unittest.main()

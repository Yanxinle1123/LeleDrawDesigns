import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import CubicSpline


class LineChart:
    def __init__(self, squares=None, input_values=None, skin=None, style=None,
                 inewidth=None, labelsize=None, set_title=None, set_title_fontsize=None, set_xlabel=None,
                 set_xlabel_fontsize=None, set_ylabel=None, set_ylabel_fontsize=None):
        self._linewidth = inewidth
        self._labelsize = labelsize
        self._squares = squares
        self._input_values = input_values
        self._set_title = set_title
        self._set_title_fontsize = set_title_fontsize
        self._set_xlabel = set_xlabel
        self._set_xlabel_fontsize = set_xlabel_fontsize
        self._set_ylabel = set_ylabel
        self._set_ylabel_fontsize = set_ylabel_fontsize
        self._skin = skin
        self._style = style
        if self._squares is None:
            self._squares = [1, 4, 9, 16, 25]
        if self._skin is None:
            self._skin = 'seaborn-v0_8'
        if self._style is None:
            self._style = 'straight'
        if self._linewidth is None:
            self._linewidth = 3
        if self._labelsize is None:
            self._labelsize = 10
        if self._input_values is None:
            self._input_values = [0, 1, 2, 3, 4]
        self.draw()

    def draw(self):
        if self._style == 'straight':
            input_values = self._input_values
            squares = self._squares
            # print(f"input_values:{input_values}")
            # print(f"squares:{squares}")

            plt.style.use(self._skin)

            _, ax = plt.subplots()
            if input_values is None:
                ax.plot(squares, linewidth=self._linewidth)
            else:
                ax.plot(input_values, squares, linewidth=self._linewidth)

            ax.set_title(self._set_title, fontsize=self._set_title_fontsize)
            ax.set_xlabel(self._set_xlabel, fontsize=self._set_xlabel_fontsize)
            ax.set_ylabel(self._set_ylabel, fontsize=self._set_ylabel_fontsize)

            ax.tick_params(labelsize=self._labelsize)

            plt.show()
        elif self._style == 'curved':
            input_values = self._input_values
            squares = self._squares

            # 三次样条插值
            cs = CubicSpline(input_values, squares)

            # 生成插值数据点
            x = np.linspace(min(input_values), max(input_values), num=100)
            y = cs(x)

            # 设置图的样式
            plt.style.use(self._skin)

            _, ax = plt.subplots()

            # 绘制折线图（蓝线）
            ax.plot(x, y, linewidth=self._linewidth)

            # 绘制散点图（红点）
            ax.scatter(input_values, squares, color='red', marker='o', zorder=3)

            # 设置图题并给坐标轴加上标签
            ax.set_title(self._set_title, fontsize=self._set_title_fontsize)
            ax.set_xlabel(self._set_xlabel, fontsize=self._set_xlabel_fontsize)
            ax.set_ylabel(self._set_ylabel, fontsize=self._set_ylabel_fontsize)

            # 设置刻度标记的样式
            ax.tick_params(labelsize=self._labelsize)

            plt.show()

    def obtain_all_skin(self):
        print(['Solarize_Light2', '_classic_test_patch', '_mpl-gallery', '_mpl-gallery-nogrid', 'bmh', 'classic',
               'dark_background', 'fast', 'fivethirtyeight', 'ggplot', 'grayscale', 'seaborn-v0_8',
               'seaborn-v0_8-bright', 'seaborn-v0_8-colorblind', 'seaborn-v0_8-dark', 'seaborn-v0_8-dark-palette',
               'seaborn-v0_8-darkgrid', 'seaborn-v0_8-deep', 'seaborn-v0_8-muted', 'seaborn-v0_8-notebook',
               'seaborn-v0_8-paper', 'seaborn-v0_8-pastel', 'seaborn-v0_8-poster', 'seaborn-v0_8-talk',
               'seaborn-v0_8-ticks', 'seaborn-v0_8-white', 'seaborn-v0_8-whitegrid', 'tableau-colorblind10'])

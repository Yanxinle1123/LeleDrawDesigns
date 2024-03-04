import matplotlib.pyplot as plt

from die import Die

die = Die()

list_results = []
for roll_num in range(1000):
    result = die.roll()
    list_results.append(result)

list_frequencies = []
poss_results = range(1, die.num_sides + 1)
for value in poss_results:
    frequency = list_results.count(value)
    list_frequencies.append(frequency)

print(list_frequencies)


class Histogram:
    def __init__(self, input_values=None, frequencies=None, color=None, edgecolor=None, title=None, title_fontsize=None,
                 x_label=None, x_label_fontsize=None, y_label=None, y_label_fontsize=None):
        self._input_values = input_values
        self._frequencies = frequencies
        self._color = color
        self._edgecolor = edgecolor
        self._title = title
        self._title_fontsize = title_fontsize
        self._x_label = x_label
        self._x_label_fontsize = x_label_fontsize
        self._y_label = y_label
        self._y_label_fontsize = y_label_fontsize

        if self._input_values is None:
            self._input_values = poss_results
        if self._frequencies is None:
            self._frequencies = list_frequencies
        if self._color is None:
            self._color = 'blue'
        if self._edgecolor is None:
            self._edgecolor = 'black'

        self.draw()

    def draw(self):
        plt.bar(self._input_values, self._frequencies, color=self._color, edgecolor=self._edgecolor)
        plt.title(self._title, fontsize=self._title_fontsize)
        plt.xlabel(self._x_label, fontsize=self._x_label_fontsize)
        plt.ylabel(self._y_label, fontsize=self._y_label_fontsize)

        plt.show()

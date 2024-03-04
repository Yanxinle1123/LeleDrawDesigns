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
                 xlabel=None, xlabel_fontsize=None, ylabel=None, ylabel_fontsize=None):
        self._input_values = input_values
        self._frequencies = frequencies
        self._color = color
        self._edgecolor = edgecolor
        self._title = title
        self._title_fontsize = title_fontsize
        self._xlabel = xlabel
        self._xlabel_fontsize = xlabel_fontsize
        self._ylabel = ylabel
        self._ylabel_fontsize = ylabel_fontsize

        if self._input_values is None:
            self._input_values = poss_results
        if self._frequencies is None:
            self._frequencies = list_frequencies
        if self._color is None:
            self._color = 'blue'
        if self._edgecolor is None:
            self._edgecolor = 'black'

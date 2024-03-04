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
            return
        if self._frequencies is None:
            return
        if self._color is None:
            return
        if self._edgecolor is None:
            return
        if self._title is None:
            return
        if self._title_fontsize is None:
            return
        if self._ylabel is None:
            return
        if self._ylabel_fontsize is None:
            return
        if self._title_fontsize is None:
            return

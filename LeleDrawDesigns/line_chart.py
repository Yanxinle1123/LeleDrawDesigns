class LineChart:
    def __init__(self, squares=None, input_values=None, skin=None, style=None,
                 set_title=None, set_title_fontsize=None, set_xlabel=None,
                 set_xlabel_fontsize=None, set_ylabel=None, set_ylabel_fontsize=None):
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

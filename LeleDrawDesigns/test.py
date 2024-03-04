from LeleDrawDesigns.histogram import Histogram
from LeleDrawDesigns.line_chart import LineChart, obtain_all_skin

curved_line_chart = LineChart(input_values=[1, 2, 3, 4, 5], squares=[1, 4, 9, 16, 25], style='curved',
                              skin='Solarize_Light2', set_title='CurvedLineChart', set_title_fontsize=20,
                              set_x_label='XLabel', set_x_label_fontsize=20, set_y_label='YLabel',
                              set_y_label_fontsize=20, line_width=3)

straight_line_chart = LineChart(input_values=[1, 2, 3, 4, 5], squares=[1, 4, 9, 16, 25], style='straight',
                                skin='Solarize_Light2', set_title='StraightLineChart', set_title_fontsize=20,
                                set_x_label='XLabel', set_x_label_fontsize=20, set_y_label='YLabel',
                                set_y_label_fontsize=20, line_width=3)

obtain_all_skin()

histogram = Histogram()

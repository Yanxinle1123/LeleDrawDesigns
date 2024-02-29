from LeleDrawDesigns.line_chart import LineChart

curved_line_chart = LineChart(input_values=[1, 2, 3, 4, 5], squares=[1, 4, 9, 16, 25], style='curved',
                              skin='Solarize_Light2', set_title='CurvedLineChart', set_title_fontsize=20,
                              set_xlabel='XLabel', set_xlabel_fontsize=20, set_ylabel='YLabel', set_ylabel_fontsize=20)

straight_line_chart = LineChart(input_values=[1, 2, 3, 4, 5], squares=[1, 4, 9, 16, 25], style='straight',
                                skin='Solarize_Light2', set_title='StraightLineChart', set_title_fontsize=20,
                                set_xlabel='XLabel', set_xlabel_fontsize=20, set_ylabel='YLabel',
                                set_ylabel_fontsize=20)

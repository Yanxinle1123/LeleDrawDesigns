from LeleDrawDesigns.line_chart import LineChart

line_chart = LineChart(input_values=[1, 2, 3, 4, 5], squares=[1, 4, 9, 16, 25], style='curved')
line_chart.draw()

line_chart = LineChart(input_values=[1, 2, 3, 4, 5], squares=[1, 4, 9, 16, 25], style='straight')
line_chart.draw()

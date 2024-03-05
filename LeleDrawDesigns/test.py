from LeleDrawDesigns.dice_analysis import dice_analysis
from LeleDrawDesigns.histogram import Histogram
from LeleDrawDesigns.line_chart import LineChart, obtain_all_skin

poss_results, frequencies = dice_analysis()

input_values = []
for i in range(len(frequencies)):
    input_values.append(i + 1)

title = 'Results of Rolling One D6 1,000 Times'
xlabel = 'Result'
ylabel = 'Frequency of Result'
x_labels = ["one", "two", "three", "four", "five", "six"]

histogram = Histogram(poss_results, frequencies, x_ticks=x_labels, skin='Solarize_Light2', title=title,
                      title_fontsize=20, x_label=xlabel, x_label_fontsize=20, y_label=ylabel, y_label_fontsize=20,
                      color='green', edgecolor='black', figsize=(15, 10), x_ticks_fontsize=20)

straight_line_chart = LineChart(input_values=input_values, squares=frequencies, x_ticks=x_labels, style='straight',
                                line_color='green', skin='Solarize_Light2', set_title=title, set_title_fontsize=20,
                                set_x_label=xlabel, set_x_label_fontsize=20, set_y_label=ylabel,
                                set_y_label_fontsize=20, line_width=3, figsize=(15, 10), x_ticks_fontsize=20)

curved_line_chart = LineChart(input_values=input_values, squares=frequencies, x_ticks=x_labels, style='curved',
                              line_color='green', skin='Solarize_Light2', set_title=title, set_title_fontsize=20,
                              set_x_label=xlabel, set_x_label_fontsize=20, set_y_label=ylabel, set_y_label_fontsize=20,
                              line_width=3, figsize=(15, 10), x_ticks_fontsize=20)

obtain_all_skin()

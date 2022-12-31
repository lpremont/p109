import random 
import statistics
#import plotly.figure_factory as ff

dice_result = []

for i in range(0,1000):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    dice_result.append(dice1+dice2)

mean = sum(dice_result)/len(dice_result)
#mean = statistics.mean(dice_result)
median = statistics.median(dice_result)
mode = statistics.mode(dice_result)
std_dev = statistics.stdev(dice_result)

first_std_dev_start, first_std_dev_end = mean-std_dev, mean+std_dev
list_of_data_within_1_std_dev = [result for result in dice_result if result > first_std_dev_start and result < first_std_dev_end]

second_std_dev_start, second_std_dev_end = mean-(2*std_dev), mean+(2*std_dev)
list_of_data_within_2_std_dev = [result for result in dice_result if result > second_std_dev_start and result < second_std_dev_end]

third_std_dev_start, third_std_dev_end = mean-(3*std_dev), mean+(3*std_dev)
list_of_data_within_3_std_dev = [result for result in dice_result if result > third_std_dev_start and result < third_std_dev_end]

print("Mean of the data {}"+format(mean))
print("Median of the data {}"+format(median))
print("Mode of the data {}"+format(mode))

print("Standard deviation of the data {}"+format(std_dev))
print('{}% of data lies within first standard deviation'.format(len(list_of_data_within_1_std_dev)*100.0/len(dice_result)))
print('{}% of data lies within second standard deviation'.format(len(list_of_data_within_2_std_dev)*100.0/len(dice_result)))
print('{}% of data lies within third standard deviation'.format(len(list_of_data_within_3_std_dev)*100.0/len(dice_result)))

#fig = ff.create_distplot([dice_result],["result"],show_hist=False)


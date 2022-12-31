import pandas as pd
import statistics

df = pd.read_csv("height-weight.csv")
height = df["Height(Inches)"].to_list()

mean = statistics.mean(height)
median = statistics.median(height)
mode = statistics.mode(height)
std_dev = statistics.stdev(height)

first_std_dev_start, first_std_dev_end = mean-std_dev, mean+std_dev
list_of_data_within_1_std_dev = [result for result in height if result > first_std_dev_start and result < first_std_dev_end]

second_std_dev_start, second_std_dev_end = mean-(2*std_dev), mean+(2*std_dev)
list_of_data_within_2_std_dev = [result for result in height if result > second_std_dev_start and result < second_std_dev_end]

third_std_dev_start, third_std_dev_end = mean-(3*std_dev), mean+(3*std_dev)
list_of_data_within_3_std_dev = [result for result in height if result > third_std_dev_start and result < third_std_dev_end]

#print("Mean of the data {}"+format(mean))
#print("Median of the data {}"+format(median))
#print("Mode of the data {}"+format(mode))
print("Mean, Medan and Mode of height is {}, {} and {}".format(mean, median, mode))
print("Standard deviation of the data {}"+format(std_dev))
print('{}% of data lies within first standard deviation'.format(len(list_of_data_within_1_std_dev)*100.0/len(height)))
print('{}% of data lies within second standard deviation'.format(len(list_of_data_within_2_std_dev)*100.0/len(height)))
print('{}% of data lies within third standard deviation'.format(len(list_of_data_within_3_std_dev)*100.0/len(height)))

import numpy as np
import random
import matplotlib.pyplot as plt


class TossingCoin:  # create a class for experiment
    def __init__(self, times, H_probability):   # initiate 2 parameters: run times and the probability of head occurs
        self.times = times
        self.H_probability = H_probability
        experiment_result = []  # The list of experiment result
        run_of_head = 0     # Count the number of head occurs.
        longest_run_of_head = 0     # Count the longest run of heads.
        longest_run_of_head_list = []
        # following is the experiment
        for i in range(self.times):     # run "times" of experiments
            experiment_element = random.uniform(0,1)    # generate a random number between 0 and 1
            if experiment_element < self.H_probability:    # If the # if bigger or equal to the probability of head
                experiment_result.append("H")               # occurs, append a "H" into result list
                run_of_head += 1                            # The # of head + 1
            else:
                experiment_result.append("T")           # generate a "T" into result list
                if run_of_head > longest_run_of_head:   # If the length of the run of head is bigger than the longest
                    longest_run_of_head = run_of_head   # run of heads, replace the longest run of heads.
                run_of_head = 0                         # Initiate the run of head.
        self.experiment_result = experiment_result
        self.longest_run_of_head = longest_run_of_head

    def num_of_head(self):                              # a function for count the # of "H"
        return self.experiment_result.count("H")

    def longestRunOfHead(self):                         # a function for return the longest run of heads
        return self.longest_run_of_head


#Q1
# data = TossingCoin(50, 0.5)                             # create a class for 50 run times with 0.5 head probability
# experiment_result = data.experiment_result              # result is a list
# print("The number of heads is:", data.num_of_head())
# print("The longest run of heads is:", data.longestRunOfHead())
# labels, counts = np.unique(experiment_result, return_counts=True)   # let labels as "T" and "H", counts as # of occurs
# plt.bar(labels, counts, align="center")                             # let the label of bar shows in the middle
# plt.gca().set_xticks(labels)
# plt.xlabel("Experiment results")
# plt.ylabel("Counts")
# plt.show()


#Q1.a
# def exp_times(times):   # create a function for implement experiment in specific times.
#     head_list = []
#     for i in range(times):
#         data = TossingCoin(50, 0.5)
#         head_list.append(data.num_of_head())
#     return head_list, sum(head_list)    # return 2 values: head list and the number of heads.
# result = exp_times(1000)
# print("The number of heads", result[1])
# labels, counts = np.unique(result[0], return_counts=True)
# plt.bar(labels, counts, align="center")
# plt.gca().set_xticks(labels)
# plt.title("1000 times")
# plt.xlabel("Number of heads")
# plt.ylabel("Times")
# plt.show()


#Q2
# data = TossingCoin(200, 0.8)                            # create a class for 200 run times with 0.8 head probability
# experiment_result = data.experiment_result              # result is a list
# print("The number of heads is:", data.num_of_head())
# print("The longest run of heads is:", data.longestRunOfHead())
# labels, counts = np.unique(experiment_result, return_counts=True)   # let labels as "T" and "H", counts as # of occurs
# plt.bar(labels, counts, align="center")                             # let the label of bar shows in the middle
# plt.gca().set_xticks(labels)
# plt.xlabel("Experiment results")
# plt.ylabel("Counts")
# plt.show()



#Q3
def head_run(times):
    head_run = 0
    result = []
    result_index = -1
    for i in range(times):
        experiment_element = random.uniform(0, 1)  # generate a random number between 0 and 1
        if experiment_element >= 0.5:
            head_run += 1                          # length of head run increase 1
        else:
            if head_run > 0:
                result_index += 1
                result.append(head_run)
                head_run = 0                       # reset the head run
    return result


# result = head_run(100)                             # do 100 times
# labels, counts = np.unique(result, return_counts=True)   # let labels as 1, 2, 3 ... and counts as # of occurs
# plt.bar(labels, counts, align="center")                  # let the label of bar shows in the middle
# plt.gca().set_xticks(labels)
# plt.xlabel("run of heads")
# plt.ylabel("Counts")
# plt.show()


#Q4
def until_num():
    num = int(input("Enter a specific positive number of heads that you want: "))
    head_num = 0
    exp_num = 0
    while head_num < num:       # generate a while loop while the # of heads small than specified number.
        exp_num += 1
        experiment_element = random.uniform(0, 1)  # generate a random number between 0 and 1
        if experiment_element >= 0.5:              # if bigger or equal to 0.5, it's a head
            head_num += 1                          # length of head run increase 1
    return exp_num


print(until_num())

# --------------
# Importing header files
import numpy as np
print(path)

data_file = '/opt/greyatom/kernel-gateway/data/executor/attachments/account/b1/2a7f53f8-19f6-45c7-9d74-560da9338b1a/b51/d10ae496-b58a-4581-a727-949af1aa6e23/file.csv'

data = np.genfromtxt(data_file, delimiter=",", skip_header=1)

print(data)

print("\nType of data: \n\n", type(data))


# Append 'new_record' (given) to 'data' using "np.concatenate()" and store the new array in a variable called censu

# New record


new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]
new_record = np.array(new_record)
print(new_record)
type(new_record)

census = np.concatenate((data , new_record))
print(census)







# --------------
#Code starts here
age = census[:,0]
age = np.array(age)
print(age)
max_age = np.max(age)
print(max_age)
min_age = np.min(age)
print(min_age)
age_mean = np.mean(age)
print(age_mean)
age_std = np.std(age)
print(age_std)


# --------------
#Code starts here
race = census[0:,2]
print(race)
c_0,c_1,c_2,c_3,c_4 = race==0,race==1,race==2,race==3,race==4
race_0,race_1,race_2,race_3,race_4 = census[c_0], census[c_1], census[c_2], census[c_3], census[c_4]

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

minimum = min(len_0,len_1,len_2,len_3,len_4)
if minimum == len_0:
    minority_race = 0
elif minimum == len_1:
    minority_race = 1
elif minimum == len_2:
    minority_race = 2
elif minimum == len_3:
    minority_race = 3
elif minimum == len_4:
    minority_race = 4



# --------------
#Code starts here
senior_citizens = census[census[:,0]>60]
print(senior_citizens)
working_hours_sum = senior_citizens[:,6].sum()
print(working_hours_sum)
senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)
avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high = census[census[:,1]>10]
print(high)
low = census[census[:,1]<=10]
print(low)
avg_pay_high = np.mean(high[:,7])
avg_pay_low = np.mean(low[:,7])
print(avg_pay_high)
print(avg_pay_low)




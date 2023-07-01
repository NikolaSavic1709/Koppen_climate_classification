import os
def get_missed_indexes():
    folder_path = "../data/weather_index"  # Replace with the path to your folder
    # Iterate over each file in the folder
    a=[]
    for filename in os.listdir(folder_path):
        a.append(int(filename.split('.')[0]))

    a_set = set(a)

    all_numbers_set = set(range(1, 2001))

    not_present_set = all_numbers_set - a_set

    not_present_list = list(not_present_set)
    not_present_list.sort()
    print(not_present_list)



from functional_util import then, keep, remove, change
import math
import datetime
import os

def count_lines(file_location):
    num_lines = 0
    with open(file_location, 'r') as f:
        for line in f:
            num_lines += 1
    return num_lines

folder_location = os.getcwd() + "/sample_folder/"

print(folder_location)

total_line_count = \
    folder_location \
    | then | os.listdir \
    | then | remove(lambda name: 'bad' in name) \
    | then | change(lambda name: folder_location + name) \
    | then | change(count_lines) \
    | then | sum 


print(total_line_count)


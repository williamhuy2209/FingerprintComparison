import os
import math

def get_data_from_txt(txt_file_path):
    f = open(txt_file_path, 'r+')
    data = f.readlines()
    full_array = []
    for line in data:
        line = line.replace(" ", "")
        line_text = line.split(":")
        x = int(line_text[1].split(",")[0])
        y = int(line_text[1].split(",")[1])
        z = round(float(line_text[2]))
        full_array.append([x, y, z])
    f.close()
    return full_array

# def calculate_array(array):
#     for first_point in array:
# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    line_number = 0
    txt1_array = get_data_from_txt('02_left.txt')
    txt2_array = get_data_from_txt('02_right.txt')
    b = [0, 5, 9, 13, 25]
    a = b.pop(2)
    print(a)
    print(b)
    print(txt1_array)
    # print(math.degrees(math.atan2(math.fabs(x1-x2), math.fabs(y1-y2))))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
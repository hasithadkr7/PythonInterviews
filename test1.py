# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# Q1
# Given a list of integers L. Find the maximum length of a sequence
# of consecutive numbers that can be formed using elements from L.
# [5, 2, 99, 3, 4, 1, 100] -> max(|{99,100}|,|{1..5}|)

# ** particular number only belong to single sequence.

def find_maximum_length_sequence(num_list):
    visited = [False] * len(num_list)
    length = 0
    max_length = 0
    num_set = set(num_list)
    for i in range(0, len(num_list)):
        if not visited[i]:
            visited[i] = True
            length += 1

            forward = num_list[i]+1
            while forward in num_set:
                visited[num_list.index(forward)] = True
                length += 1
                forward += 1

            backward = num_list[i]-1
            while backward in num_set:
                visited[num_list.index(backward)] = True
                length += 1
                backward -= 1
            max_length = max(max_length, length)
            length = 0
    return max_length


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    arr = [5, 2, 99, 3, 4, 1, 100]
    print('max array length = ', find_maximum_length_sequence(arr))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

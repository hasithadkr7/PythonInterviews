def find_green_percentages(build_runs):
    print(build_runs)
    green_percentages = [0] * len(build_runs)
    for i in range(0, len(build_runs)):
        fail_count = 0
        for j in range(len(build_runs[i]) - 1, -1, -1):
            if not build_runs[i][j]:
                fail_count += 1
        green_percentages[i] = (len(build_runs[i])-fail_count)*100/len(build_runs[i])
    print(green_percentages)


if __name__ == '__main__':
    build_runs = [
        [True, True, True, False, False],
        [True, True, True, True, False],
        [True, True, True, True, True, True, False, False, False],
        [True, False, False, False, False, False],
        [True, True, True, True, True, True, True, True, True, True, True, True, False],
        [True, False],
        [True, True, True, True, False, False]
    ]
    find_green_percentages(build_runs)

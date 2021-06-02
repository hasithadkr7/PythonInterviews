def find_perfect_block(blocks, reqs):
    distance_matrix = [[len(blocks)]*len(reqs),
                       [len(blocks)]*len(reqs),
                       [len(blocks)]*len(reqs),
                       [len(blocks)]*len(reqs),
                       [len(blocks)]*len(reqs)]
    print(distance_matrix)
    for i in range(0, len(blocks)):
        print(blocks[i])
        for j in range(0, len(blocks)):
            for k in range(0, len(reqs)):
                if reqs[k] in blocks[j]:
                    if blocks[j][reqs[k]]:
                        if distance_matrix[i][k] == len(blocks):
                            distance_matrix[i][k] = abs(i - j)
                        else:
                            if distance_matrix[i][k] > abs(i - j):
                                distance_matrix[i][k] = abs(i - j)
    print(distance_matrix)


if __name__ == '__main__':
    reqs = ["gym", "school", "store", "office"]
    blocks = [{"gym": False,
               "school": True,
               "store": False},

              {"gym": True,
               "school": False,
               "store": False},

              {"gym": True,
               "school": True,
               "store": False},

              {"gym": False,
               "school": True,
               "store": False},

              {"gym": False,
               "school": True,
               "store": True}
              ]
    find_perfect_block(blocks, reqs)

# testing something


def splitList(urlList, num_core):
    part_len = len(urlList) // num_core
    mod = len(urlList) % num_core
    return [urlList[part_len * i:part_len * i + part_len + mod * (i == num_core - 1)] for i in range(num_core)]

test = list(range(41))
n = 8
print(splitList(test, n))

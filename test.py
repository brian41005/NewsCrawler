# testing something
# def splitList(urlList, num_core):
#     part_len = len(urlList) // num_core
#     mod = len(urlList) % num_core
# return [urlList[part_len * i:part_len * i + part_len + mod * (i ==
# num_core - 1)] for i in range(num_core)]

# test = list(range(41))
# n = 8
# print(splitList(test, n))
import datetime
Classification = ['world']
start = datetime.datetime.strptime('2016/12/1', '%Y/%m/%d')
end = datetime.datetime.strptime('2017/1/3', '%Y/%m/%d')

datelist = [(start + datetime.timedelta(days=x)).strftime('%Y/%b/%d').lower()
            for x in range(0, (end - start).days + 1)]
print(datelist)
for d in datelist:
    for c in Classification:
        print('https://www.theguardian.com/%s/%s/all' % (c, d))

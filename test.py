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
start = datetime.datetime.strptime('2016/12/1', '%Y/%m/%d')
end = datetime.datetime.strptime('2017/3/3', '%Y/%m/%d')

datelist = [(start + datetime.timedelta(days=x)).strftime('%Y/%b/%d').lower()
            for x in range(0, (end - start).days + 1)]
# for i in datelist:
#     print(i.strftime('%Y/%b/%d').lower())

    Classification = ['world']
    myList = generate_url_list('https://www.theguardian.com', 2010,
                               2016, Classification, end_month=5)

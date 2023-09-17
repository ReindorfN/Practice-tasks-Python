from important import fruits
from linear_search import search

start = fruits[0]
mid = len(fruits)//2
end = len(fruits)-1
mid_pos = fruits[mid]
while start <= end:
    if mid_pos > search:
        end = mid_pos - 1
    elif mid_pos < search:
        start = mid_pos + 1
    else:
        print(mid_pos)
seq = [1, 1, 1, 2, 3, 0]

result=1
max_result=0
last_seen=seq[0]

for i in seq[1:]:
    if i == last_seen:
        result += 1
    else:
        if result > max_result:
            max_result = result
        last_seen = i
        result = 1
if result > max_result:
    max_result = result

print(max_result)
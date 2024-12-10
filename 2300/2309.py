heights = []
for i in range(9):
    heights.append(int(input()))  # 난쟁이 9명의 키를 리스트로 입력

heights.sort() #난쟁이 9명의 키를 오름차순으로 정렬

for i in range(9):
    for j in range(i+1, len(heights)):
        if sum(heights) - heights[i] - heights[j] == 100:   # 9명의 키의 합에서 2명의 키의 합을 뺀 값이 100 일때
            a = heights[i]  
            b = heights[j]

heights.remove(a)
heights.remove(b)

for i in heights:
    print(i)
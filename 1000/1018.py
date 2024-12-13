n,m = map(int,input().split())
board = [input() for i in range(n)]  #체스판을 입력받는다.

def count_repaint(x, y): #x,y 는 8x8보드의 시작 좌표이다.
    # (x,y)를 시작으로 하는 8x8 영역을 체스판 두 패턴과 비교하여 최소로 다시 칠해야 하는 칸의 개수를 계산
    pattern1, pattern2 = 0, 0   # 규칙 1 : 맨 왼쪽 위 칸이 검정(B)로 시작/ 규칙 2: 맨 왼쪽 위 칸이 흰색(W)로 시작
    for i in range(8): #8x8칸의 행(위아래) 탐색
        for j in range(8): #8x8칸의 얄(왼오른쪽) 탐색
            #현재 칸의 색과 패턴 비교
            if (i + j) % 2 == 0:   #짝수 칸
                if  board [x+i][y+j] != 'B':  #패턴 1은 B로 시작
                    pattern1 +=1   # 다시 칠해야 함
                if board[x+i][y+j] != 'W': # 패턴 2는 w로 시작
                    pattern2 +=1   # 다시 칠해야 함
            
            else:   # 홀수 칸
                if board[x+i][y+j] != 'W': # 패턴 1은 W로 시작
                    pattern1 += 1
                if board[x+i][y+j] != 'B': #패턴 2는 B로 시작
                    pattern2 += 1
    
    # 두 패턴 중 더 적은 칸을 칠하는 경우 선택
    return min(pattern1, pattern2)

min_repaint = float('inf')  #칠해야 할 칸의 최소값 초기화

# 가능한 모든 8x8 영역의 시작점 탐색
for i in range(n-8+1):  #행 시작점 탐색
    for j in range(m-8+1):  # 열 시작점 탐색
        #(i,j)에서 시작하는 8x8 영역의 최소 칠하기 값 갱신
        min_repaint = min(min_repaint, count_repaint(i,j))

# 최종 결과 출력
print(min_repaint)





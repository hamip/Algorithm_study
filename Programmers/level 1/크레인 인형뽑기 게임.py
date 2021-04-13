# programmers.co.kr/learn/courses/30/lessons/64061

def solution(board, moves):
    basket = []  # stack for storing dolls
    popped_dolls = 0 # number of dolls that are popped

    for mv in moves:
        for i in range(len(board)):
        	# for each column
            if board[i][mv-1] != 0:
                if len(basket) == 0:
                    basket.append(board[i][mv-1])
                    
                elif basket[-1] == board[i][mv-1]:
                    basket.pop()
                    popped_dolls += 2  # two dolls are popped
                else:
                    basket.append(board[i][mv-1]) 

                board[i][mv-1] = 0
                break
                       
    return popped_dolls
  

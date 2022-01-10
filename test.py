





lottos1 = [2,4,0,0,7,8]
win_nums1 = [2,4,5,6,7,8]




def solution(lottos, win_nums):
    win_number = 0
    success_number = 0
    secret_number = 0
    for num1 in lottos :
        if num1 == 0 :
            secret_number += 1 # lottos 에 모르는 숫자의 개수를 구하는 함수
        else :
            for num2 in win_nums : 
                if num1 == num2 :  
                    success_number += 1 # 민우의 로또 번호와 당첨 번호가 같은 개수
                else :
                    pass

    number1 = []
    number = 1
    while number <= len(win_nums) :
        number1.append(number) 
        number += 1
    
           
    
    
    number1.reverse()

    win_number = number1[success_number - 1]
            
    top_score = number1[success_number - 1 + secret_number]
    answer = [win_number, top_score]
    return answer



print(solution(lottos1, win_nums1))

# 예시에 [a, b] 안에 들어가는것은 a등에서 b등까지 가능하다뜻 따라서 몇등이 가능한지 예상하는 코드를 작성해야함















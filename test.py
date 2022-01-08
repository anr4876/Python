





lottos1 = [1,3,4,5,6,7]
win_nums1 = [1,2,3,4,5,6]




def solution(lottos, win_nums):
    success_number = 0
    for num1 in lottos :
        for num2 in win_nums :
            if num1 == num2 :
                success_number += 1 # 민우의 로또 번호와 당첨 번호가 같은 개수
    number1 = []
    number = 0
    while number <= len(win_nums) :
        number1.append(number) 
        number += 1
    
    number1.reverse()
    
    for num in range(0,len(win_nums)+1)  :
        if success_number == num :
            win_number = number1[num] # 당첨 등수
        else :
            pass


    answer = [success_number, win_number]
    return answer



print(solution(lottos1, win_nums1))


















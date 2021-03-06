article1 = {"번호" : 1, "제목" : "소니의 축구교실", "내용" : "소니의 축구 강좌", "작성자" : "sony7"}
article2 = {"번호" : 2, "제목" : "류뚱의 야구교실", "내용" : "류뚱의 야구 강좌", "작성자" : "ryu99"}
article3 = {"번호" : 3, "제목" : "길동의 도술교술", "내용" : "길동의 도술 강좌", "작성자" : "hong123"}

article_list = [article1, article2, article3] # 게시물 저장소

user1 = {"아이디":"hong123", "비밀번호" : "1234", "이름" : "홍길동"}
user2 = {"아이디":"sony7", "비밀번호" : "7777", "이름" : "손흥민"}
user3 = {"아이디":"ryu99", "비밀번호" : "9999", "이름" : "류현진"}

user_list = [user1, user2, user3]

# 게시판 명령어 입력 : help

# add : 게시물 추가
# list : 게시물 목록 조회

# 게시판 명령어 입력 : list

# ==========  게시물 목록  =========
# 번호 : 1    제목 : 소니의 축구교실    작성자 : sony7
# 번호 : 2    제목 : 류뚱의 야구교실    작성자 : ryu99
# 번호 : 3    제목 : 길동의 도술교술    작성자 : hong123
# ================================= 

# 게시판 명령어 입력 : add

# 제목을 입력해주세요 : aaa
# 내용을 입력해주세요 : aaa

# 게시물이 등록되었습니다.

# 게시판 명령어 입력 : add

# 제목을 입력해주세요 : bbb
# 내용을 입력해주세요 : bbb

# 게시물이 등록되었습니다.

# 게시판 명령어 입력 : add

# 제목을 입력해주세요 : ccc
# 내용을 입력해주세요 : ccc

# 게시물이 등록되었습니다.

# 게시판 명령어 입력 : list

# ==========  게시물 목록  =========
# 번호 : 1    제목 : 소니의 축구교실
# 번호 : 2    제목 : 류뚱의 야구교실
# 번호 : 3    제목 : 길동의 도술교술
# 번호 : 4    제목 : aaa
# 번호 : 5    제목 : bbb
# 번호 : 6    제목 : ccc
# ================================= 

no = 3
while True :
    cmd = input("명령어를 입력해주세요 : ")

    if cmd == "help" :
        print("add  게시물 추가")
        print("list  게시물 목록 조회")
        print("exit  프로그램 종료")

    elif cmd == "add" :
        title = input("제목을 입력해주세요 : ")
        content = input("내용을 입력해주세요 : ")
        no += 1
        article = {"번호" : no, "제목" : title, "내용" : content, "작성자" : "익명"}
        article_list.append(article)


    elif cmd == "list" :

        print("======================= 게시물 목록 ======================")
        for article in article_list :
            print("번호 : {}     제목 : {}     작성자 : {}".format(article["번호"], article["제목"], article["작성자"]))
        print("==========================================================")



    elif cmd == "exit" :
        print("프로그램을 종료합니다.")
        break # 반복문 안에서 실행되면 무조건 그 순간 반복문을 종료.
    else  :
        print("알 수 없는 명령어입니다.")
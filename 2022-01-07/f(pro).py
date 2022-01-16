article1 = {"번호" : 1, "제목" : "소니의 축구교실", "내용" : "소니의 축구 강좌", "작성자" : "sony7"}
article2 = {"번호" : 2, "제목" : "류뚱의 야구교실", "내용" : "류뚱의 야구 강좌", "작성자" : "ryu99"}
article3 = {"번호" : 3, "제목" : "길동의 도술교술", "내용" : "길동의 도술 강좌", "작성자" : "hong123"}

article_list = [article1, article2, article3] # 게시물 저장소

user1 = {"아이디":"hong123", "비밀번호" : "1234", "이름" : "홍길동"}
user2 = {"아이디":"sony7", "비밀번호" : "7777", "이름" : "손흥민"}
user3 = {"아이디":"ryu99", "비밀번호" : "9999", "이름" : "류현진"}

user_list = [user1, user2, user3]



# ===================================================================
# 회원정보 가져오는 함수
# ===================================================================


def get_user_data(login_id) :
  is_exist = 1 # 1. 존재하지 않음.  2. 존재함
  for user in user_list :
    if user["아이디"] == login_id :     
      return user
  
  if is_exist == 1 :
    return None



# =====================================================================
# 회원가입 함수
# ======================================================================


def add_user(login_id, name, login_pw) :
  
  user = get_user_data(login_id)
  
  if user == None :
    new_user = {"아이디" : login_id, "비밀번호" : login_pw, "이름" : name}
    user_list.append(new_user)  
    print("회원 가입이 완료되었습니다.")
  else :
    print("이미 존재하는 아이디입니다.")


# =================================================================
# 로그인 함수
# =================================================================
def login(login_id, login_pw) :
  user = get_user_data(login_id)
  
  if user == None :
    print("없는 아이디입니다.")
  else :
    if user["비밀번호"] == login_pw :
      print("{}님 환영합니다!".format(user["이름"]))
      return True
    elif user["비밀번호"] != login_pw :
      print("비밀번호를 틀렸습니다.")
 
# ==================================================================== 
# 게시물 추가 및 조회 함수
# ====================================================================
def post_inquiry() :
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
            
# =====================================================================              
def first() :

    while True :

        menu = input("메뉴를 선택해주세요 (1. 회원가입, 2. 로그인, 3. 종료 : " )
        
        if menu == "1" :
            id = input("아이디를 입력해주세요 : " )
            pw = input("비밀번호를 입력해주세요 : ")
            name = input("이름을 입력해주세요 : ")
            
            add_user(id, name, pw)
            
        elif menu == "2" :
            id = input("아이디 : ")
            pw = input("비밀번호 : ")
            
            login(id, pw)
            
            if login(id, pw) == True :
                post_inquiry()

        elif menu == "3" :
            print("프로그램을 종료합니다.")
            break

first()
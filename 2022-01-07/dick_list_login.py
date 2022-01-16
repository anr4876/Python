# 딕셔너리 리스트를 이용해 유저정보를 출력해주세요.
user1 = {"아이디" : "hong123", "비밀번호" : "1234", "이름" : "홍길동"}
user2 = {"아이디" : "sony7"  , "비밀번호" : "7777", "이름" : "손흥민"}
user3 = {"아이디" : "ryu99"  , "비밀번호" : "9999", "이름" : "류현진"}

user_list = [user1, user2, user3]


# 모든 회원 아이디를 출력
# 출력 :
'''
hong123
sony7
ryu99
'''

for user in user_list:
  print(user["아이디"])

# hong123 아이디를 가진 회원의 이름 출력
# 출력 : 홍길동
# ======================================================================
# 아이디로 회원 정보 가져오기 함수
# ======================================================================
def get_user_data(login_id) :
  is_exist = 1 # 1. 존재하지 않음.  2. 존재함
  for user in user_list :
    if user["아이디"] == login_id :     
      return user
  
  if is_exist == 1 :
    return None

# ======================================================================
# 회원정보가 없을 때 출력하는 함수
# ======================================================================
def print_not_found() :
  print("없는 아이디입니다.")


# ======================================================================
# 아이디로 회원 이름 출력하는 함수
# ======================================================================

def find_user_name(login_id) :
  user = get_user_data(login_id) # user 나오든지 None이 나오든지
  if user != None :
    print(user["이름"])
  else :
    print_not_found()

# ======================================================================
# 아이디로 회원 찾아 비밀번호 수정하는 함수
# ======================================================================

def update_user_pass(login_id, new_pass) :
  user = get_user_data(login_id)
  
  if user != None :
    user["비밀번호"] = new_pass
  else :
    print_not_found()

# ====================================================================== 
# 회원 전체 출력 함수
# ====================================================================== 
def print_all_users() :
  for user in user_list :
    print("아이디 : {},  비밀번호 : {},  이름 : {}"
        .format(user["아이디"], user["비밀번호"], user["이름"]))

# ====================================================================== 
# 회원 가입 함수
# ====================================================================== 
def add_user(login_id, name, login_pw) :
  
  user = get_user_data(login_id)
  
  if user == None :
    new_user = {"아이디" : login_id, "비밀번호" : login_pw, "이름" : name}
    user_list.append(new_user)  
    print("회원 가입이 완료되었습니다.")
  else :
    print("이미 존재하는 아이디입니다.")
# ================================================================================
def login(login_id, login_pw) :
  user = get_user_data(login_id)
  
  if user == None :
    print("없는 아이디입니다.")
  else :
    if user["비밀번호"] == login_pw :
      print("{}님 환영합니다!".format(user["이름"]))
    elif user["비밀번호"] != login_pw :
      print("비밀번호를 틀렸습니다.")

# ================================================================================

# 회원 아이디로 회원 이름 출력
find_user_name("hong123")  
find_user_name("ryu99")  
find_user_name("123123")  

# hong123 아이디를 가진 회원의 비밀번호를 3333으로 수정 후 모든 회원 정보 출력
# 출력 : 홍길동의 비밀번호가 3333으로 수정되어 출력되어야 함
print_all_users()
update_user_pass("hong123", "3333")
print_all_users()


# 기능을 구현 > 함수 (바텀업)
# 함수가 있다고 가정하고 사용 > 함수를 구현 (탑다운)

# 회원가입
# 아이디가 chacha, 이름 차태진, 비밀번호 c123인 회원을 추가
print("===== 가입 전 =====")
print_all_users()
add_user("chacha", "차태진", "c123")
print("===== 가입 후 =====")
print_all_users()


# 아이디가 hong123, 이름 홍길순, 비밀번호 h1234 인 회원추가
# 아이디가 중복될 시 추가 거부.
add_user("hong123", "홍길순", "h1234")


# 로그인 
# 아이디, 비밀번호 
login("hong123", "3333")

# 프로그램 기본 구조
# 유저 인터페이스

# 메뉴 선택
# 1. 회원가입, 2. 로그인, 3. 종료



# for, while 

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

  elif menu == "3" :
    print("프로그램을 종료합니다.")
    break


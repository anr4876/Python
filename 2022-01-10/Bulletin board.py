# 로그인 성공시에만 게시판 기능 활성화 하기


# 아이디   : wefsd
# 비밀번호 : 2134
# 잘못된 아이디입니다.

# 아이디   : hong123
# 비밀번호 : 566
# 비밀번호를 틀렸습니다.

# 아이디   : hong123
# 비밀번호 : 1234

# 홍길동님 안녕하세요! 게시판 기능을 시작합니다!
# 게시판 명령어 입력 :help 
# add : 게시물 추가
# list : 게시물 목록 조회 

# ==========  게시물 목록  =========
# 번호 : 1    제목 : 소니의 축구교실
# 번호 : 2    제목 : 류뚱의 야구교실
# 번호 : 3    제목 : 길동의 도술교술
# ================================= 

# 게시판 명령어 입력 : update
# 수정할 게시물 번호를 입력 : 4
# 없는 게시물입니다.

# 게시판 명령어 입력 : update
# 수정할 게시물 번호를 입력 : 3
# 제목 : 제목3 
# 내용 : 내용3
# 수정이 완료되었습니다.
# ==========  게시물 목록  =========
# 번호 : 1    제목 : 소니의 축구교실
# 번호 : 2    제목 : 류뚱의 야구교실
# 번호 : 3    제목 : 제목3
# ================================= 

#============================================================= 전역변수
article1 = {"번호" : 1, "제목" : "소니의 축구교실", "내용" : "소니의 축구 강좌", "작성자" : "sony7"}
article2 = {"번호" : 2, "제목" : "류뚱의 야구교실", "내용" : "류뚱의 야구 강좌", "작성자" : "ryu99"}
article3 = {"번호" : 3, "제목" : "길동의 도술교술", "내용" : "길동의 도술 강좌", "작성자" : "hong123"}

article_list = [article1, article2, article3] # 게시물 저장소

user1 = {"아이디":"hong123", "비밀번호" : "1234", "이름" : "홍길동"}
user2 = {"아이디":"sony7", "비밀번호" : "7777", "이름" : "손흥민"}
user3 = {"아이디":"ryu99", "비밀번호" : "9999", "이름" : "류현진"}

user_list = [user1, user2, user3]

no = 4


#============================================================= 함수

#  article_list에 article1.txt ~ article3.txt 파일 내용을 읽어와 딕셔너리로 저장

# 로그인 성공여부 체크 함수
def login_check(id, pw) :
  for user in user_list :
    if user['아이디'] == id :
      if user['비밀번호'] == pw :
        print("{}님 반갑습니다!".format(user['이름']))
        return True
      else :
        print("비밀번호를 틀렸습니다.")
        return False
    
  print("없는 아이디입니다.")
  return False

# 게시물 목록을 출력하는 함수
def print_articles() :
  print("========== 게시물 목록 ==========")
  for article in article_list :
    print("번호 : {}    제목 : {}".format(article['번호'], article['제목']))
  print("==================================")

# 게시물 한개 추가하는 함수
def add_article() :
  global no # 전역변수 사용
  title = input('제목을 입력해주세요 : ')
  body = input('내용을 입력해주세요 : ')
  article = {"번호" : no, "제목" : title, "내용" : body, "작성자" : login_id}
  article_list.append(article)
  no += 1

# 게시물 번호 받아서 해당 게시물을 반환해주는 함수
def get_article_by_article_no() :
  ano = int(input('게시물 번호를 선택해주세요 : '))

  target = None
  for article in article_list :
    if article['번호'] == ano :
      target = article
      break

  return target

# 선택한 게시물 수정하는 함수
def update_article() :
  target = get_article_by_article_no()
  if target == None :
    print('없는 게시물 번호입니다.')
  else :
    title = input('수정할 제목 :')    
    body = input('수정할 내용 :')
    target['제목'] = title
    target['내용'] = body

# 선택한 게시물 삭제하는 함수
def delete_article() :
  target = get_article_by_article_no()

  if target == None :
    print('없는 게시물 번호입니다.')
  else :
    article_list.remove(target)
    print('삭제가 완료되었습니다')
    
# 선택한 게시물을 상세보기하는 함수
def detail_article() :
  target = get_article_by_article_no()

  if target == None :
    print('없는 게시물 번호입니다.')
  else :
    print("=========== 게시물 상세 ==========")
    print("번호 :", target['번호'])
    print("제목 :", target['제목'])
    print("내용 :", target['내용'])
    print("작성자 :", target['작성자'])
    print("=================================")

# ==========  게시물 상세  =========
# 번호 : 1 
# 제목 : 류뚱의 야구교실
# 내용 : 류뚱의 야구 강좌
# 작성자 : ryu99
# ----- 댓글 -----
# ================================= 

# 게시판 명령어 도움말 함수
def print_help() :
  print('add : 게시물 추가')      
  print('list : 게시물 목록 조회')
  print('update : 게시물 수정')
  print('delete : 게시물 삭제')
  print('detail : 게시물 상세 조회')


# 게시물 파일 생성 함수

# 게시물 파일 읽기 함수

# ===============================================================

login_id = input("아이디를 입력해주세요 : ")
login_pw = input("비밀번호를 입력해주세요 : ")

login_result = login_check(login_id, login_pw); # 성공? 실패?

if login_result :
  while True :
    cmd = input("명령어를 입력해주세요 : ")
    if cmd == 'exit' :
      print("프로그램을 종료합니다.")
      break
    elif cmd == 'help' :
      print_help()

    elif cmd == "list" :
      print_articles()

    elif cmd == 'add' :
      add_article()

    elif cmd == 'update' :
      update_article()
    
    elif cmd == 'delete' :
      delete_article()

    elif cmd == "detail" :
      detail_article()
      



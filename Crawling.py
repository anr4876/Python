import requests

URL = 'https://page.kakao.com/main?categoryUid=11&subCategoryUid=86'
raw = requests.get(URL)
#print(raw)요청 성공 여부 출력

print(raw.text)#HTML 코드 출력


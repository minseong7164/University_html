# 변수 선언 부분
inText = ""
encrypText, decrypText= "", ""
key = 0

# 메인 코드 부분
if __name__ == "__main__":
    inText = input("문자열을 입력하세요:")
    key = int(input("키 값을 입력하세요: "))

    for ch in inText :
        encrypText += chr(ord(ch) ^ key)
    print("\n암호화된 문자열---> ", encrypText)

for ch in encrypText:
    decrypText += chr(ord(ch) ^ key)
print("복호화된 문자열---> ", decrypText)
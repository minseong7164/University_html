password = ""
special_chars = "~!@#$%^&*_-"
length_ok_8 = False
length_ok_12 = False
upper_ok = False
lower_ok = False
digit_ok = False
special_ok = False

password = input("비밀번호를 입력하세요: ")

if len(password) >= 12:
    length_ok_12 = True
elif len(password) >= 8:
    length_ok_8 = True

for char in password:
    if 'A' <= char <= 'Z':
        upper_ok = True
    elif 'a' <= char <= 'z':
        lower_ok = True
    elif '0' <= char <= '9':
        digit_ok = True
    elif char in special_chars:
        special_ok = True

if length_ok_12 and upper_ok and lower_ok and digit_ok and special_ok:
    print("비밀번호 수준: 강력한 비밀번호입니다.")
elif length_ok_8 and ((upper_ok and lower_ok) or (upper_ok and digit_ok) or
(lower_ok and digit_ok)) :
    print("비밀번호 수준: 보통 비밀번호입니다.")
else:
    print("비밀번호 수준: 약한 비밀번호입니다.")
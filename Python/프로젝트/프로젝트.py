import os

FILE_NAME = "db_bank.txt"

users = []
banks = []
records = []


# -------------------------
# 파일 불러오기
# -------------------------
def load_file():
    if not os.path.exists(FILE_NAME):
        return

    with open(FILE_NAME, "r", encoding="utf-8") as f:
        section = None

        for line in f:
            line = line.strip()

            if line == "[USERS]":
                section = "users"
                continue
            elif line == "[BANKS]":
                section = "banks"
                continue
            elif line == "[RECORDS]":
                section = "records"
                continue

            if section == "users" and line:
                uid, name = line.split(",")
                users.append({"id": int(uid), "name": name})

            elif section == "banks" and line:
                bid, name = line.split(",")
                banks.append({"id": int(bid), "name": name})

            elif section == "records" and line:
                uid, bid, date, type_, amount, category = line.split(",")
                records.append({
                    "user_id": int(uid),
                    "bank_id": int(bid),
                    "date": date,
                    "type": type_,
                    "amount": int(amount),
                    "category": category
                })


# -------------------------
# 파일 저장
# -------------------------
def save_file():
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        f.write("[USERS]\n")
        for u in users:
            f.write(f"{u['id']},{u['name']}\n")

        f.write("[BANKS]\n")
        for b in banks:
            f.write(f"{b['id']},{b['name']}\n")

        f.write("[RECORDS]\n")
        for r in records:
            f.write(f"{r['user_id']},{r['bank_id']},{r['date']},{r['type']},{r['amount']},{r['category']}\n")


# -------------------------
# 사용자 등록
# -------------------------
def add_user():
    name = input("사용자 이름: ")

    for u in users:
        if u["name"] == name:
            print("이미 존재하는 사용자입니다.")
            return

    new_id = len(users) + 1
    users.append({"id": new_id, "name": name})
    print("사용자 등록 완료")


# -------------------------
# 은행 등록
# -------------------------
def add_bank():
    name = input("은행 이름: ")

    for b in banks:
        if b["name"] == name:
            print("이미 존재하는 은행입니다.")
            return

    new_id = len(banks) + 1
    banks.append({"id": new_id, "name": name})
    print("은행 등록 완료")


# -------------------------
# 선택 함수
# -------------------------
def select_user():
    for u in users:
        print(f"{u['id']}. {u['name']}")
    return int(input("사용자 선택: "))


def select_bank():
    for b in banks:
        print(f"{b['id']}. {b['name']}")
    return int(input("은행 선택: "))


# -------------------------
# 거래 (입금/출금)
# -------------------------
def transaction(type_):
    if not users or not banks:
        print("사용자와 은행을 먼저 등록하세요.")
        return

    uid = select_user()
    bid = select_bank()

    date = input("날짜 (YYYY-MM-DD): ")
    amount = int(input("금액: "))
    category = input("내용: ")

    records.append({
        "user_id": uid,
        "bank_id": bid,
        "date": date,
        "type": type_,
        "amount": amount,
        "category": category
    })

    print("거래 완료")


# -------------------------
# ID → 이름 변환
# -------------------------
def get_user_name(uid):
    for u in users:
        if u["id"] == uid:
            return u["name"]
    return "?"


def get_bank_name(bid):
    for b in banks:
        if b["id"] == bid:
            return b["name"]
    return "?"


# -------------------------
# 전체 거래 조회
# -------------------------
def show_records():
    print("\n[전체 거래 내역]")
    print("-" * 60)
    print(f"{'사용자':<10}{'은행':<10}{'유형':<6}{'금액':<10}{'내용':<10}")
    print("-" * 60)

    for r in records:
        uname = get_user_name(r["user_id"])
        bname = get_bank_name(r["bank_id"])
        sign = "+" if r["type"] == "입금" else "-"

        print(f"{uname:<10}{bname:<10}{r['type']:<6}{sign}{r['amount']:<9}{r['category']:<10}")

    print("-" * 60)


# -------------------------
# 사용자 거래 조회
# -------------------------
def show_user_records():
    uid = select_user()

    print("\n[사용자 거래 내역]")
    print("-" * 60)

    for r in records:
        if r["user_id"] == uid:
            uname = get_user_name(r["user_id"])
            bname = get_bank_name(r["bank_id"])
            sign = "+" if r["type"] == "입금" else "-"

            print(f"{uname} | {bname} | {r['type']} | {sign}{r['amount']} | {r['category']}")

    print("-" * 60)


# -------------------------
# 계좌 요약
# -------------------------
def show_summary():
    uid = select_user()

    income = 0
    expense = 0

    for r in records:
        if r["user_id"] == uid:
            if r["type"] == "입금":
                income += r["amount"]
            else:
                expense += r["amount"]

    print(f"\n총 입금: {income}")
    print(f"총 출금: {expense}")
    print(f"잔액: {income - expense}")


# -------------------------
# 은행별 잔액
# -------------------------
def show_balance_by_bank():
    uid = select_user()

    print("\n[은행별 잔액]")
    print("-" * 40)

    for b in banks:
        balance = 0

        for r in records:
            if r["user_id"] == uid and r["bank_id"] == b["id"]:
                if r["type"] == "입금":
                    balance += r["amount"]
                else:
                    balance -= r["amount"]

        print(f"{b['name']}: {balance}")

    print("-" * 40)


# -------------------------
# 메뉴
# -------------------------
def menu():
    while True:
        print("\n====== 🏦 DB 은행 시스템 ======")
        print("1. 사용자 등록")
        print("2. 은행 등록")
        print("3. 입금")
        print("4. 출금")
        print("5. 전체 거래 조회")
        print("6. 계좌 요약")
        print("7. 은행별 잔액 조회")
        print("8. 사용자 거래 조회")
        print("9. 저장")
        print("0. 종료")

        choice = input("선택: ")

        if choice == "1":
            add_user()
        elif choice == "2":
            add_bank()
        elif choice == "3":
            transaction("입금")
        elif choice == "4":
            transaction("출금")
        elif choice == "5":
            show_records()
        elif choice == "6":
            show_summary()
        elif choice == "7":
            show_balance_by_bank()
        elif choice == "8":
            show_user_records()
        elif choice == "9":
            save_file()
        elif choice == "0":
            save_file()
            print("프로그램 종료")
            break
        else:
            print("잘못된 입력입니다.")


# -------------------------
# 실행
# -------------------------
load_file()
menu()
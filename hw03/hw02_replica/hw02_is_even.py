#반복문하고 조건문
def main():
    total = 0

    for i in range(1, 101):
        # total = total + i
        if i % 2 == 0:
            total += i
    print(f"1부터 100까지 짝수의 합은 {total}입니다.")
#지능형 리스트
    even_100 = [i for i in range(1,101) if i % 2 == 0]
    total = 0
    for i in even_100:
        total += i
    print(f"1부터 100까지 짝수의 합은 {total}입니다.")
#수학함수
    total = sum(range(2,101,2))
    print(f"1부터 100까지 짝수의 합은 {total}입니다.")

if __name__ == "__main__":
    main()
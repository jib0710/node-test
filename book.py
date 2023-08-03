import random

word:list = ['apple', 'mango', 'banana', 'melon', 'kiwi', 'peach', 'grape', 'coconut']

index:int = random.randint(0,(len(word)))

fruit:str = word[index]

number_of_guess = 0 
count = 3

while True:
    print(f"fruit -> {fruit}")
    guess = input("과일이름을 입력하세요 : ")
    number_of_guess += 1
    count -= 1
    if fruit == guess:
        print(f"축하합니다! {number_of_guess}회 만에 과일을 맞췄습니다.")
        break
    else:
        print(f"틀렸습니다. 기회 {count}번 남았습니다.")
        if count == 0:
            print("기회가 없습니다.")
            break
        
        
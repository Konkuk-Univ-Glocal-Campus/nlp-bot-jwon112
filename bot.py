import random

# This list contains the random responses (you can add your own or translate them into your own language too)
random_responses = ["그것 참 흥미롭네요., 부디 더 얘기해주세요.",
                    "그렇군요. 계속하세요.",
                    "왜 그런 말을 하세요?",
                    "참 이상한 하루에요, 그렇죠?",
                    "주제를 바꿔보죠.",
                    "어제밤 경기는 보았나요?"]

print("안녕하세요, 저는 단순한 로봇 마빈이에요")
print("'언제든지 '잘가'라고 타이핑하면 당신은 대화를 끝마칠 수 있어요.'")
print("각 응답을 타이핑 한 후에 'enter'를 눌러주세요.")
print("안녕하세요?")

while True:
    # wait for the user to enter some text
    user_input = input("> ")
    if user_input.lower() == "잘가":
        # if they typed in 'bye' (or even BYE, ByE, byE etc.), break out of the loop
        break
    else:
        response = random.choices(random_responses)[0]
    print(response)

print("당신과 얘기할 수 있어서 즐거웠어요, 잘가요!")

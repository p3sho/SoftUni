import re

messages_count = int(input())

patern = re.compile(r"^([$%])(?P<tag>[A-Z][a-z]{2,})\1: "
                     r"\[(?P<num1>[\d]+)"
                     r"\]\|\[(?P<num2>[\d]+)"
                     r"\]\|\[(?P<num3>[\d]+)\]\|$")


for p in range(messages_count):
    current_message = input()
    result = list(patern.finditer(current_message))

    for res in result:
        successfull_decrypt = f'{chr(int(res["num1"]))}{chr(int(res["num2"]))}{chr(int(res["num3"]))}'
        print(f"{res['tag']}: {successfull_decrypt}")

    if not result:
        print("Valid message not found!")


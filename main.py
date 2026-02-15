from art import logo
print(logo)
def add(n1, n2):
    return n1 + n2
def sub(n1,n2):
    return n1 - n2
def mul(n1,n2):
    return n1 * n2
def div(n1,n2):
    if n2 != 0:
        return n1 / n2
    else:
        return "Cannot Divide by Zero"

operation = {
    "+" : add,
    "-" : sub,
    "*" : mul,
    "/" : div,
}



def calculator():

    first_num = float(input("Type your First Number: "))
    continue_calc = True
    while continue_calc == True:
        for choice in operation:
            print(choice)
        choice = input("Pick an Operation: ")
        second_num = float(input("Type your Second Number: "))
        answer = operation[choice](first_num, second_num)
        print(f"{first_num} {choice} {second_num} = {answer}")
        yes_no_leave = input(f"Type 'y' to continue with {answer}, or type 'n' to start new calculation. To leave type 'l': ").lower()
        if yes_no_leave == "y":
            first_num = answer
            continue_calc = True
        elif yes_no_leave == 'n':
            continue_calc = False
            print("\n"*20)
            print("Start a New Calculation!: ")
            calculator()
        elif yes_no_leave == 'l':
            print("Thank You, Visit Again ❤️")
            continue_calc = False
calculator()
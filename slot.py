# SLOT MACHINE PROGRAM

import random

MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

# dictionary containing symbols of slot machine
symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

#dictionary containing the value of each symbol in slot machine
symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}


def check_winnnings(columns, lines, bet, values):
    winnings = 0
    winnings_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winnings_lines.append(line + 1)
    
    return winnings, winnings_lines


def slot_spin(rows, cols, symbols):
    all_symbols = []

    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)

        columns.append(column)

    return columns

#displays the "screen" of the slot machine
def display(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end= " | ")
            else:
                print(column[row], end = "")
        
        print()

#function used to gather user input for deposit
def deposit():

    #continues running until valid amount is entered
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0: 
                break #valid case thus break
            else:
                print("Enter a valid amount")
        else:
            print("Enter a number")

    return amount

#function used to gather user input for number of lines user wants to bet on
def getNumberOfLines():
    while True:
        lines = input("Enter number of lines you want to bet on (1 - " + str(MAX_LINES) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 0 < lines <= MAX_LINES:
                break
            else:
                print("Number of lines must be between 1 and " + str(MAX_LINES))
        else:
            print("Enter a valid number")

    return lines

# function used to gather user input for betting amount
def getBetAmount():
    while True:
        amount = input("What would you like to bet on each line? $")
        if amount.isdigit():
            amount = int(amount)
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Bet must be between ${MIN_BET} - ${MAX_BET}")
        else:
            print("Enter a valid number")

    return amount
    
def game(balance):
    lines = getNumberOfLines()

    while True:
        bet = getBetAmount()
        totalBet = bet * lines

        if totalBet > balance:
            print(f"You do not have enough in your balance (${balance}) to bet ${totalBet}")
        else:
            break
  
    print(f"You are betting ${bet} on {lines} lines. Your total bet is ${totalBet}")
    
    slots = slot_spin(ROWS,COLS, symbol_count)
    display(slots)
    winnings, winning_lines = check_winnnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}!")
    print(f"You won on lines:", *winning_lines)

    return winnings - totalBet

# main driver function
def main():
    balance = deposit()
    while True:
        print(f"Current Balance is ${balance}")
        answer = input("Press Enter to play (q to quit).")
        if answer == 'q':
            print(f"You are leaving with ${balance}")
            break
        balance += game(balance)

   

main()
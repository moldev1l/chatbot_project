def check_winner(area):
    if area[0][2] == "Кресло" and area[1][2] == "Шкаф":
        return True
    else:
        return False


def print_area(area):
    for i in area:
        print(i)


furniture = [["Стол", "Стул", "Шкаф"], ["Стул", "*", "Кресло"]]
print_area(furniture)
while not check_winner(furniture):
    current_row = int(input("из какой строки взять 0,1 "))
    current_column = int(input("из какого столбика взять 0,1,2 "))

    next_row = int(input("в какую строку поставить 0,1 "))
    next_column = int(input("в какой столбик поставить 0,1,2 "))
    item = furniture[current_row][current_column]

    if furniture[next_row][next_column] != "*":
        print("Ход невозможен")
    else:
        furniture[next_row][next_column] = item
        furniture[current_row][current_column] = "*"

    print_area(furniture)




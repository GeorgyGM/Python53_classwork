import qwerty
journal=[]

subjects=["рус", "мат", "лит", "физ"]

def add_subject(subject_name):
    subject_name = subject_name[:3]
    subjects.append(subject_name)
    for i in journal:
        i.append(0)

def add_student():
    journal.append([])
    for i in subjects:
        journal[len(journal)-1].append(0)

def show_journal():
    print("№", end="")
    for i in subjects:
        print(f"\t| {i}", end="")
    print()
    for i in range(len(journal)):
        print(i + 1, end="\t")
        for j in range(len(journal[i])):
            print("| ", journal[i][j], end="\t")
        print()

def change_mark(number, subject, mark):
    index = subjects.index(subject)
    journal[number-1][index]=mark

def remove_student(index):
    journal.pop(index-1)

def best_student():
    best_index=-1
    best_summa=0
    for i in range (len(journal)):
        if sum(journal[i])>best_summa:
            best_index=i
    return best_index+1

def start_menu():
    variant = int(input(
        '''
        1. вывод журнала
        2. добавление студента
        3. добавление дисциплины
        4. удаление студента
        5. удаление дисциплины
        6. замена оценки
        7. выйти
        '''
    ))
    match variant:
        case 1: show_journal()
        case 2: add_student()
        case 3:
            add_subject(input("введите название дисциплины: "))
        case 4:
            remove_student(int(input("введите номер студента")))
        case 6:
            number = int(input("введите номер студента"))
            subject = input("введите название дисциплины: ")
            mark = int(input("введите оценку: "))
            change_mark(number, subject, mark)
        case 7:
            exit()
        case _: start_menu()


if __name__ == '__main__':
    while True:
        start_menu()




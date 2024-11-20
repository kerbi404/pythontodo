tasks = []  # Globalna lista zadań

def save_tasks_to_file(filename="tasks.txt"):
    with open(filename, "w") as file:
        for task in tasks:
            file.write(f"{task['task']}|{task['deadline']}|{task['priority']}\n")
    print("Zadania zostały zapisane do pliku.")

def load_tasks_from_file(filename="tasks.txt"):
    try:
        with open(filename, "r") as file:
            global tasks
            tasks = []
            for line in file.readlines():
                task_name, deadline, priority = line.strip().split("|")
                task = {
                    "task": task_name,
                    "deadline": deadline,
                    "priority": priority
                }
                tasks.append(task)
        print("Zadania zostały wczytane z pliku.")
    except FileNotFoundError:
        print("Plik z zadaniami nie istnieje. Rozpoczynam od pustej listy.")

def show_menu():  # Wyświetla menu
    print("\n--- Menu ---")
    print("1. Dodaj zadanie")
    print("2. Wyświetl zadania")
    print("3. Usuń zadanie")
    print("4. Wyjdź")

def add_task():    # Dodaje zadania
    task_name = input("Wpisz nowe zadanie: ")

    # Wprowadzanie daty (rok, miesiąc, dzień)
    while True:
        try:
            year = int(input("Wpisz rok (YYYY): "))
            month = int(input("Wpisz miesiąc (1-12): "))
            if month < 1 or month > 12:
                print("Miesiąc musi być w zakresie 1-12.")
                continue
            day = int(input("Wpisz dzień (1-31): "))

            # Walidacja dni w zależności od miesiąca
            if month == 2:
                if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):   # Przestępny rok
                    if day < 1 or day > 29:
                        print("Luty w roku przestępnym ma maksymalnie 29 dni.")
                        continue
                    else:
                        if day < 1 or day > 28:
                            print("Luty w roku nieprzestępnym ma maksymalnie 28 dni.")
                            continue
            elif month in [4, 6, 9, 11]: # Miesiące mające 30 dni
                if day < 1 or day > 30:
                    print(f"Miesiąc {month} ma maksymalnie 30 dni.")
                    continue
            else:
                if day < 1 or day > 31:
                    print(f"Miesiąc {month} ma maksymalnie 31 dni.")
                    continue
            # Data do kiedy
            deadline = f"{year}-{month:02d}-{day:02d}"
            break
        except ValueError:
            print("Nieprawidłowa wartość! Wprowadź liczby dla daty.")

    # Wprowadzanie priorytetu (1, 2, 3) i konwersja na tekst (nauka)
    while True:
        try:
            priority = int(input("Wpisz priorytet (1 - wysoki, 2 - średni, 3 - niski): "))
            if priority == 1:
                priority_text = "Wysoki"
                break
            if priority == 2:
                priority_text = "Średni"
                break
            if priority == 3:
                priority_text = "Niski"
                break
            else:
                print("Priorytet musi być 1, 2 lub 3.")
        except ValueError:
            print("Nieprawidłowy priorytet! Wpisz liczbę (1, 2, 3).")

    task = {
        "task": task_name,
        "deadline": deadline,
        "priority": priority_text
    }
    tasks.append(task)
    save_tasks_to_file()
    print(f"Zadanie '{task_name}' zostało dodane.")

def view_tasks():   # Wyświetla zadania
    if tasks:
        print("\nTwoje zadania:")
        for idx, task in enumerate(tasks, start=1):  # Numerowanie zadań
            print(f"{idx}. {task['task']} - Termin: {task['deadline']} - Priorytet: {task['priority']}")
    else:
        print("Nie masz jeszcze żadnych zadań!")

def delete_task():
    view_tasks()  # Wyświetlamy zadania
    if tasks:    # Sprawdzamy, czy lista nie jest pusta
        try:
            task_num = int(input("Podaj numer zadania do usunięcia: "))
            if 0 < task_num <= len(tasks):  # Sprawdzamy, czy numer jest poprawny
                removed_task = tasks.pop(task_num - 1)  # Usuwamy zadanie za pomoca .pop
                save_tasks_to_file()
                print(f"Usunięto zadanie: {removed_task['task']}")
            else:
                print("Nieprawidłowy numer!")
        except ValueError:
            print("Wprowadź poprawny numer!")

# Ładowanie zadań z pliku przy starcie programu
load_tasks_from_file()

while True:
    show_menu()  # Wyświetlamy menu
    choice = input("Wybierz opcję: ")

    if choice == "1":
        add_task()
    elif choice == "2":
        view_tasks()
    elif choice == "3":
        delete_task()
    elif choice == "4":
        print("Do zobaczenia następnym razem!")
        break
    else:
        print("Niepoprawny wybór, spróbuj ponownie.")

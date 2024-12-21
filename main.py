
# class Transport: 
#     def __init__(self, brand, model, year): 
#         self.brand = brand 
#         self.model = model 
#         self.year = year 
 
#     def get_info(self): 
#         return f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}" 
 
#     def honk(self): 
#         return "Generic transport sound!" 
 
 
# class Car(Transport): 
#     def __init__(self, brand, model, year, fuel_type): 
#         super().__init__(brand, model, year) 
#         self.fuel_type = fuel_type 
 
#     def get_info(self): 
#         return f"{super().get_info()}, Fuel Type: {self.fuel_type}" 
 
#     def honk(self): 
#         return "Beep-beep!" 
 
 
# class Bicycle(Transport): 
#     def __init__(self, brand, model, year, gear_count): 
#         super().__init__(brand, model, year) 
#         self.gear_count = gear_count 
 
#     def get_info(self): 
#         return f"{super().get_info()}, Gear Count: {self.gear_count}" 
 
#     def honk(self): 
#         return "Ding-ding!" 
 
 
# if __name__ == "__main__": 
  
#     car = Car("Mercedes-AMG", " CLE Coupe", 2024, "Gasoline") 
#     print(car.get_info())   
#     print(car.honk())       
 
#     bicycle = Bicycle("Giant", "Escape 3", 2022, 21) 
#     print(bicycle.get_info())   
#     print(bicycle.honk())




import os

def create_file_if_not_exists(filename):
    """Перевіряє наявність файлу і створює його, якщо він відсутній."""
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            pass

def add_contact(filename):
    """Додає новий контакт у файл."""
    name = input("Введіть ім'я: ").strip()
    phone = input("Введіть номер телефону: ").strip()
    email = input("Введіть електронну пошту: ").strip()

    with open(filename, 'a') as file:
        file.write(f"Ім'я: {name}, Телефон: {phone}, Електронна пошта: {email}\n")
    print("Контакт успішно додано!\n")

def view_contacts(filename):
    """Відображає список контактів з файлу."""
    with open(filename, 'r') as file:
        contacts = file.readlines()
        if contacts:
            print("Список контактів:")
            for contact in contacts:
                print(contact.strip())
        else:
            print("Список контактів порожній.\n")

def main():
    filename = "contacts.txt"
    create_file_if_not_exists(filename)

    while True:
        print("\nОберіть дію:")
        print("1. Додати новий контакт")
        print("2. Переглянути список контактів")
        print("3. Вийти")

        choice = input("Ваш вибір: ").strip()

        if choice == '1':
            add_contact(filename)
        elif choice == '2':
            view_contacts(filename)
        elif choice == '3':
            print("Вихід з програми. До побачення!")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.\n")

if __name__ == "__main__":
    main()

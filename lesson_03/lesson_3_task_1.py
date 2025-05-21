from user import User

my_user = User("Оксана", "Медведева")

my_user.print_first_name()  # Ожидаемый результат: "Оксана"
my_user.print_last_name()   # Ожидаемый результат: "Медведева"
my_user.print_full_name()   # Ожидаемый результат: "Оксана Медведева"

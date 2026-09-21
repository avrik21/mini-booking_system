from client.ui import Ui
from utils import use_func, input_choice
ui = Ui()

while True:
    use_func(ui.show_menu)
    choice = input_choice(7)
    if choice == 1:
        use_func(ui.request_add_client)
    elif choice == 2:
        use_func(ui.request_add_service)
    elif choice == 3:
        use_func(ui.request_add_appoitment)
    elif choice == 4:
        use_func(ui.request_show_appoitments)
    elif choice == 5:
        use_func(ui.request_find_appoitment)
    elif choice == 6:
        use_func(ui.request_cancel_appoitment)
    elif choice == 7:
        use_func(ui.request_change_status)
    elif choice == 8:
        use_func(ui.request_income)
    elif choice == 0:
        print("Спасибо за работу!!")
        break
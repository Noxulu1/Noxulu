from tkinter import Tk, ttk   # импортируем классы Tk и ttk из модуля tkinter.
from tkinter import messagebox, filedialog # импортируем функции messagebox и filedialog из модуля tkinter.

app_name = "Яковишин Антон Максимович"
root = Tk()  # создаем главное окно приложения.
root.title(app_name)  # задаем заголовок окна. 

# Здесь размещаю вкладки
tab_control = ttk.Notebook(root) # создаем объект Notebook (вкладки) и привязываем его к главному окну.
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

tab_control.add(tab1, text="Калькулятор") # добавляем первую вкладку в объект Notebook с названием "Калькулятор".
tab_control.add(tab2, text="Чекбоксы")
tab_control.add(tab3, text="Работа с текстом")
tab_control.pack(expand=1, fill="both")

# Код для первой вкладки - калькулятор
def calculate():
    # Получаю введенные числа и выбранный оператор
    num1 = float(entry_num1.get()) #  получаем первое число из поля ввода и преобразуем его в тип float.
    num2 = float(entry_num2.get())
    operator = operator_cb.get() #  получаем выбранный оператор из выпадающего списка.
    
    # Выполняю операцию в зависимости от выбранного оператора
    if operator == "+":
        result = num1 + num2
    elif operator == "-":
        result = num1 - num2
    elif operator == "*":
        result = num1 * num2
    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            messagebox.showerror("Ошибка", "Деление на ноль недопустимо")
            return
    
    # Отображаю результат операции
    result_label.config(text=str(result)) #  отображаем результат операции в виджете Label.

# Создаю элементы на первой вкладке - калькуляторе
entry_num1 = ttk.Entry(tab1) #  создаем поле ввода для первого числа на первой вкладке.
entry_num1.pack() # размещаем поле ввода на первой вкладке.

entry_num2 = ttk.Entry(tab1)
entry_num2.pack()

operator_cb = ttk.Combobox(tab1, values=["+", "-", "*", "/"]) # создаем выпадающий список с операторами на первой вкладке.
operator_cb.pack() # размещаем выпадающий список на первой вкладке.

calculate_button = ttk.Button(tab1, text="Посчитать", command=calculate) # создаем кнопку для выполнения математических операций на первой вкладке.
calculate_button.pack()

result_label = ttk.Label(tab1, text="") # создаем виджет Label для отображения результата операции на первой вкладке.
result_label.pack()

# Код для второй вкладки - чекбоксы
def show_message(): # определяем функцию show_message для работы с чекбоксами.
    selected_options = []
    if checkbox1_var.get():
        selected_options.append("первый")
    if checkbox2_var.get():
        selected_options.append("второй")
    if checkbox3_var.get():
        selected_options.append("третий")

    if not selected_options: # если список выбранных опций пуст.
        messagebox.showinfo("Выбор", "Вы ничего не выбрали")
    else:
        message = "Вы выбрали: " + ", ".join(selected_options) # формируем сообщение о выбранных опциях.
        messagebox.showinfo("Выбор", message)

checkbox1_var = ttk.BooleanVar() # создаем переменную типа BooleanVar для первого чекбокса.
checkbox2_var = ttk.BooleanVar()
checkbox3_var = ttk.BooleanVar()

checkbox1 = ttk.Checkbutton(tab2, text="первый", variable=checkbox1_var) # создаем первый чекбокс на второй вкладке.
checkbox1.pack()

checkbox2 = ttk.Checkbutton(tab2, text="второй", variable=checkbox2_var)
checkbox2.pack()

checkbox3 = ttk.Checkbutton(tab2, text="третий", variable=checkbox3_var)
checkbox3.pack()

show_message_button = ttk.Button(tab2, text="Показать сообщение", command=show_message) # создаем кнопку для вывода сообщения о выбранных опциях на второй вкладке.
show_message_button.pack()

# Код для третьей вкладки - работа с текстом
def load_file():
    file_path = filedialog.askopenfilename(filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))) # открываем диалоговое окно для выбора файла и получаем путь к файлу.
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text.delete("1.0", "end") # очищаем виджет Text.
            text.insert("1.0", content) #  вставляем содержимое файла в виджет Text.

file_button = ttk.Button(tab3, text="Загрузить файл", command=load_file) # создаем кнопку для загрузки файла на третьей вкладке.
file_button.pack()

text = Text(tab3)
text.pack()

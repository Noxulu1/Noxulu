import tkinter as tk
import requests

def get_repo_info():
    repo_name = entry.get() # Получаем имя репозитория из поля ввода
    
    # Делаем запрос к API GitHub для получения информации о репозитории
    response = requests.get(f'https://api.github.com/blocklist-ipsets/{repo_name}')
    if response.status_code == 200: # Если запрос успешный
        repo_info = response.json()
        
        # Создаем новый файл и записываем нужную информацию в него
        with open('blocklist-ipsets', 'w') as file:
            file.write(f"'company': {repo_info['owner']['company']},n")
            file.write(f"'created_at': {repo_info['created_at']},n")
            file.write(f"'email': {repo_info['owner']['email']},n")
            file.write(f"'id': {repo_info['id']},n")
            file.write(f"'name': {repo_info['name']},n")
            file.write(f"'url': {repo_info['url']}n")
    else:
        print("Ошибка при выполнении запроса")

# Создаем графический интерфейс
window = tk.Tk()
window.title("Получение информации о репозитории")
window.geometry("300x200")

# Поле ввода для имени репозитория
entry = tk.Entry(window)
entry.pack(pady=10)

# Кнопка для выполнения запроса и получения информации
button = tk.Button(window, text="Получить информацию", command=get_repo_info)
button.pack(pady=10)

window.mainloop()

import tkinter as tk
import os
purchases = 0
root = tk.Tk()
root.title("Трекер расходов")
root.geometry("460x520")
try: root.iconbitmap("icon.ico")
except: pass
folder = os.path.dirname(__file__) #Находим папку, где лежит сам файл, чтобы картинка точно нашлась
img_path = os.path.join(folder, "wallet.png")
try:
    img = tk.PhotoImage(file=img_path)
    tk.Label(root, image=img).pack(pady=10)
except:
    tk.Label(root, text="[изображение]").pack(pady=10) #Заглушка, если файла wallet.png нет
tk.Label(root, text="Название покупки:").pack(anchor="w", padx=20) #Подпись поля
e1 = tk.Entry(root)
e1.pack(fill="x", padx=20)
tk.Label(root, text="Стоимость (руб.):").pack(anchor="w", padx=20) #Подпись поля
e2 = tk.Entry(root)
e2.pack(fill="x", padx=20, pady=(0, 12)) #Поле ввода стоимости
lbl = tk.Label(root, text="Покупок добавлено: 0", anchor="w", relief="solid", borderwidth=1, padx=6, pady=4) # сложный виджет: счётчик с рамкой
lbl.pack(fill="x", padx=20, pady=(0, 8))
def add(): #Обработчик кнопки «Добавить»
    global purchases
    purchases += 1 # увеличиваем счётчик
    lbl["text"] = f"Покупок добавлено: {purchases}\nПоследняя: {e1.get()} - {e2.get()} руб." #get() + обновление метки
b = tk.Button(root, text="Добавить покупку", bg="#1d5b76", fg="white", command=add) #Новая кнопка: command=add без скобок
b.pack(pady=10) #Размещаем кнопку на экране
root.mainloop()

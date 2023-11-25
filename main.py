import tkinter as tk
from tkinter import messagebox
lista_to_do = []


def main():
    def close_window():
        window.destroy()

    def add_button():
        content = txt.get()
        if content.isspace() :
            messagebox.showerror("Erro", "Você precisa escrever uma tarefa!")
        elif content:
            lista_to_do.append(content)
        txt.delete(0, tk.END)
        print(listtk)
        update()

    def update():
        listtk.delete(0, tk.END)
        for item in lista_to_do:
            listtk.insert(tk.END, item)

    
    window = tk.Tk()
    window.title("To do list")
    window.geometry("500x250")
    

    txt = tk.Entry(window, width=50)
    txt.grid(row=0, column=0, padx=10)

    btn_add = tk.Button(window, text="Add new", width=40, command=add_button)
    btn_add.grid(row=2, column=0, padx=10)
    btn_add.config(bg="#ccff33")

    #btn_update = tk.Button(window, text= "Update", command=update)
    #btn_update.pack()

    listtk = tk.Listbox(window, selectmode=tk.SINGLE, width=50)
    listtk.grid(row=4, column=0, padx=10)

    btn_remove = tk.Button(window, text="Remove", width=10)
    btn_remove.grid(row=6, column=1, padx=5)
    btn_remove.config(bg="red")

    btn_edit = tk.Button(window, text="Edit", width=10)
    btn_edit.grid(row=6, column=2, padx=5)

    btn_save = tk.Button(window, text="Save", width=10)
    btn_save.grid(row=6, column=0, padx=5)
     

    #btn_close = tk.Button(window, text="Close", command=close_window)
    #btn_close.pack(pady=50)

    window.mainloop()


if __name__ == "__main__":
    main()

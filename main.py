import tkinter as tk
from tkinter import messagebox
import os
import time
lista_to_do = []


def main():
    def close_window():
        window.destroy()

    #This method will add what is written on the textbox to the listbox.
    #If the user dont write and click the button, nothing will be added.
    #If the user write only spaces, a error message will apear.
    def add_button():
        content = txt.get()
        if content.isspace() :
            messagebox.showerror("Error", "You need to write a to do!")
        elif content:
            lista_to_do.append(content)
        txt.delete(0, tk.END)
        print(listtk)
        update()

    def update():
        listtk.delete(0, tk.END)
        for item in lista_to_do:
            listtk.insert(tk.END, item)

    def remove():
        selected_item = listtk.curselection()
        if selected_item:
            try:
                item = listtk.delete(selected_item)
                item = lista_to_do[int(selected_item[0])]
                lista_to_do.remove(item)

                print(f"Deletado o item {item}")
            except Exception as e:
                print(e)
        else:
            messagebox.showerror("Error","Select an item to remove!")


    def save():
        with open("text.txt", "w") as text:
            for t in lista_to_do:
                text.write(t + "\n")
            messagebox.showinfo("Info", "Saved successfully")
    
    def edit():
        ...

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

    btn_remove = tk.Button(window, text="Remove", width=10, command=remove)
    btn_remove.grid(row=6, column=1, padx=5)
    btn_remove.config(bg="red")

    btn_edit = tk.Button(window, text="Edit", width=10)
    btn_edit.grid(row=6, column=2, padx=5)

    btn_save = tk.Button(window, text="Save", width=10, command=save)
    btn_save.grid(row=6, column=0, padx=5)
     

    #btn_close = tk.Button(window, text="Close", command=close_window)
    #btn_close.pack(pady=50)

    window.mainloop()


if __name__ == "__main__":
    main()

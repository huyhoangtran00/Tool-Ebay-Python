import tkinter as tk
from tkinter import Listbox, Scrollbar, SINGLE, END
from tkinter import messagebox


class ListOfListsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Danh sách các danh sách")

        self.lists = []

        self.listbox = Listbox(root, selectmode=SINGLE)
        self.listbox.pack(side=tk.LEFT, padx=10, pady=10)

        self.scrollbar = Scrollbar(root, command=self.listbox.yview)
        self.scrollbar.pack(side=tk.LEFT, fill=tk.Y)
        self.listbox.config(yscrollcommand=self.scrollbar.set)

        self.show_button = tk.Button(
            root, text="Hiển thị danh sách", command=self.show_selected_list
        )
        self.show_button.pack(pady=10)

        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)

    def show_selected_list(self):
        selected_index = self.listbox.curselection()
        if selected_index:
            index = selected_index[0]
            selected_list = self.lists[index]
            print("Danh sách được chọn:", selected_list)

    def on_closing(self):
        if messagebox.askokcancel("Thoát", "Bạn có muốn thoát chương trình?"):
            self.root.destroy()

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = ListOfListsApp(root)
    app.run()

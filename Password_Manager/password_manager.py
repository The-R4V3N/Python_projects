from tkinter import CENTER, Tk, Label, Button, Entry, Frame, END, Toplevel
from tkinter import ttk
from db_operations import DbOperations


class main_window:

    # Creating Tkinter window
    def __init__(self, root, db):
        self.db = db
        self.root = root
        self.root.title("Password Manager")
        self.root.geometry("900x550+500+200")
        self.root.resizable(width=True, height=True)

        head_title = Label(self.root, text="Password Manager", width=40, fg="white", bg="blue", font=(
            "Ariel", 20), padx=10, pady=10).grid(columnspan=4, padx=140, pady=20)

        self.crud_frame = Frame(
            self.root, highlightbackground="black", highlightthickness=0.5, padx=2, pady=30)
        self.crud_frame.grid()
        self.create_entry_labels()
        self.create_entry_boxes()
        self.create_crud_buttons()
        self.search_entry = Entry(
            self.crud_frame, width=30, font=("Ariel", 12))

        self.search_entry.grid(row=self.row_num, column=self.col_num)
        self.col_num += 1
        Button(self.crud_frame, text="Search", bg="yellow", font=("Ariel", 12), width=20).grid(
            row=self.row_num, column=self.col_num, padx=5, pady=5)
        self.create_records_tree()

    # Creating labels for the window
    def create_entry_labels(self):
        self.col_num, self.row_num = 0, 0
        labels_info = ('Id', 'Website', 'Username', 'Password',)
        for label_info in labels_info:
            Label(self.crud_frame, text=label_info, bg='gray', fg='white',
                  font=("Ariel", 12), padx=5, pady=2).grid(row=self.row_num, column=self.col_num, padx=5, pady=2)
            self.col_num += 1

    # Creating CRUD Buttons
    def create_crud_buttons(self):
        self.row_num += 1
        self.col_num = 0
        button_info = (('Save', 'green', self.save_record), ('Update', 'blue', self.update_record),
                       ('Delete', 'red', self.delete_record), ('Copy Password', 'violet', self.copy_password), ('Show All Records', 'purple', self.show_record))
        for btn_info in button_info:
            if btn_info[0] == 'Show All Records':
                self.row_num += 1
                self.col_num = 0
            Button(self.crud_frame, text=btn_info[0], bg=btn_info[1], fg='white',
                   font=("Ariel", 12), padx=5, pady=2, width=20, command=btn_info[2]).grid(row=self.row_num, column=self.col_num, padx=5, pady=2)
            self.col_num += 1

    # Creating Entry Boxes
    def create_entry_boxes(self):
        self.row_num += 1
        self.entry_boxes = []
        self.col_num = 0
        entry_boxex = []
        for i in range(4):
            show = ""
            if i == 3:
                show = "*"
            entry_box = Entry(self.crud_frame, width=23,
                              background="lightgray", font=("Ariel", 12), show=show)

            entry_box.grid(row=self.row_num,
                           column=self.col_num, padx=5, pady=2)
            self.col_num += 1
            self.entry_boxes.append(entry_box)

    # Create CRUD Button Functions
    def save_record(self):
        website = self.entry_boxes[1].get()
        username = self.entry_boxes[2].get()
        password = self.entry_boxes[3].get()
        data = {'website': website, 'username': username, 'password': password}
        self.db.create_record(data)
        self.show_record()

    def update_record(self):
        ID = self.entry_boxes[0].get()
        website = self.entry_boxes[1].get()
        username = self.entry_boxes[2].get()
        password = self.entry_boxes[3].get()
        data = {'ID': ID,  'website': website,
                'username': username, 'password': password}
        self.db.update_record(data)
        self.show_record()

    def delete_record(self):
        ID = self.entry_boxes[0].get()
        self.db.delete_record(ID)
        self.show_record()

    def show_record(self):
        for item in self.records_tree.get_children():
            self.records_tree.delete(item)

        records_list = self.db.show_records()
        for record in records_list:
            self.records_tree.insert('', END, values=(record[0], record[3],
                                                      record[4], record[5]))

    def create_records_tree(self):
        columns = ("ID", "Website", "Username", "Password")
        self.records_tree = ttk.Treeview(self.root, columns=columns,
                                         show='headings')
        self.records_tree.heading('ID', text="ID")
        self.records_tree.heading('Website', text="Website Name")
        self.records_tree.heading('Username', text="Username")
        self.records_tree.heading('Password', text="Password")
        self.records_tree['displaycolumns'] = (
            "Website", "Username")

        def item_selected(events):
            for selected_item in self.records_tree.selection():
                item = self.records_tree.item(selected_item)
                record = item['values']
                for entry_box, item in zip(self.entry_boxes, record):
                    entry_box.delete(0, END)
                    entry_box.insert(0, item)

        self.records_tree.bind('<<TreeviewSelect>>', item_selected)

        self.records_tree.grid()

    # Copy to Clipboard
    def copy_password(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.entry_boxes[3].get())
        message = "Password Copied"
        title = "Copy"
        if self.entry_boxes[3].get() == "":
            message = "Box is Emptry"
            title = "Error"
        self.showmessage(title, message)

        def showmessage(self, title_box: str = None, message_box: str = None):
            TIME_TO_WAIT = 900  # in milliseconds
            root = Toplevel(self.root)
            background = 'green'
            if title_box == "Error":
                background = 'red'
            root.geometry('200x30+600+200')
            root.title(title_box)
            Label(root, text=message, background=background, font=('arial', 12),
                  fg='white').pack(padx=4, pady=2)
            try:
                root.after(TIME_TO_WAIT, root.destroy)
            except Exception as e:
                print(" An error has occured", e)


 # Main Function
if __name__ == "__main__":

    # Create Table if doesn't exist
    db_class = DbOperations()
    db_class.create_table()

    # Create Tkinter window
    root = Tk()
    root_class = main_window(root, db_class)
    root.mainloop()

import tkinter.ttk


class Table:
    # def test(self, event):
    #     row_index = self.table.focus()
    #     self.selected_row = self.table.item(row_index)['values']
    #     self.on_click(self.selected_row)

    def clear_table(self):
        for item in self.table.get_children():
            self.table.delete(item)

    def show_items(self, data_list):
        self.clear_table()
        for data in data_list:
            self.table.insert('', tkinter.END, values=data)

    def __init__(self, master, headers, columns_width, x, y, data_list, on_click):
        r = tuple(range(len(headers)))
        self.table = tkinter.ttk.Treeview(master, columns=r, show='headings')
        # self.onclick = on_click

        for i in r:
            self.table.heading(i, text=headers[i])
            self.table.column(i, width=columns_width[i])

        for data in data_list:
            self.table.insert('', tkinter.END, values=data)
        # self.table.bind("<ButtonRelease>", self.on_click)
        self.table.place(x=x, y=y)

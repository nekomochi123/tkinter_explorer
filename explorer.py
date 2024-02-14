# サンプルコード
import tkinter as tk
from tkinter import ttk
import os


def folder_insert(parent, path):
    # path配下のディレクトリ・ファイル取得
    for i in os.listdir(path):
        # 変数iのフルパス取得
        full_path = os.path.join(path, i).replace(os.sep, "/")
        # dir判別
        if os.path.isdir(full_path):
            # フォルダ名の取得
            dir_path = i
            tree.insert(
                parent, "end", text=dir_path, open="False", values=str(full_path)
            )


def select_record(event):
    # 選択行の判別
    record_id = tree.focus()
    # 選択行のレコードを取得
    record_values = tree.item(record_id, "values")
    if os.path.isdir(record_values[0]):
        folder_insert(record_id, record_values[0])


init_dir = r"/Users/penmaru".replace(
    os.sep, "/"
)
root = tk.Tk()
root.title("explorer")
root.geometry("600x700")
frame_treeview = ttk.Frame(root, height=300, width=300)
frame_treeview.pack()
tree = ttk.Treeview(frame_treeview, height=50)
bind_select_path = tree.bind("<<TreeviewSelect>>", select_record)

tree.heading("#0", text="explorer", anchor=tk.CENTER)
tree.column("#0", minwidth=0, width=500)
folder_insert("", init_dir)
scrollbar_x = ttk.Scrollbar(frame_treeview, orient=tk.HORIZONTAL, command=tree.xview)
scrollbar_y = ttk.Scrollbar(frame_treeview, orient=tk.VERTICAL, command=tree.yview)
tree.configure(xscroll=scrollbar_x.set)
tree.configure(yscroll=scrollbar_y.set)
tree.pack(side=tk.LEFT)
scrollbar_x.pack(side=tk.BOTTOM, fill=tk.X)
scrollbar_y.pack(side=tk.RIGHT, fill=tk.Y)


root.mainloop()
import tkinter as tk


def button_callback():
    print("Name:", name_entry.get())
    print("Age:", age_entry.get())
    print("Is student:", is_student_var.get())
    print("Education:", education_var.get())
    print("Occupation:", occupation_var.get())


root = tk.Tk()  # 创建主窗口

# 标签和文本框
name_label = tk.Label(root, text="Name:")
name_label.pack()

name_entry = tk.Entry(root)
name_entry.pack()

age_label = tk.Label(root, text="Age:")
age_label.pack()

age_entry = tk.Entry(root)
age_entry.pack()

# 复选框和单选按钮
is_student_var = tk.BooleanVar()
is_student_checkbutton = tk.Checkbutton(root, text="Student", variable=is_student_var)
is_student_checkbutton.pack()

occupation_var = tk.StringVar()
programmer_radiobutton = tk.Radiobutton(root, text="Programmer", variable=occupation_var, value="Programmer")
programmer_radiobutton.pack()

teacher_radiobutton = tk.Radiobutton(root, text="Teacher", variable=occupation_var, value="Teacher")
teacher_radiobutton.pack()

engineer_radiobutton = tk.Radiobutton(root, text="Engineer", variable=occupation_var, value="Engineer")
engineer_radiobutton.pack()

# 下拉菜单和列表框
education_label = tk.Label(root, text="Education:")
education_label.pack()

education_var = tk.StringVar()
education_choices = ["High school", "College", "Graduate school"]
education_dropdown = tk.OptionMenu(root, education_var, *education_choices)
education_dropdown.pack()

major_label = tk.Label(root, text="Major:")
major_label.pack()

major_listbox = tk.Listbox(root, selectmode="multiple")
major_listbox.pack()

for major in ["Computer science", "Mathematics", "Physics", "Chemistry", "Biology"]:
    major_listbox.insert(tk.END, major)

# 滑块和消息
rating_label = tk.Label(root, text="Rating:")
rating_label.pack()

rating_scale = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL)
rating_scale.pack()

message = tk.Message(root, text="Please rate this program:")
message.pack()

# 按钮和框架
button_frame = tk.Frame(root)
button_frame.pack()

submit_button = tk.Button(button_frame, text="Submit", command=button_callback)
submit_button.pack(side=tk.LEFT)

cancel_button = tk.Button(button_frame, text="Cancel")
cancel_button.pack(side=tk.LEFT)

# 进入主循环
root.mainloop()

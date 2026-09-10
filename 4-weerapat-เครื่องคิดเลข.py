from tkinter import *

root = Tk()
root.title("Calculator")
root.geometry("500x600")

# -----------------------------
# ส่วนที่ป้อนและแสดงใน display
# -----------------------------
content = ""                      # ประกาศตัวแปร เป็นข้อความว่างเปล่า
txt_input = StringVar(value="0")  # ประกาศตัวแปรข้อความมีค่า เป็น 0

# หน้าจอแสดงผล (ชิดขวา)
display = Entry(root, font=('arial', 30, 'bold'),
                fg="white", bg="darkslategray",
                textvariable=txt_input, justify='right')
display.grid(columnspan=4)

# -----------------------------
# ฟังก์ชันกดปุ่ม
# -----------------------------
def btn(number):
    global content
    content = content + str(number)
    txt_input.set(content)

# -----------------------------
# ฟังก์ชันปุ่มเท่ากับ
# -----------------------------
def equal():
    global content
    try:
        calculate = float(eval(content))
        txt_input.set(calculate)
        content = ""
    except Exception:
        txt_input.set("Error")
        content = ""

# -----------------------------
# ฟังก์ชันเคลียร์จอ
# -----------------------------
def clear():
    global content
    content = ""
    txt_input.set("")
    display.insert(0, "0")

# -----------------------------
# ปุ่มรับค่า (ใช้ lambda เรียก btn())
# -----------------------------
btn_color = "dodgerblue"   # น้ำเงินฟ้า
op_color = "crimson"       # แดงเข้ม

# แถว1
btt7 = Button(root, fg="white", bg=btn_color, font=('arial', 30, 'bold'), text="7",
              padx=30, pady=15, command=lambda: btn(7)).grid(row=1, column=0)
btt8 = Button(root, fg="white", bg=btn_color, font=('arial', 30, 'bold'), text="8",
              padx=30, pady=15, command=lambda: btn(8)).grid(row=1, column=1)
btt9 = Button(root, fg="white", bg=btn_color, font=('arial', 30, 'bold'), text="9",
              padx=30, pady=15, command=lambda: btn(9)).grid(row=1, column=2)
bttC = Button(root, fg="white", bg=op_color, font=('arial', 30, 'bold'), text="C",
              padx=28, pady=15, command=clear).grid(row=1, column=3)

# แถว2
btt4 = Button(root, fg="white", bg=btn_color, font=('arial', 30, 'bold'), text="4",
              padx=30, pady=15, command=lambda: btn(4)).grid(row=2, column=0)
btt5 = Button(root, fg="white", bg=btn_color, font=('arial', 30, 'bold'), text="5",
              padx=30, pady=15, command=lambda: btn(5)).grid(row=2, column=1)
btt6 = Button(root, fg="white", bg=btn_color, font=('arial', 30, 'bold'), text="6",
              padx=30, pady=15, command=lambda: btn(6)).grid(row=2, column=2)
bttplus = Button(root, fg="white", bg=op_color, font=('arial', 30, 'bold'), text="+",
                 padx=30, pady=15, command=lambda: btn("+")).grid(row=2, column=3)

# แถว3
btt1 = Button(root, fg="white", bg=btn_color, font=('arial', 30, 'bold'), text="1",
              padx=30, pady=15, command=lambda: btn(1)).grid(row=3, column=0)
btt2 = Button(root, fg="white", bg=btn_color, font=('arial', 30, 'bold'), text="2",
              padx=30, pady=15, command=lambda: btn(2)).grid(row=3, column=1)
btt3 = Button(root, fg="white", bg=btn_color, font=('arial', 30, 'bold'), text="3",
              padx=30, pady=15, command=lambda: btn(3)).grid(row=3, column=2)
bttminus = Button(root, fg="white", bg=op_color, font=('arial', 30, 'bold'), text="-",
                  padx=35, pady=15, command=lambda: btn("-")).grid(row=3, column=3)

# แถว4
btt0 = Button(root, fg="white", bg=btn_color, font=('arial', 30, 'bold'), text="0",
              padx=92, pady=15, command=lambda: btn(0)).grid(row=4, column=0, columnspan=2)
bttdot = Button(root, fg="white", bg=btn_color, font=('arial', 30, 'bold'), text=".",
                padx=35, pady=15, command=lambda: btn(".")).grid(row=4, column=2)
bttmulti = Button(root, fg="white", bg=op_color, font=('arial', 30, 'bold'), text="x",
                  padx=30, pady=15, command=lambda: btn("*")).grid(row=4, column=3)

# แถว5
bttequal = Button(root, fg="white", bg=op_color, font=('arial', 30, 'bold'), text="=",
                  padx=35, pady=15, command=equal).grid(row=5, column=0)
bttop = Button(root, fg="white", bg=op_color, font=('arial', 30, 'bold'), text="(",
               padx=35, pady=15, command=lambda: btn("(")).grid(row=5, column=1)
bttco = Button(root, fg="white", bg=op_color, font=('arial', 30, 'bold'), text=")",
               padx=35, pady=15, command=lambda: btn(")")).grid(row=5, column=2)
bttdivi = Button(root, fg="white", bg=op_color, font=('arial', 30, 'bold'), text="/",
                 padx=35, pady=15, command=lambda: btn("/")).grid(row=5, column=3)

root.mainloop()

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout,QGridLayout

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle("Calculator")


main_l = QVBoxLayout()
grid = QGridLayout()

pole = QLabel("0")

btn_list= list()
for i in range(10):
    btn = QPushButton(str(i))
    btn_list.append(btn)

btn_dor = QPushButton("=")
btn_plus = QPushButton("+")
btn_minus = QPushButton("-")
btn_dob = QPushButton("*")

btn_dil = QPushButton("/")
btn_Clear = QPushButton("CE")

for i in range(0,4):
    grid.addWidget(btn_list[i],0,i)
for i in range(4,8):
    grid.addWidget(btn_list[i],1,(i-4))

grid.addWidget(btn_list[8],2,0)
grid.addWidget(btn_list[9],2,1)
grid.addWidget(btn_dor,2,2)
grid.addWidget(btn_Clear,2,3)

grid.addWidget(btn_plus,3,0)
grid.addWidget(btn_minus,3,1)
grid.addWidget(btn_dob,3,2)
grid.addWidget(btn_dil,3,3)

main_l.addWidget(pole)
main_l.addLayout(grid)

main_win.setLayout(main_l)



# main_win.resize(600,900)
main_win.move(200,50)
main_win.show()
app.exec_()


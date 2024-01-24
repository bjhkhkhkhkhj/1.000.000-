from PyQt5.QtWidgets import*

app=QApplication([])
from main_window import*
main_win.rezize(600,500)
main_win.setWindowTitle("Memory Card")
main_win.move(300,300)

main_win.setLayuout(line)

btn_answer.clicker.connect(switch_screen)

main_win.show()
app.exec()
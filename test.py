from random import shuffle
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QGroupBox, QRadioButton, QButtonGroup
#iiii
class Question():
    #содержит вопрос, правильный ответ и три неправельных
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        #все строки надо задать при создании объекта, они запоминаются в свойство 
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2 
        self.wrong3 = wrong3

app = QApplication([])
btn_OK = QPushButton('Ответить') #* кнопка ответа
lb_Question = QLabel('Самый сложный вопрос в мире')#* текст-вопрос

RadioGroupBox = QGroupBox('Варианты ответов') #* группа на экранедля переключателя с ответами
rbtn_1 = QRadioButton('Вариант 1')
rbtn_2 = QRadioButton('Вариант 2')
rbtn_3 = QRadioButton('Вариант 3')
rbtn_4 = QRadioButton('Вариант 4')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)

layout_ans1 = QHBoxLayout()
layout_ans2 = QVBoxLayout() #* Вертикальные будут внутри горизотального
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1) #* два ответа в первый столбец
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)#* два ответа в второй столбец
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3) #* разместили столбцы в одной строке

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат текста')
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')

layout_res = QVBoxLayout()
layout_res.addWidget(lb_Result, alignment=(Qt.AlignLeft | Qt.AlignTop))
layout_res.addWidget(lb_Correct, alignment=Qt.AlignHCenter,stretch=2)
AnsGroupBox.setLayout(layout_res)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)
layout_line2.addWidget(AnsGroupBox)
AnsGroupBox.hide()

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK,stretch=2) #* кнопка должна быть большой
layout_line3.addStretch(1)

#*Теперь созданные строки разместим друг под другом :
layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5) #* пробелы между содержим

def show_result():
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')

def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)  
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)   

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

   
def ask(q:Question):
#функция записывает значение вопроса и ответов в соотвествующиее вид
#при этом варианты ответом рапределються рандомным образом
    shuffle(answers)
    answers[0].setText(q.right_answer) # первый элемент списка заполним правелным овтетом
    answers[1].setText(q.wrong1) 
    answers[2].setText(q.wrong2) 
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)# вопрос
    lb_Correct.setText(q.right_answer) # ответ
    show_question() # панель вопросов

def show_correct(res):
    lb_Result.setText(res)
    show_result()

def check_answer():
    #если выбран какой-отот вариант ответа, то надо проверить и показать панель ответов
    if answers[0].isChecked():
        show_correct('Правильно')
    else:
        if answers[1].isChecked() or answers[2].isChecked() or answers[3].isChecked():
            show_correct('Неверно!')

def next_question():
    #задет следующие вопросы списка
    # этой функции нужна переменная, в которой будет указывать номер текущего вопроса
    # эту переменую можно сделать глобальной, либо же сделать свойством 'глобального объекта
    # мы заведем (ниже) свойство window.cur_questionю
    window.cur_question = window.cur_question + 1 # переходим к следующему вопросу
    if window.cur_question >= len(questions_list):
        window.cur_question = 0 # если список вопросов заканчился - идем сначала
    q = questions_list[window.cur_question]# взяли вопрос
    ask(q) # спросили

window = QWidget()
window.setLayout(layout_card)
window.setWindowTitle('Memo Card')  

q = Question('Государственный язык Бразилии','Португальский','Бразильский','Испанский', 'Итальяснкий')
ask(q)
btn_OK.clicked.connect(check_answer)

window.resize(400,300)
window.show()
app.exec()

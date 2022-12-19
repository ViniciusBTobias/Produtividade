import pyautogui
import time

pyautogui.PAUSE = 0.5

#Abrir chrome
pyautogui.moveTo(659,736)
pyautogui.click()

#Korber
pyautogui.moveTo(153,0)
pyautogui.click()

#...
pyautogui.moveTo(31,179)
pyautogui.click()

#Supply
pyautogui.moveTo(154,256)
pyautogui.click()

#Advantage
pyautogui.moveTo(130,603)
pyautogui.click()

#Rastreabilidade
pyautogui.moveTo(140,669)
pyautogui.click()

#Faturamento antecipado
pyautogui.moveTo(195,377)
pyautogui.click()
pyautogui.write('342')
pyautogui.press('enter')

pyautogui.moveTo(363,496)
pyautogui.click()
pyautogui.press('left')
pyautogui.press('enter')
time.sleep(0.5)

pyautogui.moveTo(100,200)
pyautogui.click()
time.sleep(0.8)

pyautogui.moveTo(364,452)
pyautogui.click()
pyautogui.press('right')
pyautogui.press('right')
pyautogui.press('right')
pyautogui.press('right')
pyautogui.press('right')
pyautogui.press('enter')
time.sleep(0.5)

#Exportar
pyautogui.moveTo(980,134)
pyautogui.click()
time.sleep(0.7)

#Abrir arquivo
pyautogui.moveTo(105,651)
pyautogui.click()
time.sleep(1)

#Habilitar edição
pyautogui.moveTo(1188,76)
pyautogui.click()

#Pagina inicial
pyautogui.moveTo(116,51)
pyautogui.click()

#Apagar linhas
pyautogui.moveTo(728,215)
pyautogui.mouseDown()
pyautogui.moveTo(58,215)
pyautogui.mouseUp()
pyautogui.hotkey('ctrl','-')

pyautogui.moveTo(525,212)
pyautogui.mouseDown()
pyautogui.moveTo(1325,218)
pyautogui.mouseUp()
pyautogui.hotkey('ctrl','-')

pyautogui.moveTo(525,212)
pyautogui.mouseDown()
pyautogui.moveTo(1325,218)
pyautogui.mouseUp()
pyautogui.hotkey('ctrl','-')

#Inserir
pyautogui.moveTo(225,56)
pyautogui.click()
pyautogui.moveTo(143,353)
pyautogui.click()

#Tabela dinamica
pyautogui.moveTo(40,77)
pyautogui.click()
pyautogui.moveTo(142,546)
pyautogui.click()
pyautogui.press('enter')

#Arrastar tabela
pyautogui.moveTo(1040,341)
pyautogui.click()

pyautogui.moveTo(1045,364)
pyautogui.click()

pyautogui.moveTo(1075,637)
pyautogui.click()
pyautogui.moveTo(1119,563)
pyautogui.click()

#Selecionar 
pyautogui.moveTo(548,283)
pyautogui.click()
pyautogui.hotkey('ctrl','t')

#Pagina inicial
pyautogui.moveTo(116,51)
pyautogui.click()

#Classificar
pyautogui.moveTo(1106,93)
pyautogui.click()

#Z > A
pyautogui.moveTo(1144,183)
pyautogui.click()

#Abrir printer
pyautogui.moveTo(578,740)
pyautogui.click()

pyautogui.moveTo(87,87)
pyautogui.click()

#Cordenadas
pyautogui.moveTo(25,225)
pyautogui.mouseDown()

pyautogui.moveTo(893,677)
pyautogui.mouseUp()

#Copiar print
time.sleep(0.5)
pyautogui.hotkey('ctrl','c')
time.sleep(0.5)

#Fechar pagina do printer
pyautogui.moveTo(825,52)
pyautogui.click()
time.sleep(0.5)

#Abrir Google
pyautogui.moveTo(664,743)
pyautogui.click()
time.sleep(0.5)
pyautogui.moveTo(565,663)
pyautogui.click()

#Abrir Gmail
pyautogui.moveTo(21,14)
pyautogui.click() 
time.sleep(0.5)

#Escrever email
pyautogui.moveTo(63,158)
pyautogui.click()
time.sleep(0.5)

#Nome do email
pyautogui.write('E-mail')
pyautogui.press('enter')
time.sleep(1)

time.sleep(3)
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.press('enter')
pyautogui.press('enter')

#Enviar email + assunto  
time.sleep(0.5)               
pyautogui.press('tab')
pyautogui.write('Produtividade')
pyautogui.press('tab')
pyautogui.write('Produtividade Do Dia')
pyautogui.press('enter')

#Copiar print
pyautogui.hotkey('ctrl','v')
time.sleep(0.7)
                                                    
#Enviar o email
pyautogui.moveTo(836,691)
time.sleep(1)
pyautogui.click()










 
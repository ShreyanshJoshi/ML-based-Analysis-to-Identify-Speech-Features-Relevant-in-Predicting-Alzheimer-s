import pyautogui, time , pandas as pd
time.sleep(3)
x = pd.read_csv("./sentence.csv")

for i in range(240):
    fname = x['File'][i]
    uttsize = x['Num_Uttr'][i]
    pyautogui.typewrite("ipsyn {} + t*PAR - leng +c{} +f{}sentence".format(fname, uttsize, fname))
    pyautogui.press("enter")
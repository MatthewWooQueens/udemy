#with statement can replace try and catch statement for opening files

import random as r
import FreeSimpleGUI as sg

def main():
    '''lower = int(input("Enter the lower bound: "))
    upper = int(input("Enter the upper bound: "))
    num = r.randint(lower,upper)
    print(num)'''

    label = sg.Text("stuff", key='-OUT-')
    input_box = sg.InputText(default_text="Enter the lower bound: ", key='-LOWER-')
    input_box2 = sg.InputText(default_text="Enter the upper bound: ",key='-OUTER-')
    rand_button = sg.Button("Random", key='-RAND-')
    exit = sg.Button("Exit", key='-EXIT-')
    window = sg.Window('Random number generator', layout=[[label, rand_button],[input_box],[input_box2],[exit]])

    while True:
        event, values = window.read()
        print("stuff")
        if event == sg.WINDOW_CLOSED or event == 'Quit' or event=='-EXIT-':
            break
        
        if event == '-RAND-':
            try:
                num = r.randint(int(values['-LOWER-']),int(values['-OUTER-']))
                window['-OUT-'].update(f"{num}")
            except ValueError:
                '''window2 = sg.Window('Error', layout = [[sg.Text("Please type a number")]])
                window2.read()
                window2.close()'''
                sg.popup("Please provide 2 numbers")
    window.close()

if __name__ == '__main__':
    main()

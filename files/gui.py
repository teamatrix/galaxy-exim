import functions
import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg. InputText(tooltip="Enter todo")
add_button = sg.Button("Add")

window = sg.Window("My To-Do App", layout=[[label, input_box, add_button]])

""" Commented code below will display the input screen on a command line below the label"""

# window = sg.Window("My To-Do App", layout=[[label], [input_box]])


window.read()
window.close()

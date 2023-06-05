import PySimpleGUI as sgui
from autocat import auto_categorize

prova = auto_categorize()


sgui.Window(title="ciao", layout=[[]], margins = (100,50)).read()
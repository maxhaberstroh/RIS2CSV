import tkinter as tk
from tkinter import messagebox as mb
from tkinter.filedialog import askopenfilename, asksaveasfilename

from ris_conv import RISConv


class Program:

    def __init__(self) -> None:

        self.input_file_path = None
        self.output_file_path = None

        self.window = tk.Tk()
        self.window.title('RIS2CSV')
        self.window.geometry('450x80+600+400')
        self.window.resizable(False, False)

        icon_folder = tk.PhotoImage(file='resources/icon_folder.png')
        self.bt_open_file = tk.Button(self.window, borderwidth=0, image=icon_folder, cursor='hand2', command=self.open_file)
        self.bt_open_file.grid(row=0, column=1, padx=10)

        icon_save = tk.PhotoImage(file='resources/icon_save.png')
        self.bt_save = tk.Button(image=icon_save, borderwidth=0, state='disable', command=self.save_file)
        self.bt_save.grid(row=0, column=2, padx=10)

        self.lbinfo = tk.Label(text='Aguardando seleção do arquivo RIS')
        self.lbinfo.place(x=10, y=30)

        self.lbcopy = tk.Label(text='RIS2CSV © 2022 Wesley Dias')
        self.lbcopy.place(x=250, y=55)

        self.window.mainloop()

    def open_file(self) -> None:
        self.input_file_path = askopenfilename(filetypes=[('RIS File', '*.ris')])
        if self.input_file_path:
            self.lbinfo['text'] = self.input_file_path
            self.bt_save['state'] = 'normal'
            self.bt_save['cursor'] = 'hand2'
    
    def save_file(self) -> None:
        self.output_file_path  = asksaveasfilename(filetypes=[('CSV File', '*.csv')])
        if self.output_file_path :
            try:
                reader = RISConv(self.input_file_path)
                reader.ris_to_csv(self.output_file_path)
            except Exception as e:
                mb.showerror('Erro', 'Tivemos problemas ao tentar converter e salvar o arquivo!')
                print(e)
            else:
                mb.showinfo('Sucesso', 'Arquivo convertido para CSV e salvo com sucesso!')


if __name__ == '__main__':
    Program()

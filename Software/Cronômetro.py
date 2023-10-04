import customtkinter as ctk
from time import sleep

root = ctk.CTk()

class Application:

    # declarações e configurações iniciais para rodar o programa

    def __init__(self):
        self.root = root
        self.tela()
        self.frame()
        self.variables()
        self.run()
        root.mainloop()

    # configurações da tela

    def tela(self):
        self.root.title('Cronômetro')
        self.root.geometry('700x500')
        self.root.resizable(True, True)
        self.root.minsize(width=500, height=400)
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('green')

    def frame(self):
        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(pady=20, padx=60, fill='both', expand=True)

    def variables(self):
        self.milliseconds = 0
        self.time_seconds_count = 0
        self.time_15minutes_count = 0
        self.time_hour_count = 0

    def run(self):

        self.label = ctk.CTkLabel(self.frame, text=f'{self.time_hour_count} : {self.time_15minutes_count} : {self.time_seconds_count}', font=('Roboto', 40), text_color='#6be3a2')
        self.label.place(rely=0.5, relx=0.5)

        self.change_time()

    def change_time(self):
        while True:
            self.root.update()
            self.milliseconds += 1

            if self.root.quit() is True:
                break

            if self.milliseconds == 1000:
                self.time_seconds_count += 1
                self.milliseconds = 0
                self.label.configure(text=f'{self.time_hour_count} : {self.time_15minutes_count} : {self.time_seconds_count}')
                self.root.update()
            # if self.time_seconds_count == 900:
            #     self.time_15minutes_count += 15
            #     self.time_seconds_count = 0
            if self.time_seconds_count == 60:
                self.time_15minutes_count += 1
                self.time_seconds_count = 0
                self.label.configure(
                    text=f'{self.time_hour_count} : {self.time_15minutes_count} : {self.time_seconds_count}')
                self.root.update()
            if self.time_15minutes_count == 60:
                self.time_hour_count += 1
                self.time_15minutes_count = 0
                self.label.configure(
                    text=f'{self.time_hour_count} : {self.time_15minutes_count} : {self.time_seconds_count}')
                self.root.update()
            sleep(0.001)


Application()
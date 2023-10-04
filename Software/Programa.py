import customtkinter as ctk
from tkinter import PhotoImage
from tkinter.messagebox import askyesno
import imagesbank as imgbank
import tests_dicts_images_and_answers as tests
import tests_user_dicts as tests_dicts
from base64 import b64decode
from random import randint

# inicia a janela

root = ctk.CTk()

class Application:

    # declarações e configurações iniciais para rodar o programa

    def __init__(self):
        self.root = root
        self.tela()
        self.frames_da_tela()
        self.run()
        root.mainloop()

    # configurações da tela

    def tela(self):
        self.root.title('Tats!')
        self.root.geometry('700x500')
        self.root.resizable(True, True)
        self.root.minsize(width=500, height=400)
        ctk.set_appearance_mode('dark')
        ctk.set_default_color_theme('green')

        self.fullscreen_option = False
        self.path_option = False

    # declaração de frames

    def frames_da_tela(self):
        self.frame1 = ctk.CTkFrame(self.root)
        self.frame2 = ctk.CTkFrame(self.root)
        self.frame3 = ctk.CTkFrame(self.root)
        self.frame4 = ctk.CTkFrame(self.root)

        self.subframe1 = ctk.CTkFrame(self.root)
        self.subframe2 = ctk.CTkFrame(self.root)
        self.subframe3 = ctk.CTkFrame(self.root)
        self.subframe4 = ctk.CTkFrame(self.root)

        self.test_subframe1 = ctk.CTkFrame(self.frame2)
        self.test_subframe2 = ctk.CTkFrame(self.frame2)
        self.test_subframe3 = ctk.CTkFrame(self.frame2)
        self.test_subframe4 = ctk.CTkFrame(self.frame2)

        self.scrollableframe1 = ctk.CTkScrollableFrame(self.root, fg_color='#FFFFFF')

        self.logo_frame = ctk.CTkFrame(self.root, fg_color='#242424')

        self.frame_transparent = ctk.CTkFrame(self.root, fg_color='#242424')

    # função para destruir frames (alternar janelas)

    def frames_destroy(self):
        self.frame1.destroy()
        self.frame2.destroy()
        self.frame3.destroy()
        self.frame4.destroy()

        self.subframe1.destroy()
        self.subframe2.destroy()
        self.subframe3.destroy()
        self.subframe4.destroy()

        self.test_subframe1.destroy()
        self.test_subframe2.destroy()
        self.test_subframe3.destroy()
        self.test_subframe4.destroy()

        self.scrollableframe1.pack_forget()

        self.logo_frame.destroy()

        self.frame_transparent.destroy()

    # função para destruir e redeclarar frames (alternar janelas)

    def new_window(self):
        self.frames_destroy()
        self.frames_da_tela()
        self.buttons()

    # definição de variáveis para o programa

    def variables(self):
        self.test_option = 'None'

        self.test_n = 1

        self.user_answers_ita = tests_dicts.test_dict_ita()
        self.user_answers_enem = tests_dicts.test_dict_enem()
        self.user_answers_fuvest = tests_dicts.test_dict_fuvest()

        self.corrected_answers_ita = tests_dicts.test_dict_ita()
        self.corrected_answers_enem = tests_dicts.test_dict_enem()
        self.corrected_answers_fuvest = tests_dicts.test_dict_fuvest()

        self.correct_answers = 0
        self.wrong_answers = 0
        self.null_answers = 0

        self.points = 0

        self.challenge_correct_answer = False
        self.passed_questions = list()

        # ita

        self.physics_points = 0
        self.portuguese_points = 0
        self.english_points = 0
        self.math_points = 0
        self.chemical_points = 0

        # enem

        self.human_science_points = 0
        self.languages_and_codes_points = 0
        self.nature_science_points = 0
        self.math_points = 0

        # fuvest

        self.total_points = 0

        # for all

        self.total_points = 0

        self.amplier = 1
        self.decrease = 1

    # executa os widgets

    def heavy_variables(self):
        if self.test_option == 'ita':
            self.test_images_ita = tests.test_mode_ita(images=True)
            self.test_answers_ita = tests.test_mode_ita(answers=True)
            self.test_images_enem_english = 0
            self.test_images_enem_spanish = 0
            self.test_answers_enem = 0
            self.test_images_fuvest = 0
            self.test_answers_fuvest = 0

        elif self.test_option  == 'enem':
            self.test_images_enem_english = tests.test_mode_enem(images=True, english=True)
            self.test_images_enem_spanish = tests.test_mode_enem(images=True, spanish=True)
            self.test_images_ita = 0
            self.test_answers_ita = 0
            self.test_images_fuvest = 0
            self.test_answers_fuvest = 0

        elif self.test_option == 'fuvest':
            self.test_images_fuvest = tests.test_mode_fuvest(images=True)
            self.test_answers_fuvest = tests.test_mode_fuvest(answers=True)
            self.test_images_ita = 0
            self.test_answers_ita = 0
            self.test_images_enem_english = 0
            self.test_images_enem_spanish = 0
            self.test_answers_enem = 0

    def run(self):
        self.variables()
        self.images_declaration()
        self.buttons()
        self.widgets_frame_1()

        # image = PhotoImage(data=b64decode(imgbank.cc_license()))
        # label = ctk.CTkLabel(self.root, image=image, text='')
        # label.place(relx=0.92, rely=0.95, anchor='center')

    # widgets de cada frame

    def widgets_frame_1(self):
        self.root.minsize(width=500, height=400)
        self.root.geometry(f'{self.root.winfo_width()}x{self.root.winfo_height()}')

        self.new_window()

        self.frame1.pack(pady=20, padx=60, fill='both', expand=True)

        self.play_home_button.place(relx=0.5, rely=0.75, anchor='center')

        image = PhotoImage(data=b64decode(self.logo_tats))
        image = image.subsample(2, 2)
        label = ctk.CTkLabel(self.frame1, image=image, text='')
        label.place(relx=0.5, rely=0.25, anchor='center')

    def widgets_frame_2(self):
        self.test_n = 1
        self.logo_tats_button_mini.place_forget()

        self.root.minsize(width=900, height=700)
        self.root.geometry(f'{self.root.winfo_width()}x{self.root.winfo_height()}')

        self.new_window()

        self.logo_frame.pack(side='top', expand=False)

        self.logo_tats_button.place(rely=0.5, relx=0.5, anchor='center')

        self.subframe1.pack(pady=5, padx=30, fill='x', expand=True)

        label = ctk.CTkLabel(self.subframe1, text='Matérias', text_color='#6be3a2', font=('Roboto', 15))
        label.place(rely=0.1, relx=0.1)

        self.em1_button.place(rely=0.5, relx=0.2, anchor='center', relwidth=0.25, relheight=0.4)
        self.em2_button.place(rely=0.5, relx=0.5, anchor='center', relwidth=0.25, relheight=0.4)
        self.em3_button.place(rely=0.5, relx=0.8, anchor='center', relwidth=0.25, relheight=0.4)

        self.subframe2.pack(pady=15, padx=30, fill='x', expand=True)

        label2 = ctk.CTkLabel(self.subframe2, text='Vestibulares', text_color='#6be3a2', font=('Roboto', 15))
        label2.place(rely=0.1, relx=0.1)

        self.ita_button.place(rely=0.5, relx=0.2, anchor='center', relwidth=0.25, relheight=0.4)
        self.enem_button.place(rely=0.5, relx=0.5, anchor='center', relwidth=0.25, relheight=0.4)
        self.fuvest_button.place(rely=0.5, relx=0.8, anchor='center', relwidth=0.25, relheight=0.4)

    def widgets_frame_3(self):
        self.heavy_variables()

        self.root.minsize(width=900, height=700)
        self.root.geometry(f'{self.root.winfo_width()}x{self.root.winfo_height()}')

        self.new_window()

        self.logo_frame.pack(side='top', fill='x', expand=True)

        # self.logo_tats_button_mini.place(rely=0.2, relx=0.1, anchor='center')
        self.logo_tats_button_mini.place(y=50, x=100, anchor='center')

        if self.test_option == 'ita':
            image = PhotoImage(data=b64decode(self.logo_ita))
            image = image.subsample(2, 2)
            label = ctk.CTkLabel(self.logo_frame, image=image, text='')
            label.place(rely=0.5, relx=0.5, anchor='center')
        elif self.test_option == 'enem':
            image = PhotoImage(data=b64decode(self.logo_enem_resized))
            image = image.subsample(2, 2)
            label = ctk.CTkLabel(self.logo_frame, image=image, text='')
            label.place(rely=0.5, relx=0.5, anchor='center')
        elif self.test_option == 'fuvest':
            image = PhotoImage(data=b64decode(self.logo_fuvest))
            image = image.subsample(3, 3)
            label = ctk.CTkLabel(self.logo_frame, image=image, text='')
            label.place(rely=0.5, relx=0.5, anchor='center')
        else:
            pass

        self.subframe1.pack(pady=5, padx=30, fill='x', expand=True)

        label = ctk.CTkLabel(self.subframe1, text='Modo Prova', text_color='#6be3a2', font=('Roboto', 30))
        label.place(rely=0.1, relx=0.1)
        label2 = ctk.CTkLabel(self.subframe1, text='↳ Fazer a prova inteira normalmente, sem ou com tempo', text_color='#6be3a2', font=('Roboto', 15))
        label2.place(rely=0.3, relx=0.15)

        self.test_mode_withtime_play_button.place(rely=0.7, relx=0.85, anchor='center')
        self.test_mode_notime_play_button.place(rely=0.3, relx=0.85, anchor='center')

        self.subframe2.pack(pady=15, padx=30, fill='x', expand=True)

        label = ctk.CTkLabel(self.subframe2, text='Modo Desafio', text_color='#6be3a2', font=('Roboto', 30))
        label.place(rely=0.1, relx=0.1)
        label2 = ctk.CTkLabel(self.subframe2, text='↳ Quiz de questões aleatórias da prova',
                              text_color='#6be3a2', font=('Roboto', 15))
        label2.place(rely=0.3, relx=0.15)

        self.challenge_mode_play_button.place(rely=0.5, relx=0.85, anchor='center')

        self.previous_button.pack_forget()
        self.next_button.pack_forget()

    def widgets_frame_3_withtime_test(self):
        #configurar pra zerar a contabilização de respostas em outro lugar depois

        self.correct_answers = 0
        self.wrong_answers = 0
        self.null_answers = 0

        self.root.minsize(width=900, height=700)
        self.root.geometry(f'{self.root.winfo_width()}x{self.root.winfo_height()}')

        self.new_window()

        self.frame1.pack(pady=20, padx=60, fill='both', expand=True)

        # devido a um bug de correlação de frame do customtkinter, os botões go e exit estão definidos aqui e não na
        # função self.buttons()

        image_go_icon = PhotoImage(data=b64decode(self.go_icon))
        self.go_button = ctk.CTkButton(self.frame1, image=image_go_icon, text='', fg_color='#2b2b2b', hover_color='#242424',
                                       command=self.func_go_test_withtime, width=1)

        image_exit_icon = PhotoImage(data=b64decode(self.exit_icon))
        self.exit_button = ctk.CTkButton(self.frame1, image=image_exit_icon, text='', fg_color='#2b2b2b', hover_color='#242424',
                                         command=self.widgets_frame_3, width=1)

        self.go_button.place(rely=0.7, relx=0.3, anchor='center')
        self.exit_button.place(rely=0.7, relx=0.7, anchor='center')

        if self.test_option == 'ita':
            image = PhotoImage(data=b64decode(self.logo_ita))
            label = ctk.CTkLabel(self.frame1, image=image, text='')
            label.place(rely=0.3, relx=0.5, anchor='center')
        elif self.test_option == 'enem':
            image = PhotoImage(data=b64decode(self.logo_enem_resized))
            label = ctk.CTkLabel(self.frame1, image=image, text='')
            label.place(rely=0.3, relx=0.5, anchor='center')

            self.go_button.place(rely=0.75, relx=0.3, anchor='center')
            self.exit_button.place(rely=0.75, relx=0.7, anchor='center')
        elif self.test_option == 'fuvest':
            image = PhotoImage(data=b64decode(self.logo_fuvest))
            image = image.subsample(2, 2)
            label = ctk.CTkLabel(self.frame1, image=image, text='')
            label.place(rely=0.3, relx=0.5, anchor='center')
        else:
            pass

    # def func_go_test_withtime(self):

    def widgets_frame_3_enem_options(self):
        self.root.minsize(width=900, height=700)
        self.root.geometry(f'{self.root.winfo_width()}x{self.root.winfo_height()}')

        self.new_window()

        self.logo_frame.pack(side='top', fill='x', expand=True)

        self.logo_tats_button_mini.place(y=50, x=100, anchor='center')

        image = PhotoImage(data=b64decode(self.logo_enem_resized))
        image = image.subsample(2, 2)
        label = ctk.CTkLabel(self.logo_frame, image=image, text='')
        label.place(rely=0.5, relx=0.5, anchor='center')

        self.subframe1.pack(pady=5, padx=30, fill='x', expand=True)

        self.enem_english_option = ctk.CTkButton(self.subframe1, text='Inglês', font=('Roboto', 30), command=self.func_enem_english_option)
        self.enem_spanish_option = ctk.CTkButton(self.subframe1, text='Espanhol', font=('Roboto', 30), command=self.func_enem_spanish_option)

        self.enem_english_option.place(rely=0.5, relx=0.4, anchor='center')
        self.enem_spanish_option.place(rely=0.5, relx=0.6, anchor='center')

    def indisponible_function(self):
        self.logo_tats_button_mini.place_forget()

        self.new_window()

        self.frame1.pack(pady=20, padx=60, fill='both', expand=True)

        label = ctk.CTkLabel(self.frame1, text='Função não disponível ainda', text_color='#6be3a2', font=('Roboto', 30))
        label.place(rely=0.5, relx=0.5, anchor='center')

        image = PhotoImage(data=b64decode(self.exit_icon))
        exit_button = ctk.CTkButton(self.frame1, image=image, text='', fg_color='#2b2b2b',
                                         hover_color='#2b2b2b', command=self.widgets_frame_2)
        exit_button.place(rely=0.7, relx=0.5, anchor='center')

    def widgets_frame_4(self, firsttime=True):
        if firsttime is True:
            self.root.state(newstate='zoomed')
            self.logo_tats_button_mini.place_forget()

        self.new_window()

        self.previous_button.pack(side='left')
        self.next_button.pack(side='right')

        self.frame_transparent.pack(side='bottom', expand=False)

        self.logo_frame.pack(side='top', fill='x')

        if self.path_option is False:
            self.scrollableframe1.pack(side='left', pady=10, padx=10, ipady=200, ipadx=100, fill='x', expand=True)
            self.frame2.pack(side='right', pady=10, padx=10, fill='both', expand=True)
        else:
            self.scrollableframe1.pack(side='right', pady=10, padx=10, ipady=200, ipadx=100, fill='x', expand=True)
            self.frame2.pack(side='left', pady=10, padx=10, fill='both', expand=True)

        self.scrollableframe1.grid_rowconfigure(0, weight=1)
        self.scrollableframe1.grid_columnconfigure(0, weight=1)

        self.fullscreen_button.pack(side='right', pady=10)
        self.swap_button.pack(side='left', pady=10)
        self.end_test_button.pack(pady=10)

        self.test_subframe1.pack(pady=10, padx=10, fill='both', expand=True)
        self.test_subframe2.pack(pady=10, padx=10, fill='both', expand=True)

        self.exit_button.pack(ipady=15)

        self.widgets_frame_4_content()

    def widgets_frame_4_content(self):
        option_label = ctk.CTkLabel(self.test_subframe2, text='Marque sua opção:', font=('Roboto', 15), text_color='#6be3a2')
        option_label.place(rely=0.1, relx=0.1)
        self.a_button.place(rely=0.5, relx=0.3)
        self.b_button.place(rely=0.5, relx=0.4)
        self.c_button.place(rely=0.5, relx=0.5)
        self.d_button.place(rely=0.5, relx=0.6)
        self.e_button.place(rely=0.5, relx=0.7)

        if self.test_option == 'ita':
            image = PhotoImage(file=self.test_images_ita[self.test_n])
            label = ctk.CTkLabel(self.scrollableframe1, image=image, text='')
            label.grid(row=0, column=0, pady=25)

            # for question_n in range(1, len(self.test_images_ita) - 1):

            view_label = ctk.CTkLabel(self.test_subframe1, text='Escolhido:', font=('Roboto', 15), text_color='#6be3a2')
            view_label.place(rely=0.1, relx=0.1)
            view_label2 = ctk.CTkLabel(self.test_subframe1, text=f'{self.user_answers_ita[self.test_n].upper()}', font=('Roboto', 60), text_color='#6be3a2')
            view_label2.place(rely=0.5, relx=0.5, anchor='center')

        if self.test_option == 'enem':
            if self.enem_option == 'english':
                image = PhotoImage(file=self.test_images_enem_english[self.test_n])
                label = ctk.CTkLabel(self.scrollableframe1, image=image, text='')
                label.grid(row=0, column=0, pady=25)

                view_label = ctk.CTkLabel(self.test_subframe1, text='Escolhido:', font=('Roboto', 15),
                                          text_color='#6be3a2')
                view_label.place(rely=0.1, relx=0.1)
                view_label2 = ctk.CTkLabel(self.test_subframe1, text=f'{self.user_answers_enem[self.test_n].upper()}',
                                           font=('Roboto', 60), text_color='#6be3a2')
                view_label2.place(rely=0.5, relx=0.5, anchor='center')
            elif self.enem_option == 'spanish':
                image = PhotoImage(file=self.test_images_enem_spanish[self.test_n])
                label = ctk.CTkLabel(self.scrollableframe1, image=image, text='')
                label.grid(row=0, column=0, pady=25)

                view_label = ctk.CTkLabel(self.test_subframe1, text='Escolhido:', font=('Roboto', 15),
                                          text_color='#6be3a2')
                view_label.place(rely=0.1, relx=0.1)
                view_label2 = ctk.CTkLabel(self.test_subframe1, text=f'{self.user_answers_enem[self.test_n].upper()}',
                                           font=('Roboto', 60), text_color='#6be3a2')
                view_label2.place(rely=0.5, relx=0.5, anchor='center')
            else:
                pass
        if self.test_option == 'fuvest':
            image = PhotoImage(file=self.test_images_fuvest[self.test_n])
            label = ctk.CTkLabel(self.scrollableframe1, image=image, text='')
            label.grid(row=0, column=0, pady=25)

            view_label = ctk.CTkLabel(self.test_subframe1, text='Escolhido:', font=('Roboto', 15), text_color='#6be3a2')
            view_label.place(rely=0.1, relx=0.1)
            view_label2 = ctk.CTkLabel(self.test_subframe1, text=f'{self.user_answers_fuvest[self.test_n].upper()}',
                                       font=('Roboto', 60), text_color='#6be3a2')
            view_label2.place(rely=0.5, relx=0.5, anchor='center')

    def widgets_frame_4_results(self):
        self.root.minsize(width=900, height=700)
        self.root.geometry('900x700')

        self.previous_button.pack_forget()
        self.next_button.pack_forget()
        self.fullscreen_button.pack_forget()

        self.new_window()

        # gambiarra pro frame ficar no centro sem afetar o conteúdo grid, ajustando a posição de acordo com o tamanho da
        # janela

        # lembrando que preciso colocar um botão pra sair, um botão pra salvar os resultados e outro para ver quais
        # questões acertou, quais errou e quais deixou em nulo, comparando com um gabarito

        self.logo_frame.pack(side='top', fill='x', expand=True)
        self.frame1.pack()
        self.frame_transparent.pack(side='bottom', fill='x', expand=True)
        label_frame_empty1 = ctk.CTkLabel(self.logo_frame, text='')
        label_frame_empty1.pack()
        self.exit_results_button.pack()

        if self.test_option == 'ita':
            label1 = ctk.CTkLabel(self.frame1, text='Resultados', text_color='#FFFFFF', font=('Roboto', 50))
            label1.grid(row=0, column=0, columnspan=5)
            label2 = ctk.CTkLabel(self.frame1, text='━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━', text_color='#FFFFFF', font=('Roboto', 15))
            label2.grid(row=1, column=0, columnspan=5)
            label3 = ctk.CTkLabel(self.frame1, text='Matéria', text_color='#6495ED', font=('Roboto', 25))
            label3.grid(row=2, column=1, pady=10)
            label4 = ctk.CTkLabel(self.frame1, text='Matemática', text_color='#FFFFFF', font=('Roboto', 25))
            label4.grid(row=3, column=1, pady=10)
            label5 = ctk.CTkLabel(self.frame1, text='Física', text_color='#FFFFFF', font=('Roboto', 25))
            label5.grid(row=4, column=1, pady=10)
            label6 = ctk.CTkLabel(self.frame1, text='Química', text_color='#FFFFFF', font=('Roboto', 25))
            label6.grid(row=5, column=1, pady=10)
            label7 = ctk.CTkLabel(self.frame1, text='Inglês', text_color='#FFFFFF', font=('Roboto', 25))
            label7.grid(row=6, column=1, pady=10)
            label8 = ctk.CTkLabel(self.frame1, text='Português', text_color='#FFFFFF', font=('Roboto', 25))
            label8.grid(row=7, column=1, pady=10)
            label_empty1 = ctk.CTkLabel(self.frame1, text='')
            label_empty1.grid(row=8, column=1, pady=10)
            label_write_total = ctk.CTkLabel(self.frame1, text='Total', text_color='#FFFFFF', font=('Roboto', 25))
            label_write_total.grid(row=9, column=1, pady=10)

            label9 = ctk.CTkLabel(self.frame1, text='Acertos', text_color='#6495ED', font=('Roboto', 25))
            label9.grid(row=2, column=3, pady=10)
            label10 = ctk.CTkLabel(self.frame1, text=self.math_points, text_color='#FFFFFF', font=('Roboto', 25))
            label10.grid(row=3, column=3, pady=10)
            label11 = ctk.CTkLabel(self.frame1, text=self.physics_points, text_color='#FFFFFF', font=('Roboto', 25))
            label11.grid(row=4, column=3, pady=10)
            label12 = ctk.CTkLabel(self.frame1, text=self.chemical_points, text_color='#FFFFFF', font=('Roboto', 25))
            label12.grid(row=5, column=3, pady=10)
            label13 = ctk.CTkLabel(self.frame1, text=self.english_points, text_color='#FFFFFF', font=('Roboto', 25))
            label13.grid(row=6, column=3, pady=10)
            label14 = ctk.CTkLabel(self.frame1, text=self.portuguese_points, text_color='#FFFFFF', font=('Roboto', 25))
            label14.grid(row=7, column=3, pady=10)
            label_empty2 = ctk.CTkLabel(self.frame1, text='')
            label_empty2.grid(row=8, column=3, pady=10)
            label_view_total = ctk.CTkLabel(self.frame1, text=self.total_points, text_color='#FFFFFF', font=('Roboto', 25))
            label_view_total.grid(row=9, column=3, pady=10)

        elif self.test_option == 'enem':

            label1 = ctk.CTkLabel(self.frame1, text='Resultados', text_color='#FFFFFF', font=('Roboto', 50))
            label1.grid(row=0, column=0, columnspan=5)
            label2 = ctk.CTkLabel(self.frame1, text='━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━', text_color='#FFFFFF',
                                  font=('Roboto', 15))
            label2.grid(row=1, column=0, columnspan=5)
            label3 = ctk.CTkLabel(self.frame1, text='Matéria', text_color='#6495ED', font=('Roboto', 25))
            label3.grid(row=2, column=1, pady=10)
            label4 = ctk.CTkLabel(self.frame1, text='Linguagens, Códigos e suas Tecnologias', text_color='#FFFFFF', font=('Roboto', 25))
            label4.grid(row=3, column=1, pady=10)
            label5 = ctk.CTkLabel(self.frame1, text='Ciências Humanas e suas Tecnologias', text_color='#FFFFFF', font=('Roboto', 25))
            label5.grid(row=4, column=1, pady=10)
            label6 = ctk.CTkLabel(self.frame1, text='Matemática e suas Tecnologias', text_color='#FFFFFF', font=('Roboto', 25))
            label6.grid(row=5, column=1, pady=10)
            label7 = ctk.CTkLabel(self.frame1, text='Ciências da Natureza e suas Tecnologias', text_color='#FFFFFF', font=('Roboto', 25))
            label7.grid(row=6, column=1, pady=1)
            label_empty1 = ctk.CTkLabel(self.frame1, text='')
            label_empty1.grid(row=7, column=1, pady=10)
            label_write_total = ctk.CTkLabel(self.frame1, text='Total', text_color='#FFFFFF', font=('Roboto', 25))
            label_write_total.grid(row=8, column=1, pady=10, padx=10)

            label9 = ctk.CTkLabel(self.frame1, text='Acertos', text_color='#6495ED', font=('Roboto', 25))
            label9.grid(row=2, column=3, pady=10)
            label10 = ctk.CTkLabel(self.frame1, text=self.languages_and_codes_points, text_color='#FFFFFF', font=('Roboto', 25))
            label10.grid(row=3, column=3, pady=10)
            label11 = ctk.CTkLabel(self.frame1, text=self.human_science_points, text_color='#FFFFFF', font=('Roboto', 25))
            label11.grid(row=4, column=3, pady=10)
            label12 = ctk.CTkLabel(self.frame1, text=self.math_points, text_color='#FFFFFF', font=('Roboto', 25))
            label12.grid(row=5, column=3, pady=10)
            label13 = ctk.CTkLabel(self.frame1, text=self.nature_science_points, text_color='#FFFFFF', font=('Roboto', 25))
            label13.grid(row=6, column=3, pady=10)
            label_empty2 = ctk.CTkLabel(self.frame1, text='')
            label_empty2.grid(row=7, column=3, pady=10)
            label_view_total = ctk.CTkLabel(self.frame1, text=self.total_points, text_color='#FFFFFF',
                                            font=('Roboto', 25))
            label_view_total.grid(row=8, column=3, pady=10)

        elif self.test_option == 'fuvest':
            label1 = ctk.CTkLabel(self.frame1, text='Resultados', text_color='#FFFFFF', font=('Roboto', 50))
            label1.grid(row=0, column=0, columnspan=5)
            label2 = ctk.CTkLabel(self.frame1, text='━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━', text_color='#FFFFFF',
                                  font=('Roboto', 15))
            label2.grid(row=1, column=0, columnspan=5)
            label3 = ctk.CTkLabel(self.frame1, text='Matéria', text_color='#6495ED', font=('Roboto', 25))
            label3.grid(row=2, column=1, pady=10)
            label4 = ctk.CTkLabel(self.frame1, text='Geral', text_color='#FFFFFF', font=('Roboto', 25))
            label4.grid(row=3, column=1, pady=10)

            label9 = ctk.CTkLabel(self.frame1, text='Acertos', text_color='#6495ED', font=('Roboto', 25))
            label9.grid(row=2, column=3, pady=10)
            label10 = ctk.CTkLabel(self.frame1, text=self.total_points, text_color='#FFFFFF', font=('Roboto', 25))
            label10.grid(row=3, column=3, pady=10)

        else:
            pass

    def widgets_frame_5_challenge_mode(self, firsttime=False):
        if firsttime is True:
            self.total_points = 0
            self.root.state(newstate='zoomed')
            if self.test_option == 'ita':
                self.test_n = randint(1, 60)
            elif self.test_option == 'enem':
                self.test_n = randint(1, 180)
            elif self.test_option == 'fuvest':
                self.test_n = randint(1, 90)
            else:
                pass
            self.logo_tats_button_mini.place_forget()

        # cuidado, preciso colocar uma função pra evitar as questões anuladas

        while True:
            if self.test_n in self.passed_questions:
                if self.test_option == 'ita':
                    self.test_n = randint(1, 60)
                elif self.test_option == 'enem':
                    self.test_n = randint(1, 180)
                elif self.test_option == 'fuvest':
                    self.test_n = randint(1, 90)
            else:
                pass

            if self.test_n not in self.passed_questions:
                break
            else:
                pass

        self.new_window()

        self.frame_transparent.pack(side='bottom', expand=False)

        self.logo_frame.pack(side='top', fill='x')

        label = ctk.CTkLabel(self.logo_frame, text='1 Acerto = 1 Ponto. 5 pontos, você ganha!', text_color='#6495ED', font=('Roboto', 20))
        label.place(rely=0.5, relx=0.5, anchor='center')

        if self.path_option is False:
            self.scrollableframe1.pack(side='left', pady=10, padx=10, ipady=200, ipadx=100, fill='x', expand=True)
            self.frame2.pack(side='right', pady=10, padx=10, fill='both', expand=True)
        else:
            self.scrollableframe1.pack(side='right', pady=10, padx=10, ipady=200, ipadx=100, fill='x', expand=True)
            self.frame2.pack(side='left', pady=10, padx=10, fill='both', expand=True)

        self.scrollableframe1.grid_rowconfigure(0, weight=1)
        self.scrollableframe1.grid_columnconfigure(0, weight=1)

        self.challenge_mode_fullscreen_button.pack(side='right', pady=10)
        self.challenge_mode_swap_button.pack(side='left', pady=10)
        self.challenge_mode_end_test_button.pack(pady=10)

        self.test_subframe1.pack(pady=10, padx=10, fill='both', expand=True)
        self.test_subframe2.pack(pady=10, padx=10, fill='both', expand=True)

        self.exit_button.pack(side='left', ipady=15)

        self.widgets_frame_5_challenge_mode_content()

    def widgets_frame_5_challenge_mode_content(self):

        # caso não estejam todas as imagens codificadas e colocadas no dicionário, vai dar erro mesmo.

        option_label = ctk.CTkLabel(self.test_subframe2, text='Marque sua opção:', font=('Roboto', 15),
                                    text_color='#6495ED')
        option_label.place(rely=0.1, relx=0.1)
        self.a_button_challenge_mode.place(rely=0.5, relx=0.3)
        self.b_button_challenge_mode.place(rely=0.5, relx=0.4)
        self.c_button_challenge_mode.place(rely=0.5, relx=0.5)
        self.d_button_challenge_mode.place(rely=0.5, relx=0.6)
        self.e_button_challenge_mode.place(rely=0.5, relx=0.7)

        if self.test_option == 'ita':
            image = PhotoImage(file=self.test_images_ita[self.test_n])
            label = ctk.CTkLabel(self.scrollableframe1, image=image, text='')
            label.grid(row=0, column=0, pady=25)

            view_label = ctk.CTkLabel(self.test_subframe1, text='Escolhido:', font=('Roboto', 15), text_color='#6495ED')
            view_label.place(rely=0.1, relx=0.1)
            view_label2 = ctk.CTkLabel(self.test_subframe1, text=f'{self.user_answers_ita[self.test_n].upper()}',
                                       font=('Roboto', 60), text_color='#6495ED')
            view_label2.place(rely=0.5, relx=0.5, anchor='center')

        if self.test_option == 'enem':
            if self.enem_option == 'english':
                image = PhotoImage(file=self.test_images_enem_english[self.test_n])
                label = ctk.CTkLabel(self.scrollableframe1, image=image, text='')
                label.grid(row=0, column=0, pady=25)

                view_label = ctk.CTkLabel(self.test_subframe1, text='Escolhido:', font=('Roboto', 15), text_color='#6495ED')
                view_label.place(rely=0.1, relx=0.1)
                view_label2 = ctk.CTkLabel(self.test_subframe1, text=f'{self.user_answers_enem[self.test_n].upper()}',
                                           font=('Roboto', 60), text_color='#6495ED')
                view_label2.place(rely=0.5, relx=0.5, anchor='center')
            elif self.enem_option == 'spanish':
                image = PhotoImage(file=self.test_images_enem_spanish[self.test_n])
                label = ctk.CTkLabel(self.scrollableframe1, image=image, text='')
                label.grid(row=0, column=0, pady=25)

                view_label = ctk.CTkLabel(self.test_subframe1, text='Escolhido:', font=('Roboto', 15),
                                          text_color='#6495ED')
                view_label.place(rely=0.1, relx=0.1)
                view_label2 = ctk.CTkLabel(self.test_subframe1, text=f'{self.user_answers_enem[self.test_n].upper()}',
                                           font=('Roboto', 60), text_color='#6495ED')
                view_label2.place(rely=0.5, relx=0.5, anchor='center')
            else:
                pass

        if self.test_option == 'fuvest':
            image = PhotoImage(file=self.test_images_fuvest[self.test_n])
            label = ctk.CTkLabel(self.scrollableframe1, image=image, text='')
            label.grid(row=0, column=0, pady=25)

            view_label = ctk.CTkLabel(self.test_subframe1, text='Escolhido:', font=('Roboto', 15), text_color='#6495ED')
            view_label.place(rely=0.1, relx=0.1)
            view_label2 = ctk.CTkLabel(self.test_subframe1, text=f'{self.user_answers_fuvest[self.test_n].upper()}',
                                       font=('Roboto', 60), text_color='#6495ED')
            view_label2.place(rely=0.5, relx=0.5, anchor='center')

    def widgets_frame_5_challenge_mode_results(self):
        self.new_window()

        self.frame1.pack(pady=20, padx=60, fill='both', expand=True)

        if self.total_points != 5:
            if self.challenge_correct_answer is False:
                label1 = ctk.CTkLabel(self.frame1, text='Errou!', font=('Roboto', 40), text_color='#941c5d')
                label1.place(rely=0.3, relx=0.5, anchor='center')
                if self.test_option == 'ita':
                    teste = self.test_answers_ita
                elif self.test_option == 'enem':
                    teste = self.test_answers_enem
                elif self.test_option == 'fuvest':
                    teste = self.test_answers_fuvest
                else:
                    pass
                label2 = ctk.CTkLabel(self.frame1, text=f'Resposta correta: {teste[self.test_n].upper()}', font=('Roboto', 20), text_color='#FFFFFF')
                label2.place(rely=0.5, relx=0.5, anchor='center')
                label3 = ctk.CTkLabel(self.frame1, text=f'Total de pontos: {self.total_points}', font=('Roboto', 20), text_color='#FFFFFF')
                label3.place(rely=0.6, relx=0.5, anchor='center')

                self.challenge_mode_avance_button.place(rely=0.8, relx=0.5, anchor='center')

                self.passed_questions.append(self.test_n)
            else:
                label1 = ctk.CTkLabel(self.frame1, text='Acertou!', font=('Roboto', 40), text_color='#6be3a2')
                label1.place(rely=0.4, relx=0.5, anchor='center')
                label2 = ctk.CTkLabel(self.frame1, text=f'Total de pontos: {self.total_points}', font=('Roboto', 20), text_color='#FFFFFF')
                label2.place(rely=0.6, relx=0.5, anchor='center')

                self.challenge_mode_avance_button.place(rely=0.8, relx=0.5, anchor='center')

                self.passed_questions.append(self.test_n)
        else:
            label1 = ctk.CTkLabel(self.frame1, text='Olha só, e não é que conseguiu mesmo?', font=('Roboto', 30), text_color='#FFFFFF')
            label1.place(rely=0.3, relx=0.5, anchor='center')

            label1 = ctk.CTkLabel(self.frame1, text='Parabéns, você venceu!', font=('Roboto', 30),
                                  text_color='#6be3a2')
            label1.place(rely=0.5, relx=0.5, anchor='center')

            self.challenge_mode_exit_button.place(rely=0.7, relx=0.5, anchor='center')

            self.total_points = 0
            self.passed_questions = list()
            self.test_n = 1

    ###############################################################################################################
    # em matérias, fazer um loop for que vá adicionando botões conforme ele vai achando mais imagens de matérias no
    # dicionário. O dicionário deverá conter o nome da matéria, depois outro dicionário dentro deste com as imagens
    # da matéria em ordem.

    # desse modo, posso adicionar quantas imagens e matérias eu quiser, que o loop for vai ajustando os botões e
    # colocando botões de próximo e anterior embaixo, para a pessoa avançar ou retroceder para ver mais conteúdos.

    # ou posso tentar fazer um frame rolável que tenha todos os botões.
    ###############################################################################################################

    def widgets_frame_6_matters(self):
        self.root.minsize(900, 700)
        self.new_window()

        self.scrollableframe1.pack(pady=20, padx=60, fill='both', expand=True)

        self.scrollableframe1.grid_columnconfigure(0, weight=1)
        self.scrollableframe1.grid_columnconfigure(1, weight=1)
        self.scrollableframe1.grid_columnconfigure(2, weight=1)
        self.scrollableframe1.grid_columnconfigure(3, weight=1)

        button1 = ctk.CTkButton(self.scrollableframe1, text='Matemática', font=('Roboto', 30))
        button1.grid(row=0, column=0, padx=20, pady=20)
        button2 = ctk.CTkButton(self.scrollableframe1, text='Física', font=('Roboto', 30))
        button2.grid(row=0, column=1, padx=20, pady=20)
        button1 = ctk.CTkButton(self.scrollableframe1, text='Química', font=('Roboto', 30))
        button1.grid(row=0, column=2, padx=20, pady=20)
        button1 = ctk.CTkButton(self.scrollableframe1, text='Biologia', font=('Roboto', 30))
        button1.grid(row=0, column=3, padx=20, pady=20)
        button1 = ctk.CTkButton(self.scrollableframe1, text='Português', font=('Roboto', 30))
        button1.grid(row=1, column=0, padx=20, pady=20)
        button2 = ctk.CTkButton(self.scrollableframe1, text='Inglês', font=('Roboto', 30))
        button2.grid(row=1, column=1, padx=20, pady=20)
        button1 = ctk.CTkButton(self.scrollableframe1, text='Redação', font=('Roboto', 30))
        button1.grid(row=1, column=2, padx=20, pady=20)
        button1 = ctk.CTkButton(self.scrollableframe1, text='Literatura', font=('Roboto', 30))
        button1.grid(row=1, column=3, padx=20, pady=20)
        button1 = ctk.CTkButton(self.scrollableframe1, text='História', font=('Roboto', 30))
        button1.grid(row=2, column=0, padx=20, pady=20)
        button2 = ctk.CTkButton(self.scrollableframe1, text='Geografia', font=('Roboto', 30))
        button2.grid(row=2, column=1, padx=20, pady=20)
        button1 = ctk.CTkButton(self.scrollableframe1, text='Filosofia', font=('Roboto', 30))
        button1.grid(row=2, column=2, padx=20, pady=20)
        button1 = ctk.CTkButton(self.scrollableframe1, text='Sociologia', font=('Roboto', 30))
        button1.grid(row=2, column=3, padx=20, pady=20)
        button2 = ctk.CTkButton(self.scrollableframe1, text='Artes', font=('Roboto', 30))
        button2.grid(row=3, column=0, columnspan=4, padx=20, pady=20)

        # self.widgets_frame_6_matters_material()

    def widgets_frame_6_matters_material(self):
        self.root.minsize(900, 700)
        self.new_window()

        self.scrollableframe1.pack(pady=20, padx=60, fill='both', expand=True)

        self.scrollableframe1.grid_rowconfigure(0, weight=1)
        self.scrollableframe1.grid_rowconfigure(1, weight=1)
        self.scrollableframe1.grid_rowconfigure(2, weight=1)
        self.scrollableframe1.grid_columnconfigure(0, weight=1)
        self.scrollableframe1.grid_columnconfigure(1, weight=1)
        self.scrollableframe1.grid_columnconfigure(2, weight=1)

        n = 0

        for row_count in range(0, 2):
            for column_count in range(0, 3):
                n += 1
                button = ctk.CTkButton(self.scrollableframe1, text=f'Matéria {n}', font=('Roboto', 30))
                button.grid(row=row_count, column=column_count, padx=20, pady=20)

    # def widgets_frame_7(self):

    # definindo opções para os próximos frames

    def ita_option(self):
        self.test_option = 'ita'
        self.widgets_frame_3()

    def enem_test_option(self):
        self.test_option = 'enem'
        self.widgets_frame_3()

    def fuvest_option(self):
        self.test_option = 'fuvest'
        self.widgets_frame_3()

    # botões pré-configurados

    def buttons(self):
        image1 = PhotoImage(data=b64decode(self.play_home_icon))
        self.play_home_button = ctk.CTkButton(self.frame1, image=image1, text='', fg_color='#2b2b2b', hover_color='#2b2b2b',
                                              command=self.widgets_frame_2)
                                              # command= self.widgets_frame_6_matters))

        image = PhotoImage(data=b64decode(self.play_icon))
        self.play_button = ctk.CTkButton(self.frame1, image=image, text='', fg_color='#2b2b2b', hover_color='#2b2b2b', command=self.widgets_frame_2)

        self.em1_button = ctk.CTkButton(self.subframe1, text='1° Ensino Médio', font=('Roboto', 15), command=self.indisponible_function)
        self.em2_button = ctk.CTkButton(self.subframe1, text='2° Ensino Médio', font=('Roboto', 15), command=self.indisponible_function)
        self.em3_button = ctk.CTkButton(self.subframe1, text='3° Ensino Médio', font=('Roboto', 15), command=self.indisponible_function)

        image1 = PhotoImage(data=b64decode(self.logo_ita)).subsample(4, 4)
        self.ita_button = ctk.CTkButton(self.subframe2, image=image1, text='', command=self.ita_option)
        image2 = PhotoImage(data=b64decode(self.logo_enem)).subsample(3, 3)
        self.enem_button = ctk.CTkButton(self.subframe2, image=image2, text='', command=self.widgets_frame_3_enem_options)
        image3 = PhotoImage(data=b64decode(self.logo_fuvest)).subsample(5, 5)
        self.fuvest_button = ctk.CTkButton(self.subframe2, image=image3, text='', command=self.fuvest_option)

        image4 = PhotoImage(data=b64decode(self.logo_tats)).subsample(3, 3)
        self.logo_tats_button = ctk.CTkButton(self.logo_frame, image=image4, text='', fg_color='#242424', hover_color='#242424', command=self.widgets_frame_1)

        image5 = PhotoImage(data=b64decode(self.logo_tats)).subsample(5, 5)
        self.logo_tats_button_mini = ctk.CTkButton(self.root, image=image5, text='', fg_color='#242424', hover_color='#242424', command=self.widgets_frame_2)

        image7 = PhotoImage(data=b64decode(self.play_icon_notime))
        self.test_mode_notime_play_button = ctk.CTkButton(self.subframe1, image=image7, text='', fg_color='#2b2b2b', hover_color='#2b2b2b', command=self.widgets_frame_4, text_color='#6be3a2')
        image8 = PhotoImage(data=b64decode(self.play_icon_withtime))
        self.test_mode_withtime_play_button = ctk.CTkButton(self.subframe1, image=image8, text='', fg_color='#2b2b2b', hover_color='#2b2b2b',
                                                            command=self.indisponible_function,
                                                            # command=self.widgets_frame_3_withtime_test,
                                                            text_color='#6be3a2')

        self.challenge_mode_play_button = ctk.CTkButton(self.subframe2, image=image, text='', fg_color='#2b2b2b', hover_color='#2b2b2b', command=self.play_challenge_mode_func)

        image9 = PhotoImage(data=b64decode(self.logo_tats_mini)).subsample(5, 5)
        self.exit_button = ctk.CTkButton(self.logo_frame, image=image9, text='', fg_color='#242424', hover_color='#242424', command=self.exit_func)

        image10 = PhotoImage(data=b64decode(self.previous_icon))
        self.previous_button = ctk.CTkButton(self.root, image=image10, text='', fg_color='#242424', hover_color='#242424', width=1, command=self.func_previous)

        image11 = PhotoImage(data=b64decode(self.next_icon))
        self.next_button = ctk.CTkButton(self.root, image=image11, text='', fg_color='#242424', hover_color='#242424', width=1, command=self.func_next)

        image12 = PhotoImage(data=b64decode(self.fullscreen_icon))
        self.fullscreen_button = ctk.CTkButton(self.frame_transparent, image=image12, text='', fg_color='#242424', hover_color='#242424', width=1, command=self.fullscreen_func)

        image13 = PhotoImage(data=b64decode(self.swap_icon))
        self.swap_button = ctk.CTkButton(self.frame_transparent, image=image13, text='', fg_color='#242424', hover_color='#242424', width=1, command=self.path_func)

        image14 = PhotoImage(data=b64decode(self.end_test_icon))
        self.end_test_button = ctk.CTkButton(self.frame_transparent, image=image14, text='', fg_color='#242424', hover_color='#242424', width=1, command=self.verify_answers)
                                             # command=print('Preciso dar a opção nos resultados de ver o gabarito'))

        self.a_button = ctk.CTkButton(self.test_subframe2, text='A)', command=self.a_button_set_user_answer, width=50, height=50, font=('Roboto', 25))
        self.b_button = ctk.CTkButton(self.test_subframe2, text='B)', command=self.b_button_set_user_answer, width=50, height=50, font=('Roboto', 25))
        self.c_button = ctk.CTkButton(self.test_subframe2, text='C)', command=self.c_button_set_user_answer, width=50, height=50, font=('Roboto', 25))
        self.d_button = ctk.CTkButton(self.test_subframe2, text='D)', command=self.d_button_set_user_answer, width=50, height=50, font=('Roboto', 25))
        self.e_button = ctk.CTkButton(self.test_subframe2, text='E)', command=self.e_button_set_user_answer, width=50, height=50, font=('Roboto', 25))

        image15 = PhotoImage(data=b64decode(self.exit_icon))
        self.exit_results_button = ctk.CTkButton(self.frame_transparent, image=image15, text='', fg_color='#242424', hover_color='#242424', width=1, command=self.exit_results)

        image16 = PhotoImage(data=b64decode(self.challenge_mode_fullscreen_icon))
        self.challenge_mode_fullscreen_button = ctk.CTkButton(self.frame_transparent, image=image16, text='',
                                                              fg_color='#242424',
                                                              hover_color='#242424', width=1,
                                                              command=self.fullscreen_func)

        image17 = PhotoImage(data=b64decode(self.challenge_mode_swap_icon))
        self.challenge_mode_swap_button = ctk.CTkButton(self.frame_transparent, image=image17, text='',
                                                        fg_color='#242424',
                                                        hover_color='#242424', width=1,
                                                        command=self.path_challenge_mode_func)

        image18 = PhotoImage(data=b64decode(self.challenge_mode_end_test))
        self.challenge_mode_end_test_button = ctk.CTkButton(self.frame_transparent, image=image18, text='',
                                                            fg_color='#242424',
                                                            hover_color='#242424', width=1,
                                                            command=self.verify_answers_challenge_mode)

        self.a_button_challenge_mode = ctk.CTkButton(self.test_subframe2, text='A)', command=self.a_button_set_user_answer_challenge_mode, width=50,
                                      height=50, font=('Roboto', 25), fg_color='#6495ED')
        self.b_button_challenge_mode = ctk.CTkButton(self.test_subframe2, text='B)', command=self.b_button_set_user_answer_challenge_mode, width=50,
                                      height=50, font=('Roboto', 25), fg_color='#6495ED')
        self.c_button_challenge_mode = ctk.CTkButton(self.test_subframe2, text='C)', command=self.c_button_set_user_answer_challenge_mode, width=50,
                                      height=50, font=('Roboto', 25), fg_color='#6495ED')
        self.d_button_challenge_mode = ctk.CTkButton(self.test_subframe2, text='D)', command=self.d_button_set_user_answer_challenge_mode, width=50,
                                      height=50, font=('Roboto', 25), fg_color='#6495ED')
        self.e_button_challenge_mode = ctk.CTkButton(self.test_subframe2, text='E)', command=self.e_button_set_user_answer_challenge_mode, width=50,
                                      height=50, font=('Roboto', 25), fg_color='#6495ED')

        image19 = PhotoImage(data=b64decode(self.challenge_mode_purple_avance_icon))
        self.challenge_mode_avance_button = ctk.CTkButton(self.frame1, image=image19, text='', fg_color='#2b2b2b',
                                                          hover_color='#2b2b2b',
                                                          command=self.widgets_frame_5_challenge_mode)

        image20 = PhotoImage(data=b64decode(self.exit_icon))
        self.challenge_mode_exit_button = ctk.CTkButton(self.frame1, image=image20, text='', fg_color='#2b2b2b',
                                                        hover_color='#2b2b2b', command=self.widgets_frame_2)

    # função para ocultar previous_button e next_button, e sair

    def exit_func(self):
        self.previous_button.pack_forget()
        self.next_button.pack_forget()
        self.fullscreen_button.pack_forget()
        self.widgets_frame_3()

    # função para colocar e tirar do modo fullscreen

    def fullscreen_func(self):
        if self.fullscreen_option is False:
            self.root.attributes('-fullscreen', True)
            self.fullscreen_option = True
        else:
            self.root.attributes('-fullscreen', False)
            self.fullscreen_option = False

    def path_func(self):
        if self.path_option is False:
            self.path_option = True
        else:
            self.path_option = False
        self.previous_button.pack_forget()
        self.next_button.pack_forget()
        self.fullscreen_button.pack_forget()
        self.widgets_frame_4(firsttime=False)

    def path_challenge_mode_func(self):
        if self.path_option is False:
            self.path_option = True
        else:
            self.path_option = False
        self.fullscreen_button.pack_forget()
        self.widgets_frame_5_challenge_mode(firsttime=False)

    def func_previous(self):
        test_images = 'none'
        if self.test_option == 'ita':
            test_images = self.test_images_ita
        elif self.test_option == 'enem':
            if self.enem_option == 'english':
                test_images = self.test_images_enem_english
            elif self.enem_option == 'spanish':
                test_images = self.test_images_enem_spanish
            else:
                pass
        elif self.test_option == 'fuvest':
            test_images = self.test_images_fuvest
        else:
            pass
        try:
            PhotoImage(file=test_images[self.test_n-1])
            self.test_n -= 1
        except:
            self.test_n = 1
        self.previous_button.pack_forget()
        self.next_button.pack_forget()
        self.fullscreen_button.pack_forget()
        self.widgets_frame_4(firsttime=False)

    def func_next(self):
        test_images = 'none'
        if self.test_option == 'ita':
            test_images = self.test_images_ita
        elif self.test_option == 'enem':
            if self.enem_option == 'english':
                test_images = self.test_images_enem_english
            elif self.enem_option == 'spanish':
                test_images = self.test_images_enem_spanish
            else:
                pass
        elif self.test_option == 'fuvest':
            test_images = self.test_images_fuvest
        else:
            pass
        try:
            PhotoImage(file=test_images[self.test_n + 1])
            self.test_n += 1
        except:
            pass  # mantém o frame
        self.previous_button.pack_forget()
        self.next_button.pack_forget()
        self.fullscreen_button.pack_forget()
        self.widgets_frame_4(firsttime=False)

    def a_button_set_user_answer(self):
        if self.test_option == 'ita':
            self.user_answers_ita[self.test_n] = 'a'
        elif self.test_option == 'enem':
            self.user_answers_enem[self.test_n] = 'a'
        elif self.test_option == 'fuvest':
            self.user_answers_fuvest[self.test_n] = 'a'
        else:
            pass
        self.previous_button.pack_forget()
        self.next_button.pack_forget()
        self.fullscreen_button.pack_forget()
        self.widgets_frame_4(firsttime=False)

    def b_button_set_user_answer(self):
        if self.test_option == 'ita':
            self.user_answers_ita[self.test_n] = 'b'
        elif self.test_option == 'enem':
            self.user_answers_enem[self.test_n] = 'b'
        elif self.test_option == 'fuvest':
            self.user_answers_fuvest[self.test_n] = 'b'
        else:
            pass
        self.previous_button.pack_forget()
        self.next_button.pack_forget()
        self.fullscreen_button.pack_forget()
        self.widgets_frame_4(firsttime=False)

    def c_button_set_user_answer(self):
        if self.test_option == 'ita':
            self.user_answers_ita[self.test_n] = 'c'
        elif self.test_option == 'enem':
            self.user_answers_enem[self.test_n] = 'c'
        elif self.test_option == 'fuvest':
            self.user_answers_fuvest[self.test_n] = 'c'
        else:
            pass
        self.previous_button.pack_forget()
        self.next_button.pack_forget()
        self.fullscreen_button.pack_forget()
        self.widgets_frame_4(firsttime=False)

    def d_button_set_user_answer(self):
        if self.test_option == 'ita':
            self.user_answers_ita[self.test_n] = 'd'
        elif self.test_option == 'enem':
            self.user_answers_enem[self.test_n] = 'd'
        elif self.test_option == 'fuvest':
            self.user_answers_fuvest[self.test_n] = 'd'
        else:
            pass
        self.previous_button.pack_forget()
        self.next_button.pack_forget()
        self.fullscreen_button.pack_forget()
        self.widgets_frame_4(firsttime=False)

    def e_button_set_user_answer(self):
        if self.test_option == 'ita':
            self.user_answers_ita[self.test_n] = 'e'
        elif self.test_option == 'enem':
            self.user_answers_enem[self.test_n] = 'e'
        elif self.test_option == 'fuvest':
            self.user_answers_fuvest[self.test_n] = 'e'
        else:
            pass
        self.previous_button.pack_forget()
        self.next_button.pack_forget()
        self.fullscreen_button.pack_forget()
        self.widgets_frame_4(firsttime=False)

    def verify_answers(self):
        continue_answer = askyesno(title='Confirmação',
                          message='Quer mesmo encerrar a prova?')
        if continue_answer is True:
            if self.test_option == 'ita':
                user_answers = self.user_answers_ita
                feedback_answers = self.test_answers_ita
            elif self.test_option == 'enem':
                user_answers = self.user_answers_enem
                feedback_answers = self.test_answers_enem
            elif self.test_option == 'fuvest':
                user_answers = self.user_answers_fuvest
                feedback_answers = self.test_answers_fuvest
            else:
                pass

            for n_question in user_answers:

                # print(f'n_questão: {n_question}')
                # print(f'resposta do usuário: {user_answers[n_question]}')
                # print(f'resposta correta: {feedback_answers[n_question]}')

                if self.test_option == 'ita':
                    if user_answers[n_question] == feedback_answers[n_question]:
                        self.correct_answers += 1
                        self.corrected_answers_ita[n_question] = 'correct'
                    elif user_answers[n_question] == 'nenhuma':
                        self.null_answers += 1
                        self.corrected_answers_ita[n_question] = 'null'
                    else:
                        self.wrong_answers += 1
                        self.corrected_answers_ita[n_question] = 'wrong'

                elif self.test_option == 'enem':
                    if user_answers[n_question] == feedback_answers[n_question]:
                        self.correct_answers += 1
                        self.corrected_answers_enem[n_question] = 'correct'
                    elif user_answers[n_question] == 'nenhuma':
                        self.null_answers += 1
                        self.corrected_answers_enem[n_question] = 'null'
                    else:
                        self.wrong_answers += 1
                        self.corrected_answers_enem[n_question] = 'wrong'

                elif self.test_option == 'fuvest':
                    if user_answers[n_question] == feedback_answers[n_question]:
                        self.correct_answers += 1
                        self.corrected_answers_fuvest[n_question] = 'correct'
                    elif user_answers[n_question] == 'nenhuma':
                        self.null_answers += 1
                        self.corrected_answers_fuvest[n_question] = 'null'
                    else:
                        self.wrong_answers += 1
                        self.corrected_answers_fuvest[n_question] = 'wrong'
                else:
                    pass
            # print(f'Questões certas: {self.correct_answers}')
            # print(f'Questões erradas: {self.wrong_answers}')
            # print(f'Questões em branco: {self.null_answers}')
            # print(f'Dicionário das correções: {self.corrected_answers_ita}')

            # caso a pontuação dê a mais, é porque há questões anuladas. tenho que ver como contabilizar os pontos delas
            # depois, pois elas só são contabilizadas caso o usuário não digite nenhuma resposta, o que não vai acontecer
            # caso ele for fazer a prova toda (lembrar também de colocar imagens com a censura "anulada").

            self.results_individual_matters_info()
            self.widgets_frame_4_results()
        else:
            pass

    def results_individual_matters_info(self):

        if self.test_option == 'ita':

            physics_points = self.points
            portuguese_points = self.points
            english_points = self.points
            math_points = self.points
            chemical_points = self.points

            total_points = self.total_points

            for n_question in self.corrected_answers_ita:
                if (n_question >= 1 and n_question <= 5) or (n_question >=7 and n_question <= 12):
                    if self.corrected_answers_ita[n_question] == 'correct':
                        physics_points += 1
                        total_points += 1
                    else:
                        pass
                elif n_question == 6:
                    physics_points += 1
                    total_points += 1
                elif (n_question >= 13 and n_question <= 17) or (n_question >=19 and n_question <= 24):
                    if self.corrected_answers_ita[n_question] == 'correct':
                        portuguese_points += 1
                        total_points += 1
                    else:
                        pass
                elif n_question == 18:
                    portuguese_points += 1
                    total_points += 1
                elif n_question >= 25 and n_question <= 36:
                    if self.corrected_answers_ita[n_question] == 'correct':
                        english_points += 1
                        total_points += 1
                    else:
                        pass
                elif n_question >= 37 and n_question <= 48:
                    if self.corrected_answers_ita[n_question] == 'correct':
                        math_points += 1
                        total_points += 1
                    else:
                        pass
                elif n_question >= 49 and n_question <= 60:
                    if self.corrected_answers_ita[n_question] == 'correct':
                        chemical_points += 1
                        total_points += 1
                    else:
                        pass
                else:
                    pass
            self.physics_points = f'{physics_points}/12'
            self.portuguese_points = f'{portuguese_points}/12'
            self.english_points = f'{english_points}/12'
            self.math_points = f'{math_points}/12'
            self.chemical_points = f'{chemical_points}/12'
            self.total_points = f'{total_points}/60'

        elif self.test_option == 'enem':

            languages_and_codes_points = self.languages_and_codes_points
            human_science_points = self.human_science_points
            nature_science_points = self.nature_science_points
            math_points = self.math_points

            total_points = self.total_points

            for n_question in self.corrected_answers_enem:
                if n_question >= 1 and n_question <= 45:
                    if self.corrected_answers_enem[n_question] == 'correct':
                        languages_and_codes_points += 1
                        total_points += 1
                    else:
                        pass
                elif n_question >= 46 and n_question <= 90:
                    if self.corrected_answers_enem[n_question] == 'correct':
                        human_science_points += 1
                        total_points += 1
                    else:
                        pass
                elif n_question >= 91 and n_question <= 135:
                    if self.corrected_answers_enem[n_question] == 'correct':
                        nature_science += 1
                        total_points += 1
                    else:
                        pass
                elif (n_question >= 136 and n_question <= 156) or (n_question >= 158 and n_question <= 180):
                    if self.corrected_answers_enem[n_question] == 'correct':
                        math_points += 1
                        total_points += 1
                    else:
                        pass
                elif n_question == 157:
                    math_points += 1
                    total_points += 1

            self.languages_and_codes_points = f'{languages_and_codes_points}/45'
            self.human_science_points = f'{human_science_points}/45'
            self.nature_science_points = f'{nature_science_points}/45'
            self.math_points = f'{math_points}/45'

        elif self.test_option == 'fuvest':

            total_points = self.total_points

            for n_question in self.corrected_answers_fuvest:
                if (self.test_n >=1 and self.test_n <= 53) or (self.test_n >= 55 and self.test_n <= 90):
                    if self.corrected_answers_fuvest[n_question] == 'correct':
                        total_points += 1
                    else:
                        pass
                if self.test_n == 54:
                    total_points += 1
                else:
                    pass

            self.total_points = f'{total_points}/90'

    def exit_results(self):
        continue_answer = askyesno(title='Confirmação',
                                   message='Quer mesmo sair? Você perderá seus resultados')
        if continue_answer is True:
            self.reset_test_data()
            self.widgets_frame_2()
        else:
            pass

    def reset_test_data(self):
        self.user_answers_ita = tests_dicts.test_dict_ita()
        self.user_answers_enem = tests_dicts.test_dict_enem()
        self.user_answers_fuvest = tests_dicts.test_dict_fuvest()

        self.corrected_answers_ita = tests_dicts.test_dict_ita()
        self.corrected_answers_enem = tests_dicts.test_dict_enem()
        self.corrected_answers_fuvest = tests_dicts.test_dict_fuvest()

        self.correct_answers = 0
        self.wrong_answers = 0
        self.null_answers = 0

        self.points = 0

        # ita

        self.physics_points = 0
        self.portuguese_points = 0
        self.english_points = 0
        self.math_points = 0
        self.chemical_points = 0

        # enem

        self.human_science_points = 0
        self.languages_and_codes_points = 0
        self.nature_science_points = 0
        self.math_points = 0

        # fuvest

        self.total_points = 0

        # for all

        self.total_points = 0

        self.test_n = 1

    # challenge_mode functions

    def play_challenge_mode_func(self):
        self.widgets_frame_5_challenge_mode(firsttime=True)

    def a_button_set_user_answer_challenge_mode(self):
        if self.test_option == 'ita':
            self.user_answers_ita[self.test_n] = 'a'
        elif self.test_option == 'enem':
            self.user_answers_enem[self.test_n] = 'a'
        elif self.test_option == 'fuvest':
            self.user_answers_fuvest[self.test_n] = 'a'
        else:
            pass
        self.widgets_frame_5_challenge_mode(firsttime=False)

    def b_button_set_user_answer_challenge_mode(self):
        if self.test_option == 'ita':
            self.user_answers_ita[self.test_n] = 'b'
        elif self.test_option == 'enem':
            self.user_answers_enem[self.test_n] = 'b'
        elif self.test_option == 'fuvest':
            self.user_answers_fuvest[self.test_n] = 'b'
        else:
            pass
        self.widgets_frame_5_challenge_mode(firsttime=False)

    def c_button_set_user_answer_challenge_mode(self):
        if self.test_option == 'ita':
            self.user_answers_ita[self.test_n] = 'c'
        elif self.test_option == 'enem':
            self.user_answers_enem[self.test_n] = 'c'
        elif self.test_option == 'fuvest':
            self.user_answers_fuvest[self.test_n] = 'c'
        else:
            pass
        self.widgets_frame_5_challenge_mode(firsttime=False)

    def d_button_set_user_answer_challenge_mode(self):
        if self.test_option == 'ita':
            self.user_answers_ita[self.test_n] = 'd'
        elif self.test_option == 'enem':
            self.user_answers_enem[self.test_n] = 'd'
        elif self.test_option == 'fuvest':
            self.user_answers_fuvest[self.test_n] = 'd'
        else:
            pass
        self.widgets_frame_5_challenge_mode(firsttime=False)

    def e_button_set_user_answer_challenge_mode(self):
        if self.test_option == 'ita':
            self.user_answers_ita[self.test_n] = 'e'
        elif self.test_option == 'enem':
            self.user_answers_enem[self.test_n] = 'e'
        elif self.test_option == 'fuvest':
            self.user_answers_fuvest[self.test_n] = 'e'
        else:
            pass
        self.widgets_frame_5_challenge_mode(firsttime=False)

    def verify_answers_challenge_mode(self):
        continue_answer = askyesno(title='Confirmação',
                                   message='Confirma ver o resultado?')
        if continue_answer is True:
            print(self.passed_questions)
            if self.test_option == 'ita':
                if self.user_answers_ita[self.test_n] == self.test_answers_ita[self.test_n]:
                    self.challenge_correct_answer = True
                    self.total_points += 1
                else:
                    self.challenge_correct_answer = False
            elif self.test_option == 'enem':
                if self.user_answers_enem[self.test_n] == self.test_answers_enem[self.test_n]:
                    self.challenge_correct_answer = True
                    self.total_points += 1
                else:
                    self.challenge_correct_answer = False
            elif self.test_option == 'fuvest':
                if self.user_answers_fuvest[self.test_n] == self.test_answers_fuvest[self.test_n]:
                    self.challenge_correct_answer = True
                    self.total_points += 1
                else:
                    self.challenge_correct_answer = False
            else:
                pass
            self.widgets_frame_5_challenge_mode_results()
        else:
            pass

    def func_enem_english_option(self):
        self.enem_option = 'english'
        self.enem_test_option()
        self.test_answers_enem = tests.test_mode_enem(answers=True, english=True)

    def func_enem_spanish_option(self):
        self.enem_option = 'spanish'
        self.enem_test_option()
        self.test_answers_enem = tests.test_mode_enem(answers=True, spanish=True)

    # declaração de variáveis e decodificação de imagens do banco de imagens

    def images_declaration(self):
        self.logo_tats_mini = imgbank.logo_tats_mini()
        self.logo_tats = imgbank.logo_tats()
        self.play_home_icon = imgbank.play_home_icon()
        self.play_icon = imgbank.play_icon()
        self.play_icon_notime = imgbank.play_icon_notime()
        self.play_icon_withtime = imgbank.play_icon_withtime()
        self.go_icon = imgbank.go_icon()
        self.logo_ita = imgbank.logo_ita()
        self.logo_enem = imgbank.logo_enem()
        self.logo_fuvest = imgbank.logo_fuvest()
        self.logo_enem_resized = imgbank.logo_enem_resized()
        self.previous_icon = imgbank.previous_icon()
        self.next_icon = imgbank.next_icon()
        self.exit_icon = imgbank.exit_icon()
        self.fullscreen_icon = imgbank.fullscreen_icon()
        self.swap_icon = imgbank.swap_icon()
        self.end_test_icon = imgbank.end_test_icon()
        self.challenge_mode_purple_avance_icon = imgbank.challenge_mode_purple_avance_icon()
        self.challenge_mode_green_avance_icon = imgbank.challenge_mode_green_avance_icon()
        self.challenge_mode_fullscreen_icon = imgbank.challenge_mode_fullscreen_icon()
        self.challenge_mode_swap_icon = imgbank.challenge_mode_swap_icon()
        self.challenge_mode_end_test = imgbank.challenge_mode_end_test_icon()

        ###############################################################################################################
        # Preciso colocar dois bancos de dados de imagens (funções com b64code) para se adaptarem caso a
        # resolução do monitor do usuário for mais baixa.

        # No widget_frame_4, dos testes, também deve ter uma opção de ampliar a imagem que usará a função
        # subsample(2, 2), e outra opção para mover a imagem para a esquerda (relx -= 10), direita (relx += 10),
        # cima (rely -= 10) e baixo(rely +=10), com a opção de recentralizar a imagem.

        # Também separar mais os botões de resposta caso a resolução do usuário seja HD, pois eles ficam colados
        # nessa resolução.

        ###############################################################################################################
        # em matérias, fazer um loop for que vá adicionando botões conforme ele vai achando mais imagens de matérias no
        # dicionário. O dicionário deverá conter o nome da matéria, depois outro dicionário dentro deste com as imagens
        # da matéria em ordem.

        # desse modo, posso adicionar quantas imagens e matérias eu quiser, que o loop for vai ajustando os botões e
        # colocando botões de próximo e anterior embaixo, para a pessoa avançar ou retroceder para ver mais conteúdos.

        # ou posso tentar fazer um frame rolável que tenha todos os botões.
        ###############################################################################################################

Application()

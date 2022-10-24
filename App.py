import customtkinter
from controller import ControllerLogin

# Impostazione del tema
customtkinter.set_appearance_mode('Dark')
customtkinter.set_default_color_theme('blue')

''' Finestra d'avvio '''
App = customtkinter.CTk()
App.title('App')
App.geometry('1250x700')
if __name__ == '__main__':
    ControllerLogin.ControllerLogin.show(App)
    App.mainloop()

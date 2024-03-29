from turtle import right
import pyMeow,customtkinter
from setuptools import Command

process = pyMeow.open_process("retroarch.exe")
main_module = pyMeow.get_module(process, "retroarch.exe")
base_address = main_module["base"]

global test_adress
global Read_test_adress
global fly_one
global fly_two

test_adress = 0x2006C7FC
fly_one = 0x200705C7
fly_two = 0x200705C8

customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

app = customtkinter.CTk()
app.title("Spyro 3 Mod Example")
app.geometry("400x300")

def Read_mem():
 Read_test_adress = pyMeow.r_byte(process,test_adress)
 labeltest.configure(text=f"{Read_test_adress}")
    
 app.after(10, Read_mem)

 if Read_test_adress > 16:
  labellock.configure(text="Wings Unlocked!")
  pyMeow.w_byte(process,fly_one,1)
  pyMeow.w_byte(process,fly_two,1)
 else:
   labellock.configure(text="")
  
label = customtkinter.CTkLabel(master=app,font=('roboto', 33, 'bold'),text="Collect 17 Gems to Fly")
label.pack(pady=15,padx=0)

label = customtkinter.CTkLabel(master=app,font=('roboto', 33, 'bold'),text="Gems")
label.pack(pady=0,padx=0)

labeltest = customtkinter.CTkLabel(master=app,width=120,font=('roboto', 33, 'bold'),text="",text_color='Orange')
labeltest.pack(pady=0,padx=0)

labellock = customtkinter.CTkLabel(master=app,width=120,font=('roboto', 33, 'bold'),text="",text_color='Blue')
labellock.pack(pady=20,padx=0)


Read_mem()
app.mainloop()

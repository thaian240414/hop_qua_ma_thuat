from guizero import App,Text, Picture

cua_so = App(title="Hộp quà ma thuật", width=1000, height=700)

tieu_de = Text(cua_so, text= "Chào mừng đến với hộp quà ma thuật!", color="purple", size = 30)

hinh_anh = Picture(cua_so, image="hop_qua.png")

tieu_de_2 = Text(cua_so, text="Khám phá những điều kì diệu bên trong", color="green", size=15)

cua_so.display()
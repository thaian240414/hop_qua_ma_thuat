from guizero import App, Text, Box, Picture

cuaso = App(title="Giới thiệu bản thân", width=1000, height=700)


tieude1 = Text(cuaso, text="Tên: Thái An",color="#fffa73", size=15)
tieude2 = Text(cuaso, text="Tuổi: 11",color="#fffa73", size=15)
tieude3 = Text(cuaso, text="Giới tính: Nữ", color="#fffa73", size=15)
tieude4 = Text(cuaso, text="Trường: THCS Lý Thái Tổ", color="#fffa73", size=15)
hinhanh = Picture(cuaso, image="meomeo.gif")

cuaso.display()
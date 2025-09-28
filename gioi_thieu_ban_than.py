from guizero import App, Text, Box, Picture

cuaso = App(title="Giới thiệu bản thân", width=1000, height=700,bg="#ffd6ef")
header_box = Box(cuaso,width="fill", border=True)

tieude1 = Text(header_box, text="Tên: Thái An",size=30, color="#0082d9")
tieude2 = Text(header_box,text="Tuổi: 11",size=30, color="#0082d9")
tieude3 = Text(header_box,text="Giới tính: Nữ", size=30, color="#0082d9")
tieude4 = Text(header_box, text="Trường: THCS Lý Thái Tổ",size=30, color="#0082d9")
hinhanh = Picture(header_box, image="meomeo.gif", height=400)

tieude5 = Text(header_box, text="Xin chào, tôi tên là An. Đây là chương trình giới thiệu về tôi.")

cuaso.display()


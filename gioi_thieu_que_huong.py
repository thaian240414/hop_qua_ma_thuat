# Tạo một ứng dụng GUI  giới thiệu những món ăn, phong cảnh nổi tiếng ở địa phương, thành phố các bạn đang sống.

from guizero import App, Text, Box, Picture


app = App(title="Giới thiệu món ăn và cảnh nổi tiếng ở Nha Trang", width=1000, height=1000,bg="#FEF09F")

tieu_de1= Text(app, text="Khám phá Nha Trang!", size=18, color="darkblue")

hinhanh = Picture(app, image = "bunchaca.png",width=900, height=400)

tieu_de2 = Text(app, text="Đây là món ăn nổi tiếng ở Nha Trang, bún chả cá", size=19, color="#360382")

hinhanh2 = Picture(app, image = "bien.png",width=800, height=300)

tieu_de3 = Text(app, text="Đây là cảnh nổi tiếng ở Nha Trang, biển Nha Trang", size=19,color="#360382")
app.display()
from guizero import App, Text, Box, Picture


app = App(title="Bài báo", width=1362, height=806, bg="white")

box3= Box(app,width="fill")
box1 = Box(app,width="fill")
box2 = Box(app,width="800")


text1 = Text(box3,text="Người Việt mua ôtô điện nhiều thứ hai Đông Nam Á",size=30, color="red")

text2 = Text(box1, text="Sau 8 tháng đầu 2025, thị trường Việt tiêu thụ 89.970 xe thuần điện, Thái Lan dẫn\n đầu với 92.665 xe.\nViệt Nam là thị trường ôtô lớn thứ 4 Đông Nam Á về doanh số xe mới hàng năm sau\n Indonesia, Malaysia, Thái Lan, nhưng nếu tính riêng xe thuần điện chạy bằng pin\n (BEV - Battery Electric Vehicle), Việt Nam hiện xếp thứ hai", size=20)

picture = Picture(box2, image="bai_bao.png",height=600,  align="left")


app.display()
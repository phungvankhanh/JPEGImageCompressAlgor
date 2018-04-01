from tkinter import Tk,Scale,IntVar, Frame,Menu, BOTH, Label,NW, Text,Button
from PIL import Image,ImageTk
from tkinter.filedialog import Open
import tkinter.messagebox as mbox
import os
class Example(Frame):
	def __init__(self,parent):
		Frame.__init__(self,parent)
		self.parent=parent
		self.initUI()
		self.v = 1

	def initUI(self):
		self.parent.title("Phương pháp nén ảnh JPEG")
		self.pack(fill=BOTH,expand=1)

		menuBar=Menu(self.parent)  
		self.parent.config(menu=menuBar)

		fileMenu=Menu(menuBar)
		fileMenu.add_command(label="Open",command=self.onOpen)
		menuBar.add_cascade(label="File",menu=fileMenu)
		menuBar.add_command(label="About",command=self.onInfo)
		menuBar.add_command(label="Exit",command=self.quit)

		self.txt=Text(self)
		self.txt.pack(fill=BOTH,expand=1)

		lbl0=Label(self,text="Xin gửi lời cảm ơn đến thầy Nguyễn Linh Giang đã giúp đỡ chúng em hoàn thành đề tài này, mở ảnh chọn File/Open")
		lbl0.place(x=20,y=10)
		lbl1=Label(self,text="Original Image",width=20)
		lbl1.place(x=20,y=50)
		lbl2=Label(self,text="Output Image",width=20)
		lbl2.place(x=400,y=50)
		lbl3=Label(self,text="Size:",width=10)
		lbl3.place(x=20,y=300)
		lbl4=Label(self,text="Size:",width=10)
		lbl4.place(x=400,y=300)
		lbl5=Label(self,text="Tỷ lệ nén",width=10)
		lbl5.place(x=250,y=50)
		scale=Scale(self,from_=1, to=90,command=self.onScale)
		scale.place(x=270,y=80)
		self.var=IntVar()
		

		start=Button(self,text="Start",command=self.onRelease)
		start.place(x=270,y=200)
		self.a=0
		self.b=0
	def onInfo(self):
		mbox.showinfo("Information","-Đề tài:\nPhương pháp nén ảnh JPEG\n-Thành viên:\n+Phùng Văn Khánh-20142319\n+Nguyễn Thái Phương-20143522\n+Nguyễn Ngọc Đông-20141072\n+Cù Tuấn Minh-20142895\n-Ngôn ngữ:\nPython3\n-Thuật toán sử dụng:\n+Biến đổi DCT\n+Mã hóa Huffman")

	def onScale(self,val):
		self.v=int(float(val))
		self.var.set(self.v)
	def onOpen(self):
		
		if self.a!=0:
			self.lable2.destroy()
		
		ftypes=[('Python files','*.jpg'),('All files','*')]
		dlg=Open(self,filetypes=ftypes)
		fl=dlg.show()

		if fl!='':
			self.liv=Image.open(fl)
			lbl5=Label(self,text="%f MB"%(os.path.getsize(fl)/1048576.0),width=10)
			lbl5.place(x=80,y=300)
			self.liv.thumbnail((200, 200),Image.ANTIALIAS)
		

			liverpool=ImageTk.PhotoImage(self.liv)
			self.lable2=Label(self,image=liverpool)
			self.lable2.image=liverpool
			self.lable2.place(x=20,y=80)
			self.liv=Image.open(fl)
			self.a=1

	def onRelease(self):
			self.liv.save("compressed.jpg",optimize=True,quality=self.v)

			if self.b!=0:
				self.lable3.destroy()

			self.re=Image.open("compressed.jpg")
			lbl6=Label(self,text="%f MB"%(os.path.getsize("compressed.jpg")/1048576.0),width=10)
			lbl6.place(x=410,y=300)
			self.re.thumbnail((200, 200), Image.ANTIALIAS)
			release=ImageTk.PhotoImage(self.re)
			self.lable3=Label(self,image=release)
			self.lable3.image=release
			self.lable3.place(x=350,y=80)
			self.b=1


root=Tk()
root.geometry("650x330+200+100")
Example(root)
root.mainloop()




		

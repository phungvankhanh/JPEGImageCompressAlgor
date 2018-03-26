from tkinter import Tk,Scale,Canvas,IntVar, Frame,Menu, BOTH, Label,NW, Text,X,LEFT,Button,RIGHT
from PIL import Image,ImageTk
from tkinter.filedialog import Open
import tkinter.messagebox as mbox
class Example(Frame):
	def __init__(self,parent):
		Frame.__init__(self,parent)
		self.parent=parent
		self.initUI()

	def initUI(self):
		self.parent.title("Multimedia")
		self.pack(fill=BOTH,expand=1)

		menuBar=Menu(self.parent)
		self.parent.config(menu=menuBar)

		fileMenu=Menu(menuBar)
		fileMenu.add_command(label="Open",command=self.onOpen)
		menuBar.add_cascade(label="File",menu=fileMenu)
		menuBar.add_command(label="About",command=self.onInfo)
		menuBar.add_command(label="Exit",command=self.quit)

		#self.txt=Text(self)
		self.txt=Text(self)
		self.txt.pack(fill=BOTH,expand=1)

		lbl1=Label(self,text="Original Image",width=20)
		lbl1.place(x=20,y=50)
		lbl2=Label(self,text="Output Image",width=20)
		lbl2.place(x=350,y=50)

		scale=Scale(self,from_=0, to=100,command=self.onScale)
		scale.place(x=250,y=50)
		self.var=IntVar()
		

		start=Button(self,text="Start")
		start.place(x=250,y=170)
		self.a=0
		
	def onInfo(self):
		mbox.showinfo("Information","Phung Van Khanh-20142895\nNguyen Thai Phuong-\nNguyen Ngoc Dong-20141072\nCu Tuan Minh-20142895")

	def onScale(self,val):
		v=int(float(val))
		self.var.set(v)
	def onOpen(self):
		if self.a==0:
			self.liv=Image.open("1.png")
			self.liv.thumbnail((200, 200),Image.ANTIALIAS)
			liverpool=ImageTk.PhotoImage(self.liv)
			self.lable2=Label(self,image=liverpool)
			self.lable2.image=liverpool
			self.lable2.place(x=20,y=80)
			self.lable2.destroy()
		else:
			self.lable2.destroy()
		
		ftypes=[('Python files','*.jpg'),('All files','*')]
		dlg=Open(self,filetypes=ftypes)
		fl=dlg.show()

		if fl!='':
			self.liv=Image.open(fl)
			self.liv.thumbnail((200, 200),Image.ANTIALIAS)
			liverpool=ImageTk.PhotoImage(self.liv)
			self.lable2=Label(self,image=liverpool)
			self.lable2.image=liverpool
			self.lable2.place(x=20,y=80)
			self.a=1
		

root=Tk()
root.geometry("600x300+200+100")
Example(root)
root.mainloop()





		
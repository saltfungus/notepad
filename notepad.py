import tkinter 
import os     
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *
import tkinter.font as tkfont
import webbrowser

class Notepad: 
    __root = Tk()
    # default window width and height 
    __thisWidth = 300
    __thisHeight = 300
    __thisTextArea = Text(__root) 
    __thisMenuBar = Menu(__root) 
    __thisFileMenu = Menu(__thisMenuBar, tearoff=0) 
    __thisEditMenu = Menu(__thisMenuBar, tearoff=0) 
    __thisHelpMenu = Menu(__thisMenuBar, tearoff=0)
        
      
    # To add scrollbar 
    __thisScrollBar = Scrollbar(__thisTextArea)      
    __file = None
     
        
    def __init__(self,**kwargs): 
  
        # Set icon 
        try: 
                self.__root.iconbitmap(r'C:\Users\Public\Documents\Notepad-icon\notepad.ico')                
        except: 
                pass
  
        # Set window size (the default is 300x300) 
  
        try: 
            self.__thisWidth = kwargs['width'] 
        except KeyError: 
            pass
  
        try: 
            self.__thisHeight = kwargs['height'] 
        except KeyError: 
            pass
  
        # Set the window text 
        self.__root.title("Untitled - Notepad") 
  
        # Center the window 
        screenWidth = self.__root.winfo_screenwidth() 
        screenHeight = self.__root.winfo_screenheight() 
      
        # For left-alling 
        left = (screenWidth / 2) - (self.__thisWidth / 2)  
          
        # For right-allign 
        top = (screenHeight / 2) - (self.__thisHeight /2)  
          
        # For top and bottom 
        self.__root.geometry('%dx%d+%d+%d' % (self.__thisWidth, 
                                              self.__thisHeight, 
                                              left, top))  
  
        # To make the textarea auto resizable 
        self.__root.grid_rowconfigure(0, weight=1) 
        self.__root.grid_columnconfigure(0, weight=1) 
  
        # Add controls (widget) 
        self.__thisTextArea.grid(sticky = N + E + S + W) 
          
        # To open new file 
        self.__thisFileMenu.add_command(label="New", 
                                        command=self.__newFile)     
          
        # To open a already existing file 
        self.__thisFileMenu.add_command(label="Open", 
                                        command=self.__openFile) 
          
        # To save current file 
        self.__thisFileMenu.add_command(label="Save", 
                                        command=self.__saveFile)     
  
        # To create a line in the dialog         
        self.__thisFileMenu.add_separator()                                          
        self.__thisFileMenu.add_command(label="Exit", 
                                        command=self.__quitApplication) 
        self.__thisMenuBar.add_cascade(label="File", 
                                       menu=self.__thisFileMenu)      
          
        # To give a feature of cut  
        self.__thisEditMenu.add_command(label="Cut", 
                                        command=self.__cut)              
      
        # to give a feature of copy     
        self.__thisEditMenu.add_command(label="Copy", 
                                        command=self.__copy)          
          
        # To give a feature of paste 
        self.__thisEditMenu.add_command(label="Paste", 
                                        command=self.__paste)          
          
        # To give a feature of editing 
        self.__thisMenuBar.add_cascade(label="Edit", 
                                       menu=self.__thisEditMenu)      
          
        # To create a feature of description of the notepad
        self.__thisHelpMenu.add_command(label="Help", 
                                        command=self.__showHelp) 
        self.__thisHelpMenu.add_command(label="About", 
                                        command=self.__showAbout)
        self.__thisHelpMenu.add_separator()
        self.__thisHelpMenu.add_command(label="OURmedia", 
                                        command=self.__showWebsite)
        self.__thisMenuBar.add_cascade(label="Help", 
                                       menu=self.__thisHelpMenu)
  
        self.__root.config(menu=self.__thisMenuBar) 
  
        self.__thisScrollBar.pack(side=RIGHT,fill=Y)                     
          
        # Scrollbar will adjust automatically according to the content         
        self.__thisScrollBar.config(command=self.__thisTextArea.yview)      
        self.__thisTextArea.config(yscrollcommand=self.__thisScrollBar.set) 
      
          
    def __quitApplication(self): 
        ext = askquestion("Notepad-Exit?", "are you sure you want to exit") 
        if ext == 'yes':
            self.__root.destroy()
        else:
            showinfo("Notepad-return", "you will return to Notepad")
    # exit() 
  
    def __showAbout(self): 
        About = Toplevel(self.__root, bg="lightgrey")
        About.title("Notepad-About")
        About.geometry("270x200")
        About.iconbitmap(r'C:\Users\Sam Glase\Desktop\apps\app location\notepad\notepad.ico')
        Label(About, text="About us", bg="lightgrey").pack()
        Label(About, bg="lightgrey").pack()
        Label(About, text="hhh", foreground="lightgrey", bg="lightgrey").pack(side="left")
        Label(About, text="Notepad \n was made because Sam Glase \n wanted a text editor that could run on \n any hardware.\n\n\n\n\n\nversion: 1.1 author: Sam Glase", borderwidth=2, relief="groove", bg="white", anchor=NW).pack(side="right", fill="both", expand="true")
        
    def __showHelp(self): 
        showinfo("Notepad-Help","contact the owner at http://ourmediaphp.atwebpages.com/contacts.php or email samglase69@gmail.com", icon="question")
    def __showWebsite(self): 
        webbrowser.open_new(r"http://ourmediaphp.atwebpages.com")
  
    def __openFile(self): 
          
        self.__file = askopenfilename(defaultextension=".txt", 
                                      filetypes=[("All Files","*.*"), 
                                        ("Text Documents","*.txt"),
					("Python", "*.py"),
					("php","*.php"),
				        ("html","*.html"),
					("css","*.css"),
					("javascript","*.js"),
					("c++","*.cpp"),
					("c sharp","*.cs"),
					("c","*.c")	
								])
 
        if self.__file == "": 
              
            # no file to open 
            self.__file = None
        else: 
              
            # Try to open the file 
            # set the window title 
            self.__root.title(os.path.basename(self.__file) + " - Notepad") 
            self.__thisTextArea.delete(1.0,END) 
  
            file = open(self.__file,"r") 
  
            self.__thisTextArea.insert(1.0,file.read()) 
  
            file.close() 
  
          
    def __newFile(self): 
        self.__root.title("Untitled - Notepad") 
        self.__file = None
        self.__thisTextArea.delete(1.0,END) 
  
    def __saveFile(self): 
  
        if self.__file == None: 
            # Save as new file 
            self.__file = asksaveasfilename(initialfile='Untitled.txt', 
                                            defaultextension=".txt", 
                                            filetypes=[("All Files","*.*"), 
                                                ("Text Documents","*.txt"),
						("Python","*.py"),
						("php","*.php"),
						("html","*.html"),
						("css","*.css"),
						("javascript","*.js"),
						("c++","*.cpp"),
						("c sharp","*.cs"),
						("c","*.c")	
									]) 
  
            if self.__file == "": 
                self.__file = None
            else: 
                  
                # Try to save the file 
                file = open(self.__file,"w") 
                file.write(self.__thisTextArea.get(1.0,END)) 
                file.close() 
                  
                # Change the window title 
                self.__root.title(os.path.basename(self.__file) + " - Notepad") 
                  
              
        else: 
            file = open(self.__file,"w") 
            file.write(self.__thisTextArea.get(1.0,END)) 
            file.close() 
  
    def __cut(self): 
        self.__thisTextArea.event_generate("<<Cut>>") 
  
    def __copy(self): 
        self.__thisTextArea.event_generate("<<Copy>>") 
  
    def __paste(self): 
        self.__thisTextArea.event_generate("<<Paste>>")
            
  
    def run(self): 
  
        # Run main application 
        self.__root.mainloop() 
  
  
  
  
# Run main application 
notepad = Notepad(width=800,height=500) 
notepad.run() 
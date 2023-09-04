from tkinter import ttk,Tk,PhotoImage,RIDGE,GROOVE

class FrontEnd():
    def __init__(self,master):
        self.master= master
        
         
        
        #logo
        self.frame_header = ttk.Frame(self.master)
        self.frame_header.pack()
        self.logo = PhotoImage(file='ezgif-4-1d110a5907.gif').subsample(7, 7)
        print(self.logo)
        ttk.Label(self.frame_header, image=self.logo).grid(
            row=0, column=0, rowspan=2)
        ttk.Label(self.frame_header, text='Welcome to the Image Editor App!').grid(
            row=0, column=1, columnspan=1)
        ttk.Label(self.frame_header, text='Upload, edit and save your images Easily!').grid(
            row=1, column=1, columnspan=1) 
        self.frame_menu =ttk.Frame(self.master)
        self.frame_menu.pack()
        self.frame_menu.config(relief=RIDGE, padding=(50,15))
        
        
        
        
        ttk.Button(
            self.frame_menu, text="Upload An Image", command=self.upload_action).grid(row=0, column=0, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.frame_menu, text="Crop Image", command=self.crop_action).grid(row=1, column=0, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.frame_menu, text="Add Text", command=self.text_action_1).grid(row=2, column=0, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.frame_menu, text="Draw Over Image", command=self.draw_action).grid(row=3, column=0, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.frame_menu, text="Apply Filters", command=self.filter_action).grid(row=4, column=0,  padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.frame_menu, text="Blur/Smoothening", command=self.blur_action).grid(row=5, column=0, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.frame_menu, text="Adjust Levels", command=self.adjust_action).grid(row=6, column=0, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.frame_menu, text="Rotate", command=self.rotate_action).grid(row=7, column=0, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.frame_menu, text="Flip", command=self.flip_action).grid(
            row=8, column=0, padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.frame_menu, text="Save As", command=self.save_action).grid(row=9, column=0, padx=5, pady=5, sticky='sw')
    
    #"""**********************************Footer Menu********************************************"""
        self.apply_and_cancel = ttk.Frame(self.master)
        self.apply_and_cancel.pack()
        self.apply = ttk.Button(
            self.apply_and_cancel, text="Apply", command=self.apply_action)
        self.apply.grid(row=0, column=0,
                        padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.apply_and_cancel, text="Cancel", command=self.cancel_action).grid(row=0, column=1,
                         padx=5, pady=5, sticky='sw')

        ttk.Button(
            self.apply_and_cancel, text="Revert All Changes", command=self.revert_action).grid(row=0, column=2,
                                padx=5, pady=5, sticky='sw')

#"""**********************************End of Footer Menu********************************************"""

    
     
    def upload_action(self):
            pass
    def text_action_1(self):
            pass
    def draw_action(self):
            pass
    def crop_action(self):
            pass
    def filter_action(self):
            pass
    def blur_action(self):
            pass
    def flip_action(self):
            pass
    def rotate_action(self):
            pass
    def save_action(self):
            pass
    def adjust_action(self):
            pass
    def apply_action(self):
            pass
    def cancel_action(self):
            pass
    def revert_action(self):
        pass
    
        
            
        
        
        
        
        
        
root= Tk()
FrontEnd(root)
root.mainloop()
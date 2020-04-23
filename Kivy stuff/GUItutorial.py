#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 09:10:24 2019

@author: austinmccarson
"""

from tkinter import *

class Application(Frame):
    
    def __init__(self, master):
        Frame.__init__(self,master)
        self.grid()
        self.button_clicks = 0
        self.create_widgets()
        
        
    def create_widgets(self):
        self.button1 = Button(self, text = 'Number of clicks: 0')
        self.button1.grid()
        self.button1['command'] = self.update_count
        
        self.instruction = Label(self, text = 'Enter the password')
        self.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        
        self.password = Entry(self)
        self.password.grid(row = 1, column = 1, sticky = W)
        
        self.submitButton = Button(self, text = 'submit', command = self.reveal)
        self.submitButton.grid(row = 2, column = 0, sticky = W)
        
        self.text = Text(self, width = 35, height = 5, wrap = WORD)
        self.text.grid(row = 3, column = 0, columnspan = 2, sticky = W)
        
        #check buttons
        Label(self, text = 'Choose your favorite movie genre').grid(row = 0, column = 0, sticky = W)
        Label(self, text = 'Select all that apply: ').grid(row = 0, column = 0, sticky = W)

        self.comedy = BooleanVar()
        Checkbutton(self, 
                    text = 'Comedy', 
                    variable = self.comedy, 
                    command = self.update_text).grid(row = 2, column = 0, sticky = W)
        
        self.drama = BooleanVar()
        Checkbutton(self, 
                    text = 'Drama',
                    variable = self.drama, 
                    command = self.update_text).grid(row = 3, column = 0, sticky = W)
        
        self.result = Text(self, width = 40, height = 5, wrap = WORD)
        self.result.grid(row = 5, column = 0, columnspan = 3)
        
        #RadioButtons
        Label(self, text = "Choose your favorite movie").grid(row = 5, column = 0, sticky = W)
        Label(self, text = "Selecting one: ").grid(row = 6, column = 0, sticky = W)
        
        self.favorite = StringVar()
        
        Radiobutton(self, text = 'Comedy',
                    variable = self.favorite,
                    command = self.update_RBtext).grid(row = 7, column = 0, sticky = W)
        
        Radiobutton(self, text = 'Drama',
                    variable = self.favorite,
                    command = self.update_RBtext).grid(row = 8, column = 0, sticky = W)
        
        self.result = Text(self, width = 40, height = 5, wrap = WORD)
        self.result.grid(row = 9, column = 0, columnspan = 3)
        
        
    def update_RBtext(self):
        message = "Your favorite movie is: "
        message += self.favorite.get()
        
        self.result.delete(0.0, END)
        self.result.insert(0.0, message)
        
        
    def update_text(self):
        likes = "" 
        
        if self.comedy.get():
            likes += "You like comedy."
        if self.drama.get():
            likes += "You like drama."
            
        self.result.delete(0.0, END)
        self.result.insert(0.0, likes)
        
        
        
    def reveal(self):
        content = self.password.get()
        
        if content == 'password':
            message = "ACCESS GRANTED"
        else :
            message = "ACCESS DENIED"
        self.text.delete(0.0, END)
        self.text.insert(0.0, message)
        
        
    def update_count(self):
        self.button_clicks += 1
        self.button1['text'] = 'Number of clicks: ' + str(self.button_clicks)

#create the window
root = Tk()
root.title('Password')
root.geometry('700x500')

app = Application(root)

root.mainloop()

#modify root window
#root.title('Credit Dissector')
#root.geometry('500x700')
#
#app = Frame(root)
#app.grid()
#
#label = Label(app, text = 'this is a label')
#label.grid()
#
#button1 = Button(app, text = 'this is a button')
#button1.grid()
#
#button2 = Button(app)
#button2.grid()
#button2.configure(text = 'Text')
#
#button3 = Button(app)
#button3.grid()
#button3['text'] = "more text"
#
#
#
##initialize event loop
#root.mainloop()
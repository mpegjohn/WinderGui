#!/usr/bin/python

from Tkinter import *
fields = 'Last Name', 'First Name', 'Job', 'Country'

def fetch(entries):
   for entry in entries:
      field = entry[0]
      text  = entry[1].get()
      print('%s: "%s"' % (field, text))


def makeform(root, fields):
   entries = []
   for field in fields:
      row = Frame(root)
      lab = Label(row, width=15, text=field, anchor='w')
      ent = Entry(row)
      row.pack(side=TOP, fill=X, padx=5, pady=5)
      lab.pack(side=LEFT)
      ent.pack(side=RIGHT, expand=YES, fill=X)
      entries.append((field, ent))
   return entries

class App:
   def __init__(self, master):
      self.var = IntVar()
      frame = Frame(master)
      frame.grid()
      f2 = Frame(master, width=600, height=500)
      f2.grid(row=0, column=1)
      button = Checkbutton(frame, text='show', variable=self.var, command=self.fx)
      button.grid(row=0, column=0)
      msg2 = """I feel bound to give them full satisfaction on this point"""
      self.v = Message(f2, text=msg2)


   def fx(self):
      if self.var.get():
         self.v.grid(column=1, row=0, sticky=N)
      else:
         self.v.grid_remove()


def main():
   root = Tk()

   app = App(root)


  # Label(text="one").pack()

   #separator = Frame(root, height=150, width = 300)
   #separator.pack(fill=X, padx=5, pady=5)

   #lab = Label(separator, text="two").pack()

   root.mainloop()


   ents = makeform(root, fields)
   root.bind('<Return>', (lambda event, e=ents: fetch(e)))
   b1 = Button(root, text='Show',
               command=(lambda e=ents: fetch(e)))
   b1.pack(side=LEFT, padx=5, pady=5)
   b2 = Button(root, text='Quit', command=root.quit)
   b2.pack(side=LEFT, padx=5, pady=5)
   root.mainloop()

if __name__ == '__main__':
   main()
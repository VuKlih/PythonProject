import tkinter
import tkinter.ttk
import tkinter.messagebox
from Database import *
from SearchClientInfo import *
from SearchWindow import *
from UpdateWindow import *
from Values import *

class HomePage():
    def __init__(self):
        self.homePageWindow = tkinter.Tk()
        self.homePageWindow.wm_title("Water Information Management System")
        self.homePageWindow.wm_resizable(False, False)
        self.homePageWindow.geometry("1160x630+100+65")
        self.homePageWindow.iconbitmap("D:\B2\PythonProject\icon\label.ico")
        
        lbl = tkinter.Label(self.homePageWindow, text="Water Information Management System", font="arial 20 bold", bd = 10  )
        lbl.pack(side="top", fill="x")

        self.id = tkinter.StringVar()
        self.fName = tkinter.StringVar()
        self.lName = tkinter.StringVar()
        self.address = tkinter.StringVar()
        self.phone = tkinter.StringVar()
        self.email = tkinter.StringVar()
        self.wateramount = tkinter.StringVar() 

        self.genderList = ["Male", "Female", "Other"]
        self.dateList = list(range(1, 32))
        self.monthList = list(range(1, 13))
        self.yearList = list(range(1900, 2024))

#---FRAME----------------------------------------------------------------------------------------------------------------------
        self.F1 = tkinter.LabelFrame(self.homePageWindow, text = "Insert Client Infor")
        self.F1.place(x=20, y=55, width=690, height=270)

        self.F2 = tkinter.LabelFrame(self.homePageWindow, text = "Bill Details")
        self.F2.place(x=720, y=55, width=425, height=270)

        self.F3 = tkinter.LabelFrame(self.homePageWindow, text = "Display")
        self.F3.place(x=20, y=326, width=1125, height=270)

        self.innerFrame3 = tkinter.Frame(self.F3, width=900, height=200)
        self.innerFrame3.place(width=1000, height=250)

#---Insert client infor box----------------------------------------------------------------------------------------------------------------------
        tkinter.Label(self.F1, text = "Client ID",  width = 25).grid(pady = 5, column = 0, row = 0)
        tkinter.Label(self.F1, text = "First Name",  width = 25).grid(pady = 5, column = 0, row = 1)
        tkinter.Label(self.F1, text = "Last Name",  width = 25).grid(pady = 5, column = 0, row = 2)
        tkinter.Label(self.F1, text = "DOB",  width = 25).grid(pady = 5, column = 0, row = 3)
        tkinter.Label(self.F1, text = "Gender",  width = 25).grid(pady = 5, column = 0, row = 4)
        tkinter.Label(self.F1, text = "Home Address",  width = 25).grid(pady = 5, column = 0, row = 5)
        tkinter.Label(self.F1, text = "Phone Number",  width = 25).grid(pady = 5, column = 2, row = 0)
        tkinter.Label(self.F1, text = "Email ID",  width = 25).grid(pady = 5, column = 2, row = 1)
        tkinter.Label(self.F1, text = "Bill period from",  width = 25).grid(pady = 5, column = 2, row = 2)
        tkinter.Label(self.F1, text = "Bill period to",  width = 25).grid(pady = 5, column = 2, row = 3)
        tkinter.Label(self.F1, text = "Amount of water (m3)",  width = 25).grid(pady = 5, column = 2, row = 4)
        
        self.idEntry = tkinter.Entry(self.F1,  width = 25, textvariable = self.id)
        self.fNameEntry = tkinter.Entry(self.F1,  width = 25, textvariable = self.fName)
        self.lNameEntry = tkinter.Entry(self.F1,  width = 25, textvariable = self.lName)
        self.addressEntry = tkinter.Entry(self.F1,  width = 25, textvariable = self.address)
        self.phoneEntry = tkinter.Entry(self.F1,  width = 25, textvariable = self.phone)
        self.emailEntry = tkinter.Entry(self.F1,  width = 25, textvariable = self.email)
        self.wateramountEntry = tkinter.Entry(self.F1, width = 25, textvariable = self.wateramount)

        self.idEntry.grid(pady = 5, column = 1, row = 0)
        self.fNameEntry.grid(pady = 5, column = 1, row = 1)
        self.lNameEntry.grid(pady = 5, column = 1, row = 2)
        self.addressEntry.grid(pady = 5, column = 1, row = 5)
        self.phoneEntry.grid(pady = 5, column = 3, row = 0)
        self.emailEntry.grid(pady = 5, column = 3, row = 1)
        self.wateramountEntry.grid(pady = 5, column = 3, row = 4)
        
        self.dobBox = tkinter.ttk.Combobox(self.F1, values = self.dateList)
        self.mobBox = tkinter.ttk.Combobox(self.F1, values = self.monthList)
        self.yobBox = tkinter.ttk.Combobox(self.F1, values = self.yearList)
        self.billperiodfrom_dateBox = tkinter.ttk.Combobox(self.F1, values = self.dateList, width = 4)
        self.billperiodfrom_monthBox = tkinter.ttk.Combobox(self.F1, values = self.monthList, width = 10)
        self.billperiodfrom_yearBox = tkinter.ttk.Combobox(self.F1, values = self.yearList, width = 4)
        self.billperiodto_dateBox = tkinter.ttk.Combobox(self.F1, values = self.dateList, width = 4)
        self.billperiodto_monthBox = tkinter.ttk.Combobox(self.F1, values = self.monthList, width = 10)
        self.billperiodto_yearBox = tkinter.ttk.Combobox(self.F1, values = self.yearList, width = 4)
        self.genderBox = tkinter.ttk.Combobox(self.F1, values = self.genderList)

        self.dobBox.place(y = 99, x=181, width=40, height=17)
        self.mobBox.place(y = 99, x=223, width=40, height=17)
        self.yobBox.place(y = 99, x=265, width=50, height=17)
        self.billperiodfrom_dateBox.place(y = 69, x=520, width=40, height=17)
        self.billperiodfrom_monthBox.place(y = 69, x=562, width=40, height=17)
        self.billperiodfrom_yearBox.place(y = 69, x=604, width=50, height=17)
        self.billperiodto_dateBox.place(y = 99, x=520, width=40, height=17)
        self.billperiodto_monthBox.place(y = 99, x=562, width=40, height=17)
        self.billperiodto_yearBox.place(y = 99, x=604, width=50, height=17)
        self.genderBox.place(y = 130, x=181, width=155, height=17)
        
        #button
        tkinter.Button(self.F1, width = 20, text = "Insert", command = self.Insert).grid(pady = 15, padx = 5, column = 2, row = 6)
        tkinter.Button(self.F1, width = 20, text = "Reset", command = self.Reset).grid(pady = 15, padx = 5, column = 3, row = 6)

#---Bill details box----------------------------------------------------------------------------------------------------------------------
        bDetail_scrol = tkinter.Scrollbar(self.F2, orient="vertical")
        bDetail_scrol.pack(side="right", fill="y")

        self.bDetail_text = tkinter.Text(self.F2, font='arial 13', yscrollcommand=bDetail_scrol.set)
        self.bDetail_text.pack(fill="both")
        bDetail_scrol.config(command=self.bDetail_text.yview)

#---Display box----------------------------------------------------------------------------------------------------------------------
        self.style = tkinter.ttk.Style()
        self.style.theme_use('default')
        self.style.configure("Treeview", background = [('selected', "347083")],)
        
        self.clientinfo_scrollbarx = tkinter.Scrollbar(self.innerFrame3, orient="horizontal")
        self.clientinfo_scrollbary = tkinter.Scrollbar(self.innerFrame3, orient="vertical")
        self.clientinfo_scrollbarx.pack(side="bottom", fill="x", )
        self.clientinfo_scrollbary.pack(side="right", fill="y", )

        self.clientinfo_treeview = tkinter.ttk.Treeview(self.innerFrame3, xscrollcommand=self.clientinfo_scrollbarx.set ,yscrollcommand=self.clientinfo_scrollbary.set, selectmode="extended")
        self.clientinfo_treeview.pack(fill="both", expand=1)

        self.clientinfo_scrollbarx.config(command=self.clientinfo_treeview.xview)
        self.clientinfo_scrollbary.config(command=self.clientinfo_treeview.yview)

        self.clientinfo_treeview['columns'] = ("Client ID", "Name", "DOB", "Gender", "Home address", "Phone number", "Email", "Bill period", "Amount of water", "Charges")
        self.clientinfo_treeview.column("#0", width=0, stretch= 0)
        self.clientinfo_treeview.column("Client ID", anchor= "center", width=100)
        self.clientinfo_treeview.column("Name", anchor= "center", width=180)
        self.clientinfo_treeview.column("DOB", anchor= "center", width=110)
        self.clientinfo_treeview.column("Gender", anchor= "center", width=100)
        self.clientinfo_treeview.column("Home address", anchor= "center", width=180)
        self.clientinfo_treeview.column("Phone number", anchor= "center", width=140)
        self.clientinfo_treeview.column("Email", anchor= "center", width=180)
        self.clientinfo_treeview.column("Bill period", anchor= "center", width=180)
        self.clientinfo_treeview.column("Amount of water", anchor= "center", width=140)
        self.clientinfo_treeview.column("Charges", anchor= "center", width=140)
        
        self.clientinfo_treeview.heading("#0", text="", anchor= "w")
        self.clientinfo_treeview.heading("Client ID", text="Client ID", anchor= "center" )
        self.clientinfo_treeview.heading("Name",text="Name", anchor= "center")
        self.clientinfo_treeview.heading("DOB",text="DOB", anchor= "center")
        self.clientinfo_treeview.heading("Gender",text="Gender", anchor= "center")
        self.clientinfo_treeview.heading("Home address",text="Home address", anchor= "center")
        self.clientinfo_treeview.heading("Phone number",text="Phone number", anchor= "center")
        self.clientinfo_treeview.heading("Email",text="Email", anchor= "center")
        self.clientinfo_treeview.heading("Bill period",text="Bill period", anchor= "center")
        self.clientinfo_treeview.heading("Amount of water",text="Amount of water (m3)", anchor= "center")
        self.clientinfo_treeview.heading("Charges",text="Charges (VND)", anchor= "center")
        
        self.clientinfo_treeview.tag_configure('oddrow', background='white')
        self.clientinfo_treeview.tag_configure('evenrow', background='light blue')
        
        # buttons
        tkinter.Button(self.F3, width = 10, text = "Search",command = self.Search).place(x=1010, y =70)
        tkinter.Button(self.F3, width = 10, text = "Update",command= self.Update ).place(x=1010, y =100)
        tkinter.Button(self.F3, width = 10, text = "Delete",command = self.Delete).place(x=1010, y =130)
        
#-------------------------------------------------------------------------------------------------------------------------
    
        self.clientinfo_treeview.bind("<ButtonRelease>",self.select_record)
        self.query_database()
        self.homePageWindow.mainloop()


    def Insert(self):
        self.values = Values()
        self.database = Database()
        self.test = self.values.Validate(self.idEntry.get(), self.phoneEntry.get(), self.emailEntry.get(), self.wateramountEntry.get(),)
        if (self.test == "SUCCESS"):
            self.database.Insert(self.idEntry.get(), self.fNameEntry.get(), self.lNameEntry.get(), self.dobBox.get(), self.mobBox.get(), self.yobBox.get(), self.genderBox.get(), self.addressEntry.get(), self.phoneEntry.get(), self.emailEntry.get(), self.billperiodfrom_dateBox.get(), self.billperiodfrom_monthBox.get(),self.billperiodfrom_yearBox.get(), self.billperiodto_dateBox.get(), self.billperiodto_monthBox.get(), self.billperiodto_yearBox.get(),self.wateramountEntry.get())
            tkinter.messagebox.showinfo("Inserted data", "Successfully inserted the above data in the database")
            
            self.bDetail_text.delete(1.0, tkinter.END)
            self.bDetail_text.insert(tkinter.END, f'\n\t             CLIENT ID:\t{self.idEntry.get()}')
            self.bDetail_text.insert(tkinter.END, f'\n  ---------------------------------------------------------------')
            self.bDetail_text.insert(tkinter.END, f'\n\tName:                \t{self.fNameEntry.get()} {self.lNameEntry.get()}')
            self.bDetail_text.insert(tkinter.END, f'\n\tGender:              \t{self.genderBox.get()}')
            self.bDetail_text.insert(tkinter.END, f'\n\tDOB:                  \t{self.dobBox.get()} - {self.mobBox.get()} - {self.yobBox.get()}')
            self.bDetail_text.insert(tkinter.END, f'\n\tAddress:             \t{self.addressEntry.get()}')
            self.bDetail_text.insert(tkinter.END, f'\n\tEmail:                 \t{self.emailEntry.get()}')
            self.bDetail_text.insert(tkinter.END, f'\n\tPhone number:    \t{self.phoneEntry.get()}')
            self.bDetail_text.insert(tkinter.END, f'\n  ---------------------------------------------------------------')
            self.bDetail_text.insert(tkinter.END, f'\n\tPeriod:               \t{self.billperiodfrom_dateBox.get()}/{self.billperiodfrom_monthBox.get()}/{self.billperiodfrom_yearBox.get()} - {self.billperiodto_dateBox.get()}/{self.billperiodto_monthBox.get()}/{self.billperiodto_yearBox.get()}')
            self.bDetail_text.insert(tkinter.END, f'\n\tWater Consumption(m3): \t{self.wateramountEntry.get()}')
            self.bDetail_text.insert(tkinter.END, f'\n  ---------------------------------------------------------------')
            self.bDetail_text.insert(tkinter.END, f'\n\tTOTAL DUE:            \t{self.database.returnCharge(self.idEntry.get())}')
            self.bDetail_text.insert(tkinter.END, f'\n\t (VND)\n')
            
            self.Reset()
            self.clientinfo_treeview.delete(*self.clientinfo_treeview.get_children())
            self.query_database()
            
        else:
            if self.test == "existed id":
                tkinter.messagebox.showerror("Value Error", "This ID is already existed:\n-> Please enter the ID again")
            elif self.test == "id":
                self.valueErrorMessage = "Invalid input in field " + self.test +"\n The ID must be a 5 digit number and greater than 9999"
                tkinter.messagebox.showerror("Value Error", self.valueErrorMessage)
            elif self.test == "phone":
                self.valueErrorMessage = "Invalid input in field " + self.test +"\n The phone number must be a 10 digit number"
                tkinter.messagebox.showerror("Value Error", self.valueErrorMessage)
            elif self.test == "email":
                self.valueErrorMessage = "Invalid input in field " + self.test +"\n The email must contain the characters @ and . "
            else:
                self.valueErrorMessage = "Invalid input in field " + self.test +"\n The amount of water must be an integer"
                tkinter.messagebox.showerror("Value Error", self.valueErrorMessage)

    def Reset(self):
        self.idEntry.delete(0, tkinter.END)
        self.fNameEntry.delete(0, tkinter.END)
        self.lNameEntry.delete(0, tkinter.END)
        self.dobBox.set("")
        self.mobBox.set("")
        self.yobBox.set("")
        self.genderBox.set("")
        self.addressEntry.delete(0, tkinter.END)
        self.phoneEntry.delete(0, tkinter.END)
        self.emailEntry.delete(0, tkinter.END)
        self.billperiodfrom_dateBox.delete(0, tkinter.END)
        self.billperiodfrom_monthBox.delete(0, tkinter.END)
        self.billperiodfrom_yearBox.delete(0, tkinter.END)
        self.billperiodto_dateBox.delete(0, tkinter.END)
        self.billperiodto_monthBox.delete(0, tkinter.END)
        self.billperiodto_yearBox.delete(0, tkinter.END)
        self.wateramountEntry.delete(0, tkinter.END)

    def Search(self):
        self.searchWindow = SearchWindow()

    def Delete(self):
        x = self.clientinfo_treeview.selection()[0]
        #self.clientinfo_treeview.delete(x)

        self.database = Database()
        self.database.Delete(self.clientinfo_treeview.item(x)['values'][0])
        self.bDetail_text.delete(1.0, tkinter.END)
        self.query_database()
        tkinter.messagebox.showinfo("deleted data","Deleted successfully!")        

    def treeview_billDetails_afterUpdate(self, item, list):
        # Cập nhật Treeview của window 1 khi có thay đổi trên window 2
        self.clientinfo_treeview.delete(*self.clientinfo_treeview.get_children())
        for record in item:
            self.clientinfo_treeview.insert('',"end", values= record)

        # show undated info in bill details box after updating data
        self.updatedRecord = list[0]
        self.billDetails(self.updatedRecord)

    def Update(self):
        x = self.clientinfo_treeview.selection()[0]
        print(x)
        self.updateWindow = UpdateWindow(self.clientinfo_treeview.item(x)["values"], self.treeview_billDetails_afterUpdate)
    
    def billDetails(self, record):# record is a tuple       
        self.bDetail_text.delete(1.0, tkinter.END)
        self.bDetail_text.insert(tkinter.END, f'\n\t             CLIENT ID:\t{record[0]}')
        self.bDetail_text.insert(tkinter.END, f'\n  ---------------------------------------------------------------')
        self.bDetail_text.insert(tkinter.END, f'\n\tName:                \t{record[1]}')
        self.bDetail_text.insert(tkinter.END, f'\n\tGender:              \t{record[3]}')
        self.bDetail_text.insert(tkinter.END, f'\n\tDOB:                  \t{record[2]}')
        self.bDetail_text.insert(tkinter.END, f'\n\tAddress:             \t{record[4]}')
        self.bDetail_text.insert(tkinter.END, f'\n\tEmail:                 \t{record[6]}')
        self.bDetail_text.insert(tkinter.END, f'\n\tPhone number:   \t{record[5]}')
        self.bDetail_text.insert(tkinter.END, f'\n  ---------------------------------------------------------------')
        self.bDetail_text.insert(tkinter.END, f'\n\tPeriod:               \t{record[7]}')
        self.bDetail_text.insert(tkinter.END, f'\n\tWater Consumption(m3): \t{record[8]}')
        self.bDetail_text.insert(tkinter.END, f'\n  ---------------------------------------------------------------')
        self.bDetail_text.insert(tkinter.END, f'\n\tTOTAL DUE:       \t{record[9]}')
        self.bDetail_text.insert(tkinter.END, f'\n\t  (VND)\n')

    def select_record(self, select):
        self.Reset()

        self.selected = self.clientinfo_treeview.focus()
        # test: print(self.selected)
        self.values = self.clientinfo_treeview.item(self.selected, 'values')
        print(self.values)
        
        #show selected record in the bill Details box
        self.billDetails(self.values)

    def query_database(self):
        self.database = Database()
        records=self.database.Display()

        for item in self.clientinfo_treeview.get_children():
            self.clientinfo_treeview.delete(item)

        global count
        count = 0
        for record in records:
            if count%2==0:
                self.clientinfo_treeview.insert('',"end", values= record, tags='evenrow')
            else:
                self.clientinfo_treeview.insert('',"end", values= record, tags='oddrow')
            count += 1

if __name__ == "__main__":
    homePage = HomePage()
from ast import Pass
import win32clipboard as cb
import json
from tkinter import *
#from tkinter import ttk
from time import sleep

#from openpyxl import load_workbook

#wb = load_workbook("excel2022.xlsx")
#ws = wb.active
repeated_chars = []

"""for row_number in range(1, 3001):
    row_value = ws.cell(row=row_number, column=1).value
    for one_dict in list_of_dicts:"""

parsed_dict = open("charsdictsaved.json", encoding="utf8")


list_of_dicts_jsoned = json.load(parsed_dict)

parsed_dict.close()


"""

for one_dict in list_of_dicts_jsoned:

    for row_number in range(1, ws.max_row+1):
        row_value = ws.cell(row=row_number, column=1).value
        #print(row_value)
        current_row_definition = ws.cell(row = row_number, column=10).value #Definition in cell before writing, might be None.
        #print(current_row_definition)
        if one_dict["simplified"] == row_value:
            if current_row_definition == None: #Checks if definition has already been written 1 or more times. (Remember, not necesarilly saved in file.)
                #print(one_dict["english"])
                cell_value = str(one_dict["english"] + "(("+one_dict["pinyin"]+"))")
                #print(cell_value)
                ws.cell(row=row_number, column=10, value=cell_value)
                #print(str(current_row_definition) + "   " + str(new_row_definition))
            else:
                current_row_definition = ws.cell(row = row_number, column=10).value
                new_row_definition = one_dict["english"]
                joined_definitions = (str(current_row_definition) + " |/|/| " + str(new_row_definition) +"(("+str(one_dict["pinyin"]))+"))"
                #print(str(joined_definitions))
                ws.cell(row=row_number, column=10, value=joined_definitions)
                #repeated_chars.append(row_value)
                #print(str(current_row_definition) + "   " + str(new_row_definition))
                
                

            
               

            #print(str(row_number) + str(current_row_definition))
            #print("Matched character" + str(one_dict["simplified"]) + str(row_value) + str(one_dict["english"]))

#wb.save("excel2022.xlsx")
#print("Finished!")
"""


#print(repeated_chars)
#print(len(repeated_chars))



"""Try doing the list method, to see if it works better than this! Also try testing with less data on the cedict txt to understand whats going on."""

definition_list = []
component_definition_list = []
final_component_definition_list = []
data = []
formated_component_definition_list = []


def search_char(char):
    for one_dict in list_of_dicts_jsoned:
        if one_dict["simplified"] == char: #If "if" is not triggered, it shows "referenced before assignment" for "formated_definition_list"
            #print (one_dict["english"])
            definition_list.append(one_dict["english"]+"(("+one_dict["pinyin"]+"))")
            formated_definition_list = "\n\n".join(definition_list)
            #engdefinition.set(formated_definition_list) #Use this if you want to use Entry widget instead of Text Widget.
    #formated_definition_list += "\n\n" + ("////////////////////////////////////////////////////////////////////////////////////////////////////")
 
    definition_text.delete(0.1,"end")
    
    try:
        definition_text.insert("end", formated_definition_list) #Use this if you want to use Text Widget instead of Entry widget.
        #formated_definition_list += "\n\n" + ("////////////////////////////////////////////////////////////////////////////////////////////////////") 
        definition_text.insert("end", "\n\n" + ("//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////"))

    except UnboundLocalError:
        #print ("UnboundLocalError caught")
        definition_text.insert(1.0, "INPUT NOT VALID")
    definition_list.clear()
    #print("code reached")

def add_definition(char, index):
    for one_dict in list_of_dicts_jsoned:
        if one_dict["simplified"] == char: #If "if" is not triggered, it shows "referenced before assignment" for "formated_definition_list"
            #print (one_dict["english"])
            
            if len(component_definition_list) > 0:
                if str(index) == component_definition_list[-1][-1]:
                    #component_definition_list.pop(0)
                    component_definition_list.append(one_dict["simplified"] + ": " + (one_dict["english"]+"(("+one_dict["pinyin"]+"))"+ str(index)))
                    final_component_definition_list.append(one_dict["simplified"] + ": " + (one_dict["english"]+"(("+one_dict["pinyin"]+"))"))
                    #final_component_definition_list.append(one_dict["english"]+"(("+one_dict["pinyin"]+"))"+ str(index))
                    print("EQUAL" + str(index) + str(component_definition_list[-1][-1]))
                if str(index) != component_definition_list[-1][-1]:
                    print("UNEQUAL" + str(index) + str(component_definition_list[-1][-1]))
                    #component_definition_list.pop(0)
                    component_definition_list.append("//////////////////////////////////////////////////////////////////////////////////////////" + "\n\n" + one_dict["simplified"] + ": " + one_dict["english"]+"(("+one_dict["pinyin"]+"))" + str(index))
                    final_component_definition_list.append("----------------------------------------------------------------------------------------------------" + "\n\n" + one_dict["simplified"] + ": " + one_dict["english"]+"(("+one_dict["pinyin"]+"))")
                    #final_component_definition_list.append("//////////////////////////////////////////////////////////////////////////////////////////" + one_dict["english"]+"(("+one_dict["pinyin"]+"))"+ str(index))
            else:
                print("ELSE" + str(component_definition_list) + str(char))
                component_definition_list.append(one_dict["simplified"] + ": " + one_dict["english"]+"(("+one_dict["pinyin"]+"))"+ str(index))
                final_component_definition_list.append(one_dict["simplified"] + ": " + one_dict["english"]+"(("+one_dict["pinyin"]+"))")
                #final_component_definition_list.append(one_dict["english"]+"(("+one_dict["pinyin"]+"))"+ str(index))
            #print("LAST PRINT" + str(component_definition_list))
            #component_definition_list.append(one_dict["english"]+"(("+one_dict["pinyin"]+"))")
            print(component_definition_list)
    formated_component_definition_list = "\n\n".join(final_component_definition_list)
    print(formated_component_definition_list)
            #engdefinition.set(formated_definition_list) #Use this if you want to use Entry widget instead of Text Widget.
    component_definition_text.delete("1.0", "end") #I dont know why this has to be added, but fixex the definition text messing up when writing "核动力".
    component_definition_text.insert("1.0", formated_component_definition_list) #Use this if you want to use Text Widget instead of Entry widget.
    print("DEFINITION TEXT = " + str(component_definition_text.get("1.0", "end")))

           
def input_char():
    char = input("input character     ")
    #print ("input succesful")
    search_char(char)

def get_text():
    inputed_characters = input_box.get("1.0","end-1c")
    search_char(inputed_characters)
    split_chars(inputed_characters)

def split_chars(inputed_characters):
    if len(inputed_characters) > 1 and SearchMode.get() == 1:
        component_definition_list.clear()
        final_component_definition_list.clear()
        component_definition_text.delete("1.0", "end")
        print("See if its deleted" + str(component_definition_list))
        component_list = list(inputed_characters)
        for char in component_list:
            index = component_list.index(char)
            add_definition(char, index)
        component_definition_text.insert("end", "\n\n" + "//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////")
    if SearchMode.get() == 2:
        pass
    if len(inputed_characters) == 1:
        component_definition_text.delete("1.0", "end")
        
      
def callback(event):
    get_text()
    return 'break'

def update(data):
    my_list.delete(0, END)
    my_list.value = "tests"
    #print(my_list.value)   
    #for item in data: Example code
        #my_list.insert(END, item) Example code
    #for one_dict in data:
        #my_list.insert(END, one_dict["simplified"])
        #This code is commented because except for the deletion (I think), it is done with the check() function.

      
def search_root(one_dict, typed):
    one_dict_len = len(one_dict["simplified"])
    typed_len = len(typed)
    typed_range = range(typed_len)
    Counter = 0
    if typed_len <= one_dict_len:
        for x in typed_range:
            if typed[x] == one_dict["simplified"][x]:
                data.append(one_dict["simplified"])
                Counter += 1
            if Counter == typed_len:
                my_list.insert(END, one_dict["simplified"])

def disable_suggestions():
    my_list.delete(0)

                

def find_presence(one_dict, typed):
    if typed in one_dict["simplified"]:
         data.append(one_dict["simplified"])
         my_list.insert(END, one_dict["simplified"]) 
         #print(data)
         #print("test")
            

def fillout(e):
    #Delete whatever is in the entry box
    #my_entry.delete(0, END)
    input_box.delete("1.0","end-1c")

    #Add clicked list item to entry box
    #my_entry.insert(0, my_list.get(ANCHOR))
    input_box.insert("1.0", my_list.get(ANCHOR))

#Create function to check entry vs listbox
def check(e=None):# grab what was typed. None is used so func is callable outside of tkinter binds.
    #typed = my_entry.get()
    typed = input_box.get("1.0","end-1c")
    #print(typed + "lol")
    if typed == "":
        pass
        #print("empty11")
        #data = toppings Example code
        #for one_dict in list_of_dicts_jsoned:
            #data = "" #empty string for now, so it shows white list if nothing is written. If you want to show al chars maybe you need to have a list with all characters.

    else:
        print("filled")

        data.clear()
        my_list.delete(0, END)
        for one_dict in list_of_dicts_jsoned:
            if ModeNo.get() == 1:
                find_presence(one_dict, typed)
            if ModeNo.get() == 2:
                search_root(one_dict, typed)
            if ModeNo.get() ==3:
                disable_suggestions()

def toggle_search_mode():
    print("toggle entered")
    print(SearchMode.get())
    if SearchMode.get() == 1:
        print("lmfao")
        SearchMode.set(2)
        btn_text.set("DISABLED")
        component_definition_text.delete(0.1,"end")

    elif SearchMode.get() == 2:
        SearchMode.set(1)
        btn_text.set("ENABLED")
        inputed_characters = input_box.get("1.0","end-1c")
        split_chars(inputed_characters)


    # Update our ListBox with selected items (Already done in this function, no need to call update())
    #update(data)
def print_int():
    check()
    print(ModeNo.get())

def paste_def(e):
    cb.OpenClipboard()
    try:
        CbText = cb.GetClipboardData()
        input_box.delete("1.0","end-1c")
        input_box.insert(1.0, CbText)
    except TypeError:
        input_box.insert(1.0, "CB Empty!")
    cb.CloseClipboard()

 



root = Tk()

root.title("CCedict GUI V1.3")

ModeNo = IntVar()
SearchMode = IntVar()
SearchMode.set(1)
btn_text = StringVar()
btn_text.set("ENABLED")

#root.geometry("1000x1000")
#engdefinition = StringVar(value= "hello")
#engdefinition.set("definition")

frm = Frame(root, width=500, height=500, background="#4E5362")
frm.grid(column = 1, row = 1)
frm2 = Frame(frm, width=500, height=500, background="#4E5362")#4E5362
frm2.grid(column = 1, row = 1)
frm3 = Frame(frm, width=200, height=550, background="#4E5362")
frm3.grid(column=2, row= 1)
frm4 = Frame(frm2, width=100, height=100, background="#4E5362")
frm4.grid(column=1, row=8)
Button(frm2, text="Quit", command=root.destroy).grid(column=1, row=9, pady=(40, 0))
input_box = Text(frm3, height = 1, width = 10, font=("DengXian", 18), wrap="none",bg="#4B6478", fg="white", insertbackground="white")
input_box.bind('<Return>', callback)
input_box.grid(column=1, row=1)

Search_mode1 = Radiobutton(frm4, text="Presence", variable= ModeNo, value=1, command=print_int, width="15")
Search_mode1.grid(column=1, row=1)
#Search_mode1.bind("<Button-1>", check)
Search_mode2 = Radiobutton(frm4, text="Root", variable= ModeNo, value=2, command=print_int, width="15")
Search_mode2.grid(column=1, row=2)
#Search_mode2.bind("<Button-1>", check)
Search_mode3 = Radiobutton(frm4, text="Disable Suggestions", variable= ModeNo, value=3, command=print_int, width="15")
Search_mode3.grid(column=1, row=3)
print(ModeNo)

Button(frm3, text="Search", command = get_text).grid(column=1, row=2, pady=(0, 0))

#definition_text = Entry(frm, textvariable=engdefinition)
#definition_text.grid(column=2,row=3)
definition_text = Text(frm3, height=5, width=100, font=("DengXian", 13), background="#4B6478", fg="white", insertbackground="white") 
definition_text.grid(column=1, row=3, padx=(0, 20), pady=(20, 0))
DefScroll=Scrollbar(frm3, orient="vertical", command=definition_text.yview)
DefScroll.grid(row=3, column=2, sticky="ns")
definition_text.configure(yscrollcommand=DefScroll.set)
component_definition_text = Text(frm3, height= 15, width= 100, font = ("DengXian", 13), background="#4B6478", fg= "white", insertbackground="white")
component_definition_text.grid(column=1, row=4, padx=(0, 20), pady=(20, 20))
CompDefScroll=Scrollbar(frm3, orient="vertical", command=component_definition_text.yview)
CompDefScroll.grid(row=4, column=2, sticky="ns")
component_definition_text.configure(yscrollcommand=CompDefScroll.set)

#root.bind('<Return>', callback)
my_label = Label(frm2, text="Suggestions", font=("Helvetica", 14))
my_label.grid(column=1, row= 3)

my_list = Listbox(frm2, width=30, height= 10, font=("DengXian", 13), bg="#4B6478" ,fg="white")
#my_list.grid(column=1, row=4, padx=(20, 20), pady=(0, 20))

v=Scrollbar(frm2, orient="vertical", command=my_list.yview)
v.grid(row=4, column=2, sticky="ns")
my_list.configure(yscrollcommand=v.set)
my_list.grid(column=1, row=4, padx=(20, 0), pady=(0, 20))

SearchModeToggle = Button(frm4, command= toggle_search_mode, textvariable=btn_text)
SearchModeToggle.grid(column=2, row=4)

update(list_of_dicts_jsoned)

my_list.bind("<<ListboxSelect>>", fillout)

input_box.bind("<KeyRelease>", check)

input_box.bind("<ButtonRelease-3>", check)

input_box.bind("<Button-3>", paste_def) #Both being button binds I want them to be the same, so, both button or button release, but seems it can't work like that.

root.mainloop()

       
# TO DO. IF NO MATCHES ARE OBTAINED, CHECK FOR PARTS OF THE INPUTTED TEXT.
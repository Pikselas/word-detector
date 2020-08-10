# word detector and replacer 
import os
import tkinter as ui
def Search(WORD,REPLACE,extension):
    print("WORD ->> "+str(WORD)+"\nREPLACER ->> "+str(REPLACE)+"\nEXTENSION ->>"+str(extension))
    print("**********SUMMARY*************")
    contents = os.listdir("Input//")
    for items in contents:
        if items.endswith(extension):
            with open(("Input//"+items),'r') as file:
                text = file.read()
                if WORD in text:
                    print("FOUND in ->>"+str(items))
                    Remove(items,WORD,REPLACE)
                    print("STATUS: REPLACED")
                else:
                    return False
                file.close()
def Remove(Filename,OLD,NEW):
    File = open(("Input//"+Filename),'r')
    Contents = File.read()
    Contents = Contents.replace(OLD,NEW)
    File.close()
    File = open(("Output//"+Filename),'w')
    File.write(Contents)
    File.close()
def Window():
    window = ui.Tk()
    window.geometry("350x150")
    window.title("Detector")
    ui.Label(window,text = "Enter Word to be detected:").grid(row = "1",column = "0",sticky = "W")
    EntryWord = ui.Entry(window)#Entry detectable word
    EntryWord.grid(row = "1",column = "1")
    ui.Label(window,text = "Enter word to be replaced with:").grid(row = "2" , column = "0",sticky = "W")
    EntryReplace = ui.Entry(window)#replaceable word
    EntryReplace.grid(row = "2" , column = "1")
    ui.Label(window,text = "Extension:").grid(row = "3",column = "0")
    EntryExtension = ui.Entry(window)
    EntryExtension.grid(row = "3" , column = "1")
    ui.Button(window,text = "Scan",width = "10", height = "2",command = lambda: Search(EntryWord.get(),EntryReplace.get(),EntryExtension.get())).grid(row = "4" ,column = "1")
    window.mainloop()  
if __name__ == "__main__":
    try:
        Window()
    except FileExistsError:
        print("FILE NOT EXIST")
    except FileNotFoundError:
        print("FILE NOT FOUND")
    except Exception as e:
        print("SOMETHING WENT WRONG\nContact ARITRA and show bellow error")
        print(e)

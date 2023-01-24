from tkinter import*
root=Tk()
root.title("Sales Application")
root.geometry("400x400")


label_month=Label(root)
label_profits=Label(root)
label_max_profit=Label(root)
label_min_profit=Label(root)

month= ("January","Febuary","March","April","May","June","July","August","September","October","November","December")


profits=(20000,45000,78000,97000,12000,456000,65000,54000,10000,30000,70000,90000)

label_month["text"]="Months:"+str(month)
label_profits["text"]="profits:"+str(profits)
def maxprofit():
    
    max_profit=max(profits)
    max_profit_index=profits.index(max_profit)
    max_profit_month =month[max_profit_index]
    label_max_profit['text']="The maximum profit of "+ str(max_profit)+"was recorded in the month of"
    + str(max_profit_month)
    
def minprofit():
        
    min_profit=min(profits)
    min_profit_index=profits.index(min_profit)
    min_profit_month =month[min_profit_index]
    label_min_profit['text']="The minimum profit of "+ str(min_profit)+"was recorded in the month of"
    + str(min_profit_month)
    
label_month.place(relx=0.5, rely=0.2, anchor=CENTER)
label_profits.place(relx=0.5, rely=0.3, anchor=CENTER)

btn_max=Button(root,text="max profit",command=maxprofit)
btn_max.place(relx=0.5, rely=0.4, anchor=CENTER)
btn_min=Button(root,text="min profit",command=minprofit)
label_max_profit.place(relx=0.5, rely=0.5, anchor=CENTER)
btn_min.place(relx=0.5, rely=0.6, anchor=CENTER)
label_min_profit.place(relx=0.5, rely=0.7, anchor=CENTER)


root.mainloop()
    


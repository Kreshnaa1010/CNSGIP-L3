from tkinter import *
import requests
root = Tk() 
variable1 = StringVar(root) 
variable2 = StringVar(root) 


variable1.set("currency") 
variable2.set("currency") 


def RealTimeCurrencyConversion(): 
    
    from_currency = variable1.get() 
    to_currency = variable2.get() 
    amount = float(Amount1_field.get())

   
    api_key = "Your_Api_Key"
    
    
    base_url = r"https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE"

   
    main_url = f"{base_url}&from_currency={from_currency}&to_currency={to_currency}&apikey={api_key}"

    
    try:
        req_ob = requests.get(main_url)
        req_ob.raise_for_status()  
        result = req_ob.json() 

        
        if "Realtime Currency Exchange Rate" in result:
           
            Exchange_Rate = float(result["Realtime Currency Exchange Rate"]['5. Exchange Rate'])

            
            new_amount = round(amount * Exchange_Rate, 3)

            
            Amount2_field.insert(0, str(new_amount))
        else:
            Amount2_field.insert(0, "Error: Could not fetch rates.")
    except Exception as e:
        Amount2_field.insert(0, f"Error: {str(e)}")


def clear_all(): 
    Amount1_field.delete(0, END) 
    Amount2_field.delete(0, END) 


if __name__ == "__main__" : 
    
    root.configure(background='sky blue') 
    
    
    root.geometry("400x175") 
    
   
    headlabel = Label(root, text='Welcome to Real Time Currency Converter', fg='black', bg='sky blue') 

    
    label1 = Label(root, text="Amount :", fg='black', bg='sky blue') 
    
    
    label2 = Label(root, text="From Currency", fg='black', bg='sky blue') 
    
    
    label3 = Label(root, text="To Currency :", fg='black', bg='sky blue') 

   
    label4 = Label(root, text="Converted Amount :", fg='black', bg='sky blue') 

    headlabel.grid(row=0, column=1) 
    label1.grid(row=1, column=0) 
    label2.grid(row=2, column=0) 
    label3.grid(row=3, column=0) 
    label4.grid(row=5, column=0) 
    
   
    Amount1_field = Entry(root) 
    Amount2_field = Entry(root) 
    
    
    Amount1_field.grid(row=1, column=1, ipadx="25") 
    Amount2_field.grid(row=5, column=1, ipadx="25") 

   
    CurrencyCode_list = ["INR", "USD", "CAD", "CNY", "DKK", "EUR"] 

    
    FromCurrency_option = OptionMenu(root, variable1, *CurrencyCode_list) 
    ToCurrency_option = OptionMenu(root, variable2, *CurrencyCode_list) 
    
    FromCurrency_option.grid(row=2, column=1, ipadx=10) 
    ToCurrency_option.grid(row=3, column=1, ipadx=10) 
    
    
    button1 = Button(root, text="Convert", bg="red", fg="black", command=RealTimeCurrencyConversion) 
    button1.grid(row=4, column=1) 

    
    button2 = Button(root, text="Clear", bg="red", fg="black", command=clear_all) 
    button2.grid(row=6, column=1) 
    
   
    root.mainloop() 

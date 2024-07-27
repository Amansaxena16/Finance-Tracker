import pandas as pd
import csv
from datetime import datetime
from main import *

class CSV:
    date_format = '%d-%m-%Y'
    CSV_FILE = "financeData.csv"
    COLUMN = ['Date','Amount','Category','Description']
    
    @classmethod
    def initialize_csv(cls):
        try:
            pd.read_csv(cls.CSV_FILE)
        except FileNotFoundError:
            df = pd.DataFrame(columns = cls.COLUMN)
            df.to_csv(cls.CSV_FILE, index=False)
            
    @classmethod
    def add_Entry(cls, Date, Amount, Category, Description):
        new_entry = {
            'Date' : Date,
            'Amount' : Amount,
            'Category' : Category,
            'Description' : Description
        }
        
        with open(cls.CSV_FILE,"a",newline="") as csvfile:
            write = csv.DictWriter(csvfile, fieldnames=cls.COLUMN)
            write.writerow(new_entry)
        print("Entry Added Successfully")
        
    @classmethod
    def Get_transaction(cls, start_date, end_date):
        df = pd.read_csv(cls.CSV_FILE)
        df['Date'] = pd.to_datetime(df['Date'], format=CSV.date_format)
        start_date = datetime.strptime(start_date, CSV.date_format)
        end_date = datetime.strptime(end_date, CSV.date_format)
        
        mask = (df['Date'] >= start_date) & (df['Date'] <= end_date)
        filtered_df = df.loc[mask]
        
        if filtered_df.empty:
            print('No Transaction Found in the given date')
        else:
            print(f"Transaction from {start_date.strftime(CSV.date_format)} to {end_date.strftime(CSV.date_format)}")
            print(
                filtered_df.to_string(
                    index=False, formatters={"Date" : lambda x: x.strftime(CSV.date_format)}
                )
            )
            
            total_income = filtered_df[filtered_df['Category'] ==  'Income']['Amount'].sum()
            total_expense = filtered_df[filtered_df['Category'] == 'Expense']['Amount'].sum()
            print('\nSummary: ')
            print(f"Total Income ${total_income:.2f}")
            print(f"Total Expense ${total_expense:.2f}")
            print(f"Net Saving ${(total_income - total_expense):.2f}")
            
            return filtered_df
            
def add():
    CSV.initialize_csv
    date = get_date('Enter Your transaction date(dd-mm-yy) or Enter for todays date : ', allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_Entry(date,amount,category,description)
       
CSV.Get_transaction("01-07-2024","30-07-2024")  
# add()
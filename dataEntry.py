import pandas as pd
import csv
from datetime import datetime
from main import *

class CSV:
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
            
            
def add():
    CSV.initialize_csv
    date = get_date('Enter Your transaction date(dd-mm-yy) or Enter for todays date : ', allow_default=True)
    amount = get_amount()
    category = get_category()
    description = get_description()
    CSV.add_Entry(date,amount,category,description)
         
add()
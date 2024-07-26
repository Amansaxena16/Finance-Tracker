import pandas as pd
import csv
from datetime import datetime

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
            
            
CSV.initialize_csv()
CSV.add_Entry('16-11-2000',100000,'Income','Born Date')
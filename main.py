from datetime import datetime
date_format = '%d-%m-%Y'
CATEGORIES = {
    'I' : 'Income',
    'E' : 'Expense'
}

def get_date(prompt, allow_default = False):
    date_string = input(prompt)
    if allow_default and not date_string:
        return datetime.today().strftime(date_format)
    
    try:
        valid_date = datetime.strptime(date_string,date_format)
        return valid_date.strftime(date_format)
    except ValueError:
        print('Invalid Date!! It should be dd-mm-yy format')
        get_date(prompt, allow_default)
        

def get_amount():
    try:
        amount = float(input('Enter you Amount : '))
        if amount <= 0:
            raise ValueError('Amount should be non-zero and non-negative')
        return amount
    except ValueError as e:
        print(e)
        return get_amount()

def get_category():
    category = input("Enter Category : 'I' for Income and 'E' for Expense : ")
    if category in CATEGORIES:
        return category
    else:
        print("Invalid Category!! Enter 'I' for Income and 'E' for Expense : ")
        return get_category()

def get_description():
    return input('Enter your Description : ')
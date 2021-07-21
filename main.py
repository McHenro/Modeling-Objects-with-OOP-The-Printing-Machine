
from data import data
class PrintingMachine:
    
    def __init__(self):
        #   FORMAT variables  from data.py
        self.ink_coloured = data.FORMAT['coloured']['materials']['ink']
        self.paper_coloured = data.FORMAT['coloured']['materials']['paper']
        self.price_coloured = data.FORMAT['coloured']['price']
        self.ink_greyscale =  data.FORMAT['greyscale']['materials']['ink']
        self.paper_greyscale = data.FORMAT['greyscale']['materials']['paper']
        self.price_greyscale = data.FORMAT['greyscale']['price']
        # resources variables from data.py
        self.initial_ink = data.resources['ink']
        self.initial_paper = data.resources['paper'] 
        self.initial_profit = data.resources['profit'] 
        # currency variables
        self.money_for_print = 0
        self.Biyar = 5
        self.Faiba = 10
        self.Muri= 20
        self.Wazobia = 50
        # used variables
        self.num_of_pages = 0
        self.your_price  = 0
        self.total_currency  = 0
        self.num_of_Biyar = 0
        self.Biyar = 0
        self.num_of_Faiba = 0
        self.Faiba = 0
        self.final_profit = 0
        self.initial_profit  = 0
        self.money_for_print = 0
        self.resources_ink = 0
        self.amt_ink_used = 0
        self.amt_ink_used = 0
        self.resourse_paper = 0
        self.format  = ""
        self.to_continue = ""
        self.ink_consumed = 0
        self.paper_consumed = 0
        self.print_report = 0
        
    #Checking  if resources are enough to print colored pages
    def check_resources_colored(self):
        self.num_of_pages = int(input("Enter number of pages to print\n\n"))
        self.ink_consumed = self.ink_coloured * self.num_of_pages
        self.paper_consumed = self.num_of_pages
        if self.initial_paper > self.paper_consumed and self.initial_ink > self.ink_consumed:
            print("You have enough resources\n")
            self.your_price = self.num_of_pages *   self.price_coloured 
            print(f"Your price is #{self.your_price}\n")
            
        else:
            print("Sorry you do not have enough resources for this demand!\n")
            self.to_continue  =input("If you want to continue type 'yes' or 'no'\n")
            if  self.to_continue == 'no':
                exit()
            elif self.to_continue  == 'yes':
                self.main_func()
 #Checking  if resources are enough to print greyscale pages
    def check_resources_greyscale(self):
        self.num_of_pages = int(input("Enter number of pages to print\n"))
        self.ink_consumed = self.ink_greyscale * self.num_of_pages
        self.paper_consumed = self.num_of_pages
        if self.initial_paper > self.paper_consumed and self.initial_ink > self.ink_consumed:
            print("You have enough resources for this Demand!\n\n")
            self.your_price = self.num_of_pages *  self.ink_greyscale
            print(f"Your price is #{self.your_price}")
            
        else:
            print("Sorry you do not have enough resources for this Demand!\n")
            self.to_continue  =input("If you want to continue type 'yes' or 'no'\n")
            if  self.to_continue == 'no':
                exit()
            elif self.to_continue  == 'yes':
                self.main_func()    
        
    #checking total currency(i.e nos. of Biyar,Faiba,Muri and Wazobia) imputted by the user.
    def process_price(self):
        self.num_of_Biyar = int(input('Enter number of Biyar\n'))
        total_Biyar = self.num_of_Biyar * self.Biyar
        self.num_of_Faiba = int(input('Enter number of Faiba\n'))
        total_Faiba = self.num_of_Faiba * self.Faiba
        num_of_Muri = int(input('Enter number of Muri\n'))
        total_Muri= num_of_Muri * self.Muri
        self.num_of_Wazobia= int(input('Enter number of Wazobia\n'))
        total_Wazobia= self.num_of_Wazobia * self.Wazobia
        self.total_currency = total_Biyar + total_Faiba + total_Muri + total_Wazobia
        print(f"You've just imputted #{self.total_currency}\n")
    #checking wether there is change in Naira for the user or not.
    def check_transaction(self):
        if  self.total_currency < self.your_price:
            print("Sorry not enough money. Money refunded.\n")
            self.to_continue=input("Type 'yes' or 'no' to try again\n")
            if  self.to_continue== 'no':
                exit()
            elif self.to_continue == 'yes':
                self.main_func()       
        elif self.total_currency > self.your_price:
            naira_in_change = self.total_currency - self.your_price
            print(f'and here is #{naira_in_change} Naira in change\n')
        
    #generating report for the user for colored operation or shutting down the machine.
    def  coloured_report(self):
        self.initial_profit += self.your_price
        self.ink_consumed = self.ink_coloured * self.num_of_pages
        self.initial_ink -= self.ink_consumed
        self.initial_paper -= self.num_of_pages
        print(f'''
              Your current resource values are:
              ---------------------------------
              paper:{self.initial_paper}pc, ink:{self.initial_ink}ml, profit:#{self.initial_profit}.
              ---------------------------------
              Here is your Project and Thank you for using our services.
              ''')
        self.to_continue  =input("If you want to continue type 'yes' or 'no'\n")
        if  self.to_continue  == 'no':
            exit()
        elif self.to_continue  == 'yes':
            self.main_func()  
        
     #generating report for the user for greyscale operation or shutting down the machine.
    def  greyscale_report(self):
        self.initial_profit += self.your_price
        self.ink_consumed = self.ink_greyscale * self.num_of_pages
        self.initial_ink -= self.ink_consumed
        self.initial_paper -= self.num_of_pages
        print(f'''
              Your current resource values are:
              ---------------------------------
              paper:{self.initial_paper}pc, ink:{self.initial_ink}ml, profit:#{self.initial_profit}.
              ---------------------------------
              Here is your Project and Thank you for using our services.
              ''')
        
        
        self.to_continue  =input("If you want to continue type 'yes' or 'no'\n")
        if  self.to_continue  == 'no':
            exit()
        elif self.to_continue  == 'yes':
            self.main_func()  
    # checking for format, whether colored or greyscale.            
    def format_type(self):
        self.format = input("What format would you want?\nType in 'colored' or 'greyscale'\n\n")
        while not (self.format == "colored" or self.format == "greyscale" ):
            print("please enter the correct keyword by typing 'colored' or 'greyscale' ")
            return self.format_type()
    
    # The mother function that calls every other methods or funtions     
    def main_func(self): 
        print(
'''

        WELCOME TO HENRY.TECH AUTOMATED PRINTING MACHINE
        --------oo-----------oo------------oo------------
         
''')   
        self.format_type()     
        if self.format == "colored":
            self.check_resources_colored()
            self.process_price()
            self.check_transaction()
            self.print_report = input("Do you want to print report or off machine? type 'report' or 'off\n\n")
            if self.print_report == 'off':
                exit()
                
            else:
                if self.print_report == 'report':
                    self.coloured_report()
                    
        elif self.format == "greyscale":
            self.check_resources_greyscale()
            self.process_price()
            self.check_transaction()
            self.print_report = input("Do you want to print report or off machine? type 'report' or 'off\n\n")
            if self.print_report == 'off':
                exit()
                
            else:
                if self.print_report == 'report':
                    self.greyscale_report()
                 
printer = PrintingMachine()
printer.main_func()

 
        
        
        
        
        
        
        
        
        
        
        
   

    



        
        


    
                    
        
            
            
        
    
    

    


    
        
    
    
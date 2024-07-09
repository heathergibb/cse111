import numpy_financial as np

def main():
    try:
        # Request a house price and loop until the value is a valid positive integer
        is_entry_valid = False

        while is_entry_valid == False:
            price = input("Enter house price: ")

            if is_positive_int(price):
                price = int(price)
                is_entry_valid = True
            else:
                print("Invalid response. Please enter a positive integer.")
             
        # Request down payment and loop until the value is a valid positive interger  
        # Also validate that the down payment is less than the house price
        is_entry_valid = False
        
        while is_entry_valid == False:
            down_pmt = input("Enter down payment: ")
            
            if is_positive_int(down_pmt):
                down_pmt = int(down_pmt)
                
                if down_pmt < price:
                    is_entry_valid = True
                else:
                    print("Invalid response. The down payment must be less than the house price.")
            else:
                print("Invalid response. Please enter a positive integer.")
       

        # Display down payment % value
        down_pmt_percent = calc_down_pmt_percent(price, down_pmt)
        print(f"Down Payment: {down_pmt_percent:.1f}%")
        # Request interest rate and loop until the value is a positive float between 0 and 100
        is_entry_valid = False
        
        while is_entry_valid == False:
            interest_rate = input("Enter interest rate as %: ")

            if is_positive_percent(interest_rate):
                interest_rate = float(interest_rate) / 100
                is_entry_valid = True
            else:
                print("Invalid response. Please enter a % between 0 and 100")

        # Request amortization in years and loop until the value is a positive integer
        is_entry_valid = False

        while is_entry_valid == False:
            amort_term = input("Enter amortization period (in years): ")
            
            if is_positive_int(amort_term):
                amort_term = int(amort_term)
                #amort_term_months = amort_term * 12
                is_entry_valid = True
            else:
                print("Invalid response. Please enter a positive integer.")
        
        # Select payment frequency
        pmt_frequency = None         
        while pmt_frequency not in (1,2,3):

            pmt_frequency = int(input("Select a payment frequency (1 - Monthly, 2 - Bi-weekly, or 3 - Weekly): "))

            if pmt_frequency not in (1,2,3):
                print("Invalid entry. Please try again.")
            else:
                match pmt_frequency:
                    case 1:
                        pmt_freq_desc = "Monthly"
                    case 2:
                        pmt_freq_desc = "Bi-Weekly"
                    case 3:
                        pmt_freq_desc = "Weekly"
        
        loan_amt = price - down_pmt
        loan_pmt = calc_payment(loan_amt, interest_rate, amort_term, pmt_frequency)
        
        print()
        print(f"{pmt_freq_desc} Payment = ${loan_pmt:.2f}")
        
    except ValueError as val_err:
        print(f"Error: {val_err}")
        print("You made an invalid entry. Please rerun the program and try again.")
    except ZeroDivisionError as zero_err:
        print(f"Error: {zero_err}")
        print("Term cannot be 0. Please rerun the program and try again.")


def calc_payment(principal, int_rate, years, frequency=1):
    """Parameters: 
        principal = loan amount (must be positive)
        int_rate = APR as a decimal ex 5% = 0.05 (must be > 0 and < 1)
        years = amortization term in years (must be > 0)
        payment frequency (default = 1)
            1: monthly
            2: bi-weekly
            3: weekly
    """

    match frequency:
        case 1: # monthly
            term = years * 12
            rate = int_rate / 12
        case 2: # bi-weekly
            term = years * 26
            rate = int_rate / 26
        case 3: # weekly
            term = years * 52
            rate = int_rate / 52
        case _:
            return False

    pmt = round(np.pmt(rate, term, 0 - principal), frequency)
  
    return pmt 
   
def is_positive_int(entry):
    """Returns True if the parameter is an interger and greater than 0"""
    
    try:
        # if float(entry) does not have decimals
        if float(entry) % 1 == 0:
            entry = int(entry)
            return entry > 0
        else:
            return False
    
    except ValueError:
        return False
    
def is_positive_percent(entry):
    """Returns True if the parameter is a float between 0 and 100"""
    try:
        entry = float(entry)
        return entry > 0 and entry < 100

    except ValueError:
        return False
    
def calc_down_pmt_percent(price, down_pmt):
    """Parameters:
        price = house price (cannot be 0)
        down_pmt = down payment (must be < price and > 0)
        
        returns percentage amount as an float with 1 decimal"""
    
    percent = round((down_pmt / price) * 100, 1)
    return percent


if __name__ == "__main__":
    main()
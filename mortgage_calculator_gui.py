"""This program creates a gui that will take parameters for up to 3 mortage scenarios and
calculate the payment details."""

from tkinter import ttk
from tkinter import *
import tkinter as tk
import numpy_financial as np

root = tk.Tk()

def main():
    root.title("Mortgage Comparision Calculator")
    root.geometry("600x350")

    # Add widgets

    # Create scenario titles
    lbl_title_1 = ttk.Label(root,
        text="Scenario 1",
        font=("Helvetica 12 italic"))
    lbl_title_1.grid(row=0, column=1, padx=0, pady=(10,5))
    lbl_title_2 = ttk.Label(root,
        text="Scenario 2",
        font=("Helvetica 12 italic"))
    lbl_title_2.grid(row=0, column=2, padx=0, pady=(10,5))
    lbl_title_3 = ttk.Label(root,
        text="Scenario 3",
        font=("Helvetica 12 italic"))
    lbl_title_3.grid(row=0, column=3, padx=0, pady=(10,5))

    # Create labels
    # Create house price label
    lbl_price = ttk.Label(root,
        text="House Price:",
        font=("Helvetica, 14"),
        justify="left")
    lbl_price.grid(row=1, column=0, padx=10, pady=5, sticky=E)
    
    # Create down payment label
    lbl_down_pmt = ttk.Label(root, 
        text="Down Payment:",
        font=("Helvetica, 14"))
    lbl_down_pmt.grid(row=2, column=0, padx=10, pady=5, sticky=E)

    # Create interest rate label
    lbl_int_rate = ttk.Label(root, 
        text="Interest Rate %:",
        font=("Helvetica, 14"))
    lbl_int_rate.grid(row=3, column=0, padx=10, pady=5, sticky=E)

    # Create Amortization label
    lbl_amort = ttk.Label(root, 
        text="Amortization (yrs):",
        font=("Helvetica, 14"))
    lbl_amort.grid(row=4, column=0, padx=10, pady=5, sticky=E)
    
    # Create payment frequency label
    lbl_pmt_freq = ttk.Label(root, 
        text="Payment Frequency:",
        font=("Helvetica, 14"))
    lbl_pmt_freq.grid(row=5, column=0, padx=10, pady=5, sticky=E)

    # Create payment amount label
    lbl_pmt_amt = ttk.Label(root,
        text="Payment Amount:",
        font=("Helvetica, 14"))
    lbl_pmt_amt.grid(row=7, column=0, padx=10, pady=5, sticky=E)


    # Create Scenario 1 widgets
    ent_price_1 = ttk.Entry(root, 
        width=10,
        font=("Helvetica, 14"),
        validate="key",
        validatecommand=(root.register(validate_entry), "%S"))
    ent_price_1.grid(row=1, column=1, padx=3, pady=5, sticky=W)

    ent_down_pmt_1 = ttk.Entry(root,
        width=10,
        font=("Helvetica, 14"),
        validate="key",
        validatecommand=(root.register(validate_entry), "%S"))
    ent_down_pmt_1.grid(row=2, column=1, padx=3, pady=5, sticky=W)

    ent_int_rate_1 = ttk.Entry(root,
        width=10,
        font=("Helvetica, 14"),
        validate="key",
        validatecommand=(root.register(validate_interest_entry), "%S", "%d"))
    ent_int_rate_1.grid(row=3, column=1, padx=3, pady=5, sticky=W)

    ent_amortization_1 = ttk.Entry(root,
        width=10,
        font=("Helvetica, 14"),
        validate="key",
        validatecommand=(root.register(validate_entry), "%S"))
    ent_amortization_1.grid(row=4, column=1, padx=3, pady=5, sticky=W)

    n = tk.StringVar()
    keep_value = n.get() # this is to fix a bug that makes the combo box lose it's default if not used right away
    cbo_pmt_choice_1 = ttk.Combobox(root, 
        width=8, 
        font=("Helvetica, 14"),
        textvariable = keep_value,
        state="readonly")
    cbo_pmt_choice_1["values"] = ("Monthly", "Bi-Weekly", "Weekly")
    cbo_pmt_choice_1.grid(row=5, column=1, padx=3, pady=5)
    cbo_pmt_choice_1.current(0)
    
    btn_calc_1 = tk.Button(root,
        text="Calculate",
        width=10, 
        height = 1,
        font = ("Helvetica, 14"),
        command=lambda: calc_mortgage_payment(ent_price_1.get(), ent_down_pmt_1.get(), ent_int_rate_1.get(), ent_amortization_1.get(), cbo_pmt_choice_1.get(), lbl_payment_1))
    btn_calc_1.grid(row=6, column=1, padx=3, pady=5, sticky=W)

    lbl_payment_1 = ttk.Label(root, 
        text = "",
        font=("Helvetica, 10"))
    lbl_payment_1.grid(row=7, column=1, padx=3, pady=5, sticky=SW)

    # Create Scenario 2 widgets

    ent_price_2 = ttk.Entry(root, 
        width=10,
        font=("Helvetica, 14"),
        validate="key",
        validatecommand=(root.register(validate_entry), "%S"))
    ent_price_2.grid(row=1, column=2, padx=3, pady=5, sticky=W)

    ent_down_pmt_2 = ttk.Entry(root,
        width=10,
        font=("Helvetica, 14"),
        validate="key",
        validatecommand=(root.register(validate_entry), "%S"))
    ent_down_pmt_2.grid(row=2, column=2, padx=3, pady=5, sticky=W)
    
    ent_int_rate_2 = ttk.Entry(root,
        width=10,
        font=("Helvetica, 14"),
        validate="key",
        validatecommand=(root.register(validate_interest_entry), "%S", "%d"))
    ent_int_rate_2.grid(row=3, column=2, padx=3, pady=5, sticky=W)

    ent_amortization_2 = ttk.Entry(root,
        width=10,
        font=("Helvetica, 14"),
        validate="key",
        validatecommand=(root.register(validate_entry), "%S"))
    ent_amortization_2.grid(row=4, column=2, padx=3, pady=5, sticky=W)

    n = tk.StringVar()
    keep_value = n.get() # this is to fix a bug that makes the combo box lose it's default if not used right away
    cbo_pmt_choice_2 = ttk.Combobox(root, 
        width=8, 
        font=("Helvetica, 14"),
        textvariable = keep_value,
        state="readonly")
    cbo_pmt_choice_2["values"] = ("Monthly", "Bi-Weekly", "Weekly")
    cbo_pmt_choice_2.grid(row=5, column=2, padx=3, pady=5)
    cbo_pmt_choice_2.current(0)

    btn_calc_2 = tk.Button(root,
        text="Calculate",
        width=10, 
        height = 1,
        font = ("Helvetica, 14"),
        command=lambda: calc_mortgage_payment(ent_price_2.get(), ent_down_pmt_2.get(), ent_int_rate_2.get(), ent_amortization_2.get(), cbo_pmt_choice_2.get(), lbl_payment_2))
    btn_calc_2.grid(row=6, column=2, padx=3, pady=5, sticky=W)

    lbl_payment_2 = ttk.Label(root, 
        text = "",
        font=("Helvetica, 10"))
    lbl_payment_2.grid(row=7, column=2, padx=3, pady=5, sticky=SW)

    # Create Scenario 3 widgets
    ent_price_3 = ttk.Entry(root, 
        width=10,
        font=("Helvetica, 14"),
        validate="key",
        validatecommand=(root.register(validate_entry), "%S"))
    ent_price_3.grid(row=1, column=3, padx=3, pady=5, sticky=W)

    ent_down_pmt_3 = ttk.Entry(root,
        width=10,
        font=("Helvetica, 14"),
        validate="key",
        validatecommand=(root.register(validate_entry), "%S"))
    ent_down_pmt_3.grid(row=2, column=3, padx=3, pady=5, sticky=W)

    ent_int_rate_3 = ttk.Entry(root,
        width=10,
        font=("Helvetica, 14"),
        validate="key",
        validatecommand=(root.register(validate_interest_entry), "%S", "%d"))
    ent_int_rate_3.grid(row=3, column=3, padx=3, pady=5, sticky=W)

    ent_amortization_3 = ttk.Entry(root,
        width=10,
        font=("Helvetica, 14"),
        validate="key",
        validatecommand=(root.register(validate_entry), "%S"))
    ent_amortization_3.grid(row=4, column=3, padx=3, pady=5, sticky=W)

    n = tk.StringVar()
    keep_value = n.get() # this is to fix a bug that makes the combo box lose it's default if not used right away
    cbo_pmt_choice_3 = ttk.Combobox(root, 
        width=8, 
        font=("Helvetica, 14"),
        textvariable = keep_value,
        state="readonly")
    cbo_pmt_choice_3["values"] = ("Monthly", "Bi-Weekly", "Weekly")
    cbo_pmt_choice_3.grid(row=5, column=3, padx=3, pady=5)
    cbo_pmt_choice_3.current(0)

    btn_calc_3 = tk.Button(root,
        text="Calculate",
        width=10, 
        height = 1,
        font = ("Helvetica, 14"),
        command=lambda: calc_mortgage_payment(ent_price_3.get(), ent_down_pmt_3.get(), ent_int_rate_3.get(), ent_amortization_3.get(), cbo_pmt_choice_3.get(), lbl_payment_3))
    btn_calc_3.grid(row=6, column=3, padx=3, pady=5, sticky=SW)

    lbl_payment_3 = ttk.Label(root, 
        text = "",
        font=("Helvetica, 10"))
    lbl_payment_3.grid(row=7, column=3, padx=3, pady=5, sticky=W)

    # Run the app's main loop
    root.mainloop()

def validate_entry(text):
    return text.isdecimal()

def validate_interest_entry(text, action):
    """Parameters: text = keystroke entered
        action = 1 if insert, 0 if delete, -1 anything else
        
        Returns True if the parameter is a float
        Returns True it the action was delete"""
    try:
        if action != '0':
            # get current value of textbox
            prev_value = root.focus_get().get()
            if prev_value != '':
                entry = float(prev_value + text) # this is to test that it is a float, if not ValueError will be called
                return True
            else:
                entry = float(text)
                return True
        else:
            return True

    except ValueError:
        return False 

def calc_mortgage_payment(price, down_pmt, int_rate, amort, frequency, output_label):
    """Parameters: price = house price
        down_pmt = down payment
        int_rate = interest rate as a percent
        amort = # of years of amortization
        frequency = payment frequency string ("Monthly", "Bi-Weekly", or "Weekly")
        output_label = the label where the output will be shown
        
        Sets the output label to the payment amount/frequency"""
    try:
        
        # if any of these parameters are empty, ValueError will be called and the calculations will not happen
        price = int(price)
        down_pmt = int(down_pmt)
        int_rate = float(int_rate) / 100
        amort = int(amort)

        if price != "" and down_pmt != "" and int_rate != "" and amort != "" and frequency != "":
            match frequency:
                case "Monthly":
                    frequency_num = 1
                    term = amort * 12
                    rate = int_rate / 12
                case "Bi-Weekly":
                    frequency_num = 2
                    term = amort * 26
                    rate = int_rate / 26
                case "Weekly":
                    frequency_num = 3
                    term = amort * 52
                    rate = int_rate / 52
                case _:
                    return False

            principal = price - down_pmt            
            mort_payment = round(np.pmt(rate, term, 0 - principal), frequency_num)

            if mort_payment <= 0:
                output_label.config(text = "Error. Try again.")
            else:
                output_label.config(text = f"${mort_payment:.2f}/{frequency}")

    except ValueError:
        output_label.config(text="")
        return False
    except ZeroDivisionError:
        output_label.config(text="")
        return False

if __name__ == "__main__":
    main()
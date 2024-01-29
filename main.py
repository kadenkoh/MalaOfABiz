import overheads, profit_loss , cash_on_hand

def main():
    """
    - This function organises the overhead, cash on hand, and profit loss functions into a modular structure. 
    When the main function is executed, it triggers all these functions to run sequentially. 
    Each function performs its respective calculations and writes the results into the summary text file.

    - No parameter needed 
    """
    # initialised all the functions from their respective codes
    overheads.overheads_function()
    cash_on_hand.cash_on_hand_function()
    profit_loss.profit_loss_function()

# run the main function
main()


import sys
from order_processor import process_order


def call_main():
    """
    ***********************************************
    * This is the driver code. Don't change it!!!
    * *********************************************

    Format of 'sys.argv': [`<SCRIPT_NAME>`, `<CUSTOMER_TYPE> <CATEGORY:PRICE:QTY> ..`]
    Example: python gt_main_wrapper.py "Member Electronics:100:1 Books:20:1"

    The code evaluator will execute this code by using the command:
    python gt_main_wrapper.py "Member Electronics:100:1 Books:20:1"
    """
    if len(sys.argv) < 2:
        raise ValueError("No command line arguments passed")

    process_order(sys.argv[1])


if __name__ == "__main__":
    call_main()

import requests # type: ignore
from prettytable import PrettyTable # type: ignore

# Alpha Vantage API details
API_KEY = " K10F9CMDL1EHF76W"  # Replace with your API key
API_URL = "https://www.alphavantage.co/query"

# Initialize portfolio
portfolio = {}

def add_stock(symbol, quantity, purchase_price):
    """Add stock to portfolio."""
    symbol = symbol.upper()
    portfolio[symbol] = {
        'quantity': quantity,
        'purchase_price': purchase_price
    }
    print(f"Added {quantity} shares of {symbol} at ${purchase_price:.2f} each.")

def remove_stock(symbol):
    """Remove stock from portfolio."""
    symbol = symbol.upper()
    if symbol in portfolio:
        del portfolio[symbol]
        print(f"Removed {symbol} from portfolio.")
    else:
        print(f"Stock {symbol} not found in portfolio.")

def fetch_stock_price(symbol):
    """Fetch real-time stock price."""
    params = {
        "function": "GLOBAL_QUOTE",
        "symbol": symbol.upper(),
        "apikey": API_KEY
    }
    response = requests.get(API_URL, params=params)
    data = response.json()
    try:
        price = float(data["Global Quote"]["05. price"])
        return price
    except (KeyError, TypeError):
        print(f"Error fetching data for {symbol}. Check the symbol or API limit.")
        return None

def display_portfolio():
    """Display portfolio details."""
    if not portfolio:
        print("Portfolio is empty.")
        return

    table = PrettyTable(["Symbol", "Quantity", "Purchase Price", "Current Price", "Total Value", "Profit/Loss"])
    total_value = 0

    for symbol, details in portfolio.items():
        quantity = details['quantity']
        purchase_price = details['purchase_price']
        current_price = fetch_stock_price(symbol)

        if current_price is None:
            continue

        total_stock_value = current_price * quantity
        profit_loss = total_stock_value - (purchase_price * quantity)
        total_value += total_stock_value

        table.add_row([symbol, quantity, purchase_price, current_price, total_stock_value, profit_loss])

    print(table)
    print(f"Total Portfolio Value: ${total_value:.2f}")

def main():
    """Main menu for user interaction."""
    while True:
        print("\nStock Portfolio Tracker")
        print("1. Add Stock")
        print("2. Remove Stock")
        print("3. View Portfolio")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            symbol = input("Enter stock symbol: ").upper()
            quantity = int(input("Enter quantity: "))
            purchase_price = float(input("Enter purchase price: "))
            add_stock(symbol, quantity, purchase_price)
        elif choice == "2":
            symbol = input("Enter stock symbol to remove: ").upper()
            remove_stock(symbol)
        elif choice == "3":
            display_portfolio()
        elif choice == "4":
            print("Exiting Stock Portfolio Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()





# K10F9CMDL1EHF76W --------API KEY for Alpha Vantage

#enter ur symbol(AAPL,MSFT)

#to run this program
#pip install requests prettytable

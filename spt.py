import tkinter as tk
from tkinter import messagebox

class StockPortfolioTracker:
    def __init__(self, master):
        self.master = master
        self.master.title("Stock Portfolio Tracker")

        self.portfolio = {}  # Dictionary to store stock holdings (symbol: quantity)
        self.create_widgets()

    def create_widgets(self):
        self.instruction_label = tk.Label(self.master, text="Enter stock symbol and quantity:")
        self.instruction_label.pack()

        self.symbol_label = tk.Label(self.master, text="Symbol:")
        self.symbol_label.pack()

        self.symbol_entry = tk.Entry(self.master)
        self.symbol_entry.pack()

        self.quantity_label = tk.Label(self.master, text="Quantity:")
        self.quantity_label.pack()

        self.quantity_entry = tk.Entry(self.master)
        self.quantity_entry.pack()

        self.add_button = tk.Button(self.master, text="Add to Portfolio", command=self.add_stock)
        self.add_button.pack()

        self.view_button = tk.Button(self.master, text="View Portfolio", command=self.view_portfolio)
        self.view_button.pack()

    def add_stock(self):
        symbol = self.symbol_entry.get().upper()
        quantity = self.quantity_entry.get()

        if not symbol or not quantity.isdigit():
            messagebox.showerror("Invalid Input", "Please enter valid stock symbol and quantity.")
            return

        self.portfolio[symbol] = int(quantity)
        messagebox.showinfo("Success", f"{symbol} added to portfolio!")

        # Clear input fields
        self.symbol_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)

    def view_portfolio(self):
        if not self.portfolio:
            messagebox.showinfo("Portfolio Empty", "Your portfolio is empty.")
        else:
            portfolio_text = "\n".join(f"{symbol}: {quantity}" for symbol, quantity in self.portfolio.items())
            messagebox.showinfo("Portfolio", f"Your portfolio:\n{portfolio_text}")

if __name__ == "__main__":
    root = tk.Tk()
    stock_tracker = StockPortfolioTracker(root)
    root.mainloop()

# shop-calculator# Shop Calculator

A beginner Python program that works like a small kiosk till.
It asks how many items you want, adds up the prices, applies a
discount on big orders, adds tax, and prints the date and time.

## Features
- Menu of items with prices (mandazi, tea, bread)
- Handles unknown items ("Sorry, we don't sell that")
- 10% discount when the total is over 100
- 16% tax added to the final total
- Date and time stamp on the receipt

## How to run
1. Install Python 3
2. Run: `python shop.py`
3. Enter how many items, then the name of each item

## Example
How many items? 3
bread, bread, tea -> Total: 135.0, With tax: 156.6

## What I learned
Variables, input, if/elif/else, loops, dictionaries, functions, and the datetime module.

## Next steps

Saves every receipt to receipts.txt with date and time, Counts quantities (bread x2), and Input validation for the item count.
Adds payment and calculates customer's change.

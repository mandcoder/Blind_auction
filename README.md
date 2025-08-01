# 🏆 Blind Auction – Python Project

## 📖 Description
This project is a simple **blind auction program** written in Python.  
It allows multiple participants to place bids without seeing each other’s offers.  
When all bids are in, the program announces the winner with the highest bid.

---

## 🎯 Features
✅ Accepts names and bids from multiple participants.  
✅ Stores all bids in a **dictionary**.  
✅ Clears the screen between bidders so previous bids remain hidden.  
✅ Automatically determines the highest bidder and prints the result.  
✅ **Robust input validation** – only accepts `y/n` answers and whole number bids.

---

## 🛠 How It Works
1️⃣ The program welcomes the user.  
2️⃣ Each bidder enters their **name** and **bid**.  
3️⃣ The program asks if there are more bidders:  
   - If you type `y` → the screen clears and the next bidder enters.  
   - If you type `n` → the auction ends.  
4️⃣ When all bids are in, the function `get_auction_winner()` calculates who placed the highest bid.  
5️⃣ The winner’s name and bid are displayed.

---

## ✅ Input Validation
This program includes **robust input validation** to make the auction process foolproof:

### 🔹 `get_yes_or_no(prompt)`
- Ensures the user can **only** type `y` or `n`.
- If the input is invalid (e.g. `yes`, `maybe`, `Y`), the program shows an error message and asks again.

### 🔹 `get_valid_bid(prompt)`
- Ensures the bid is a **whole number**.
- If the user types text or a decimal (e.g. `hundred` or `100.50`), the program displays:

```
❌ Please enter whole numbers only (no decimals).
```

---

## 💡 Tech Highlights
This project demonstrates several **core Python skills**:

- ✅ **Functions** – program logic is cleanly separated into functions (`get_yes_or_no`, `get_valid_bid`, `get_auction_winner`, `clear_screen`).  
- ✅ **Loops** – uses both `while` and `for` loops for input collection and processing.  
- ✅ **Dictionaries** – stores all bids in a key:value structure for easy lookup.  
- ✅ **Input validation** – prevents crashes and forces correct input for smoother user experience.  
- ✅ **Clean code** – structured and beginner-friendly, ideal for showcasing Python basics.

---

## 🚀 How to Run
1. Clone the repository:  
   ```bash
   git clone https://github.com/your-username/blind-auction.git
   ```
2. Navigate to the project folder and run the script:  
   ```bash
   python blind_auction.py
   ```
3. Follow the instructions in the terminal.

---

## 📜 License
This project is open source and available under the [MIT License](LICENSE).

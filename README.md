# 🎲 Guess the Number Game (Flask + JavaScript)

A simple **Guess the Number** web game built with **Flask (Python)** for the backend and **HTML, CSS, JavaScript** for the frontend.  
The game randomly picks a number between **1 and 100**, and you have **10 attempts** to guess it correctly!

---

## 🚀 Features
- 🎯 Random number between 1–100
- ⏳ Maximum **10 attempts** before "Game Over"
- ✅ Feedback messages: *Too Low*, *Too High*, *Correct!*
- 📊 Progress bar showing attempt usage
- 🔄 Restart button after win or game over
- 🎨 Styled with clean, responsive CSS

---

## ⚡ Installation & Setup

### 1️⃣ Clone the repo
```bash
git clone https://github.com/your-username/guess-number-game.git
cd guess-number-game
```
### 2️⃣ Create virtual environment (recommended)
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
### 4️⃣ Set environment variables 
```bash
Create a .env file in the project root:
SECRET_KEY=my-super-secret-key
```
### 5️⃣ Run the app
```bash
python app.py
```
App will start at 👉 http://127.0.0.1:5000

### 🛠️ Tech Stack
<ul>
<li>Python 3.x</li>
<li>Flask</li>
<li>Flask-CORS</li>
<li>HTML5, CSS3, JavaScript</li>
</ul>

### 📜 License
This project is open source and available under the MIT License.

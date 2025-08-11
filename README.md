# 🖱️ AntiAFK
**Anti-AFK** – Keeps you “active” so your green dot never takes a coffee break.  
Perfect for corporate warriors, remote ninjas, and anyone whose status must scream “I’m here!” even when you’re making coffee.

```
      (o_o)    Corporate Ninja Mode: ON
     <)   )╯   Your green dot shall not fade.
     /   >     Now... go get that coffee.
```

---

## 🚀 How to Use

### 1️⃣ Clone the repo
```bash
git clone https://github.com/chinmaykrishnroy/AntiAFK.git
cd AntiAFK
```

### 2️⃣ Run the setup
Just double-click **`install.bat`** — it’s your one-stop shop:  
- Creates a virtual environment  
- Installs all the dependencies from `requirements.txt`  
- Launches the app so your mouse wiggles while you’re “working”  

You’ll see a **black square with a red circle** in your system tray — that’s AntiAFK.  
You can close the terminal after it starts; the tray icon means it’s running.

---

### 3️⃣ Create a shortcut
Double-click **`createshortcut.bat`** — this drops a handy shortcut right in your project folder.  
Now you can start AntiAFK without touching the terminal ever again.

---

### ⚡ Optional: Make it run at startup
1. Press **`Win + R`**  
2. Type:
   ```
   shell:startup
   ```
3. Paste your AntiAFK shortcut into that folder.  
Boom — it runs automatically whenever your PC starts. Your green dot will never sleep again.

---

## 🎛️ Tuning AntiAFK (for power users)

Open **`main.py`** and look at the first few variables:

```python
a = 10    # Idle threshold (seconds before mouse jiggle starts)
b = 0.2   # Jiggle frequency (per second) → higher = more often
oo = 1    # Jiggle distance (pixels)
```

**Here’s what they do:**
- **`a`**: How long you can be idle before AntiAFK acts.  
  Example: `a = 300` → waits 5 minutes before wiggling.
- **`b`**: How many jiggles per second once it starts.  
  Example: `b = 1` → 1 jiggle per second, `b = 0.5` → 1 jiggle every 2 seconds.
- **`oo`**: How far the cursor moves in pixels.  
  Example: `oo = 3` → more noticeable movement (but still subtle).

You can tweak these values to be *subtle as a spy* or *hyperactive like a squirrel*.

---

## 🛑 Pausing & Quitting
- **Right-click** the tray icon → choose “Pause” to stop temporarily.  
- Choose “Quit” to close the app completely.

---

## 🏢 Corporate Survival Tips
- Never let the green dot fade — it’s a sign of weakness.  
- Keep a random spreadsheet open for camouflage.  
- Occasionally nod at the screen to sell the illusion.  
- Use “In a meeting” as your second shield.

---

## 📜 Disclaimer
This app is for **educational purposes only**.  
If your boss catches you, we were *never here*… just like you weren’t. 😏

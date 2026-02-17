# 📚 Book Search App

A **simple dark-mode book search web app** built with **FastAPI** and **vanilla HTML/CSS/JS**. Search by **title**, **author**, or **publisher** instantly!

---

## 🚀 Features

- Search books by **title**, **author**, or **publisher**
- Minimal **dark-mode UI** with **loading animation**
- Shows **number of search results**
- FastAPI **REST API** backend with CORS enabled
- Easy to run locally using **Python venv**

---

## 🛠 Tech Stack

- **Backend:** Python 3 + FastAPI  
- **Frontend:** HTML, CSS, JavaScript (vanilla)  
- **Styling:** Minimalist dark mode  

---

## ⚡ Quick Start

1. **Clone the repo**  
   ```bash
   git clone <your-repo-url>
   cd backend  

2. **Create & activate virtual environment**  
    python -m venv venv
    # Windows
    venv\Scripts\activate
    # macOS/Linux
    source venv/bin/activate

3. **Install dependencies**  
    pip install -r requirements.txt  

4. **Run backend**  
    uvicorn main:app --reload  

5. **Open frontend**  
    Open frontend/index.html in your browser, type a query, and enjoy the search!

##  📖 Example

    Search "Prentice Hall" → Shows all books published by Prentice Hall.  
    Search "Raspberry" → Finds all Raspberry Pi related books.  

##  🔧 Notes

Make sure backend is running before using the frontend.  
Dataset is currently local, can be extended in main.py.  
Vanilla JS frontend – no frameworks needed.  
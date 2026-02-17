from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

books = [
    {"title":"Game Ai Pro 360","author":"Steve Rabin","publisher":"Prentice Hall"},
    {"title":"Information Processing and Management of Uncertainty in Knowledge-Based Systems","author":"Joao Paulo Carvalho","publisher":"Addison-Wesley"},
    {"title":"The Book of Shaders","author":"Patricio Gonzalez Vivo","publisher":"No Starch Press"},
    {"title":"Storytelling with Data","author":"Cole Nussbaumer Knaflic","publisher":"Prentice Hall"},
    {"title":"Swift programming","author":"Matthew Mathias","publisher":"Prentice Hall"},
    {"title":"C# Game Programming Cookbook for Unity 3D","author":"Jeff W. Murray","publisher":"Prentice Hall"},
    {"title":"Analyzing Baseball Data With R","author":"Jim Albert","publisher":"No Starch Press"},
    {"title":"Adventures in Raspberry Pi","author":"Carrie Anne Philbin","publisher":"Prentice Hall"},
    {"title":"Raspberry Pi User Guide","author":"Eben Upton","publisher":"Prentice Hall"},
    {"title":"Arduino Cookbook","author":"Michael Margolis","publisher":"Prentice Hall"},
    {"title":"Android Fully Loaded","author":"Rob Huddleston","publisher":"Prentice Hall"},
    {"title":"Computer graphics through openGL","author":"Sumanta Guha","publisher":"Addison-Wesley"},
    {"title":"3D Game Environments","author":"Luke Ahearn","publisher":"Prentice Hall"},
    {"title":"Apple Training Series","author":"Peachpit Press","publisher":"No Starch Press"},
    {"title":"Apple Pro Training Series","author":"Diana Weynand","publisher":"No Starch Press"}
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/search")
def search_books(q: str = None):
    filtered_books = []
    for book in books:
        if (q.lower() in book["title"].lower() or q.lower() in book["author"].lower() or q.lower() in book["publisher"].lower()):
            filtered_books.append(book)

    return{ "Search Result" : filtered_books }
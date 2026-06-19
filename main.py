from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import csv

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

data = []

with open("q-fastapi.csv") as f:
    reader = csv.DictReader(f)
    for r in reader:
        data.append({
            "studentId": int(r["studentId"]),
            "class": r["class"]
        })

@app.get("/api")
def get_students(class_: list[str] | None = Query(default=None, alias="class")):
    if class_:
        return {"students": [s for s in data if s["class"] in class_]}
    return {"students": data}

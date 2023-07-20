from fastapi import FastAPI

app = FastAPI()
away = 0
home = 0


@app.get("/score")
def read_score():
    return {"away": away, "home": home}


@app.get("/goal")
def update_score(team=None):
    if team == "away":
        global away
        away = away + 1
    elif team == "home":
        global home
        home = home + 1
    return {"away": away, "home": home}
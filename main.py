from fastapi import FastAPI

app=FastAPI()

@app.get("/calculator/")
def calculator(first_number: str, action: str, second_number: str):
    if action=='+':
        return {int(first_number) + int(second_number)}
    if action=='-':
        return {int(first_number) - int(second_number)}
    if action=='*':
        return {int(first_number) * int(second_number)}
    if action=='/':
        return {int(first_number) / int(second_number)}
    if action=='**':
        return {int(first_number)**int(second_number)}












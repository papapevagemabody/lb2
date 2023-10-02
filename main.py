from fastapi import FastAPI

app=FastAPI()

@app.get("/calculator/")
def calculator(first_number: str, action: str, second_number: str):
    if action=='+':
        return {'ответ':int(first_number) + int(second_number)}
    if action=='-':
        return {'ответ':int(first_number) - int(second_number)}
    if action=='*':
        return {'ответ':int(first_number) * int(second_number)}
    if action=='/' and second_number !='0':
        return {'ответ':int(first_number) / int(second_number)}
    if action=='**':
        return {'ответ':int(first_number)**int(second_number)}
    if second_number=='0' and action=='/':
        return {'невозможная операция'}











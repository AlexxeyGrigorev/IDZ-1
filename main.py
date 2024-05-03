from fastapi import FastAPI

app = FastAPI()


@app.get('/')
async def name():
     return {"Григорьев Алексей Александрович"}

@app.get('/tools')
async def skills():
    return "Web-дизайнер начинающий"

@app.get('/users')
async def number():
    return "8 *** *** ** 46"

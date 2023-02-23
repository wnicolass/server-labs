from fastapi import FastAPI, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://127.0.0.1:5500",
    "http://127.0.0.1:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=["*"]
)

@app.post('/register')
async def register(player: str):
    return f"bem vindo {player}"

###################################
def main():
    import uvicorn

    uvicorn.run('app:app', reload=True)

if __name__ == '__main__':
    main()



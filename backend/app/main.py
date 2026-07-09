from fastapi import FastAPI

app = FastAPI(
    title="Student Support Chatbot API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "message": "Welcome to the Student Support Chatbot API!"
    }

@app.get("/health")
def health():
    return {
        "status": "OK"
    }
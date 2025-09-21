from fastapi import FastAPI
from .routes import meetings, users

app = FastAPI(title="AI Meeting Manager 🚀")

# Routers
app.include_router(meetings.router, prefix="/api/meetings", tags=["Meetings"])
app.include_router(users.router, prefix="/api/users", tags=["Users"])

@app.get("/")
def root():
    return {"message": "AI Meeting Manager Backend is Running 🚀"}

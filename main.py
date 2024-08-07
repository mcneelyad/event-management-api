from fastapi import FastAPI

from src.routers import events_router

app = FastAPI()
app.include_router(events_router.router, prefix="/events")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)
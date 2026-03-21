from fastapi import FastAPI
from src.database.database import lifespan
from src.routes.sheduled_payments_routes import router as sheduled_payments_router



app = FastAPI(
    title="Sheduled Payments API",
    description="API for managing scheduled payments",
    version="1.0.0",
    lifespan=lifespan,
)
app.include_router(sheduled_payments_router)


@app.get("/")
async def root():
    return {"message": "Welcome to the Scheduled Payments API!"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="localhost", port=8000, reload=True)

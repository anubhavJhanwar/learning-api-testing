from fastapi import FastAPI
from database import engine, Base
from routes.users import router as users_router

# Create all tables on startup (if they don't already exist)
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Users CRUD API",
    description="A simple REST API for managing users with FastAPI + MySQL.",
    version="1.0.0"
)

# Register routes
app.include_router(users_router)


@app.get("/", tags=["Health"])
def root():
    """Health check endpoint."""
    return {"status": "ok", "message": "Users API is running."}

"""FastAPI entry‑point.

- Creates the FastAPI app.
- Runs startup logic (creating the database tables) via a lifespan handler.
- Includes the health router and the coffee router.
- (Optional) mounts the authentication dependency when you uncomment it.
"""

from contextlib import asynccontextmanager

from fastapi import FastAPI

from app.database import create_db_and_tables
from app.routers import coffee, health

@asynccontextmanager
async def lifespan(app: FastAPI):
    # --- startup ---
    create_db_and_tables()   # Create the SQLite tables if they don't exist yet.
    yield
    # --- shutdown ---


app = FastAPI(
    title="Campus‑Coffee Demo API",
    description="A tiny API that demonstrates the Router → Controller → Service → Model pattern.",
    version="0.1.0",
    lifespan=lifespan,
)

# ----------------------------------------------------------------------
# Public (unauthenticated) routes
# ----------------------------------------------------------------------
app.include_router(health.router)          # /health
app.include_router(coffee.router, prefix="/coffee", tags=["coffee"])

# ----------------------------------------------------------------------
# Authentication (commented out – enable when you have time)
# ----------------------------------------------------------------------
# from fastapi import Depends
# from fastapi.security import HTTPBearer
# from app.dependencies import get_current_user
#
# security = HTTPBearer()
#
# # Example: protect ALL coffee routes with a bearer token
# # app.include_router(
# #     coffee.router,
# #     prefix="/coffee",
# #     tags=["coffee"],
# #     dependencies=[Depends(security), Depends(get_current_user)],
# # )
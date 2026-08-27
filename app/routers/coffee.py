"""FastAPI Router – wires HTTP verbs & paths to service functions.

All FastAPI‑specific concerns (dependency injection, HTTPException handling)
live here, while the pure business logic stays in `app.services.coffee`.
"""

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.database import get_session
from app.schemas.coffee import CoffeeCreate, CoffeeRead, CoffeeUpdate
from app.services.coffee import CoffeeService

router = APIRouter()


# ----------------------------------------------------------------------
# CREATE
# ----------------------------------------------------------------------
@router.post(
    "/",
    response_model=CoffeeRead,
    status_code=status.HTTP_201_CREATED,
    summary="Add a new coffee drink",
)
def create(
    payload: CoffeeCreate,
    session: Session = Depends(get_session),
):
    """
    FastAPI injects a DB session, forwards the payload to the service,
    and returns the created object (including the auto‑generated `id`).
    """
    coffee = CoffeeService.create(session, payload)
    return CoffeeRead.model_validate(coffee)


# ----------------------------------------------------------------------
# READ – list all coffees
# ----------------------------------------------------------------------
@router.get(
    "/",
    response_model=list[CoffeeRead],
    summary="List all coffee drinks",
)
def read_all(
    session: Session = Depends(get_session),
):
    coffees = CoffeeService.list_all(session)
    return [CoffeeRead.model_validate(c) for c in coffees]


# ----------------------------------------------------------------------
# READ – single coffee by ID
# ----------------------------------------------------------------------
@router.get(
    "/{coffee_id}",
    response_model=CoffeeRead,
    summary="Get a coffee drink by its ID",
)
def read_one(
    coffee_id: int,
    session: Session = Depends(get_session),
):
    coffee = CoffeeService.get_by_id(session, coffee_id)
    if coffee is None:
        raise HTTPException(status_code=404, detail="Coffee not found")
    return CoffeeRead.model_validate(coffee)


# ----------------------------------------------------------------------
# DELETE – remove a coffee
# ----------------------------------------------------------------------
@router.delete(
    "/{coffee_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Delete a coffee drink",
)
def delete(
    coffee_id: int,
    session: Session = Depends(get_session),
):
    """
    Calls the service to delete the record.
    Returns 204 No Content on success; 404 if the record does not exist.
    """
    success = CoffeeService.delete(session, coffee_id)
    if not success:
        raise HTTPException(status_code=404, detail="Coffee not found")
    # FastAPI interprets a `None` return with a 204 status as an empty body.
    return None


# ----------------------------------------------------------------------
# PATCH – partially update a coffee (commented out, enable when time permits)
# ----------------------------------------------------------------------
# @router.patch(
#     "/{coffee_id}",
#     response_model=CoffeeRead,
#     summary="Partially update a coffee drink",
# )
# def patch(
#     coffee_id: int,
#     payload: CoffeeUpdate,
#     session: Session = Depends(get_session),
# ):
#     coffee = CoffeeService.update(session, coffee_id, payload)
#     if coffee is None:
#         raise HTTPException(status_code=404, detail="Coffee not found")
#     return CoffeeRead.model_validate(coffee)
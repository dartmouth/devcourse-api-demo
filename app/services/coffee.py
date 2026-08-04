"""Business‑logic layer.

All interactions with the DB happen here. Controllers stay thin – they only
translate HTTP details (status codes, request bodies) into service calls.
"""

from typing import List, Optional

from sqlmodel import Session, select

from app.models import Coffee
from app.schemas.coffee import CoffeeCreate, CoffeeUpdate


class CoffeeService:
    """Encapsulates all CRUD operations for the Coffee resource."""

    @staticmethod
    def create(session: Session, payload: CoffeeCreate) -> Coffee:
        coffee = Coffee(**payload.model_dump())
        session.add(coffee)
        session.commit()
        session.refresh(coffee)
        return coffee

    @staticmethod
    def get_by_id(session: Session, coffee_id: int) -> Optional[Coffee]:
        return session.get(Coffee, coffee_id)

    @staticmethod
    def list_all(session: Session) -> List[Coffee]:
        stmt = select(Coffee).order_by(Coffee.id)
        return session.exec(stmt).all()

    @staticmethod
    def delete(session: Session, coffee_id: int) -> bool:
        coffee = session.get(Coffee, coffee_id)
        if coffee is None:
            return False
        session.delete(coffee)
        session.commit()
        return True

    # ------------------------------------------------------------------
    # PATCH endpoint (commented out – enable when you have time)
    # ------------------------------------------------------------------
    # @staticmethod
    # def update(session: Session, coffee_id: int, payload: CoffeeUpdate) -> Optional[Coffee]:
    #     coffee = session.get(Coffee, coffee_id)
    #     if coffee is None:
    #         return None
    #     coffee_data = payload.dict(exclude_unset=True)
    #     for key, value in coffee_data.items():
    #         setattr(coffee, key, value)
    #     session.add(coffee)
    #     session.commit()
    #     session.refresh(coffee)
    #     return coffee
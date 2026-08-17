"""Business‑logic layer.

All interactions with the DB happen here. Controllers stay thin – they only
translate HTTP details (status codes, request bodies) into service calls.
"""

from datetime import datetime
from typing import List, Optional, Tuple

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
    # Business logic that needs no database at all.
    #
    # Not every service method has to read or write a row. This one takes
    # (optional) input, applies a few rules, and returns an answer – no
    # `Session` parameter in sight.
    # ------------------------------------------------------------------
    _RECOMMENDATIONS: dict = {
        "morning": ("Espresso", "A strong start to kick off the day."),
        "afternoon": ("Latte", "Something smoother to get through the slump."),
        "evening": (
            "Decaf Americano",
            "Still coffee-flavored, but won't wreck your sleep.",
        ),
        "night": ("Herbal Tea", "Maybe skip the coffee at this hour."),
    }

    @staticmethod
    def _time_of_day(hour: int) -> str:
        if 5 <= hour < 12:
            return "morning"
        if 12 <= hour < 17:
            return "afternoon"
        if 17 <= hour < 21:
            return "evening"
        return "night"

    @classmethod
    def recommend(cls, time_of_day: Optional[str] = None) -> Tuple[str, str, str]:
        """Return (time_of_day, recommendation, reason) for the given time.

        If no `time_of_day` is supplied, it's derived from the current
        server time. This is pure business logic – deterministic given its
        inputs, with nothing to persist or fetch.
        """
        period = (time_of_day or "").strip().lower()
        if period not in cls._RECOMMENDATIONS:
            period = cls._time_of_day(datetime.now().hour)
        drink, reason = cls._RECOMMENDATIONS[period]
        return period, drink, reason

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

"""Thin layer that turns FastAPI request/response objects into service calls.

Each function returns a Pydantic schema (or raises an HTTPException) – the
router then handles turning that into JSON + proper status code.
"""

from typing import Optional

from fastapi import HTTPException
from sqlmodel import Session

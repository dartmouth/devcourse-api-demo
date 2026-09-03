"""FastAPI Router – wires HTTP verbs & paths to controller functions."""

from typing import Optional

from fastapi import APIRouter, Depends, HTTPException, status
from sqlmodel import Session

from app.database import get_session

router = APIRouter()

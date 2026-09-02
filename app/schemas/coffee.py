"""Pydantic schemas that define the public contract of the API.

We keep them separate from the DB model so we never expose internal columns
(e.g., timestamps, internal IDs) unless we explicitly want to.
"""

from typing import Optional
from pydantic import BaseModel, Field, PositiveFloat
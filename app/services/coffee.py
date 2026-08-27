"""Business‑logic layer.

All interactions with the DB happen here. Controllers stay thin – they only
translate HTTP details (status codes, request bodies) into service calls.
"""

from datetime import datetime
from typing import List, Optional, Tuple

from sqlmodel import Session, select
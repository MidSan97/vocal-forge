"""
Web package for the Vocal Forge project.

This package contains modules which define the web application of the
Vocal Forge project.
"""

from __future__ import annotations

import asyncio
import os

from vocal_forge.core.main import initialize

initialize()

if os.name == "nt":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

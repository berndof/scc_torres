import sys
from pathlib import Path

import uvicorn

sys.path.insert(0, str(Path(__file__).parent.parent / "src"))

from core.config import APP_LISTEN_ADDR, APP_LISTEN_PORT
from core.loader import load_modules

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        host=APP_LISTEN_ADDR,
        port=APP_LISTEN_PORT,
        # log_config=LOGGING_CONFIG,
        reload=True,
        loop="uvloop",
        reload_dirs=["src/"],
        reload_delay=1.0,
    )

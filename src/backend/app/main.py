from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.routes.route import router as match_router # 👈 Import your router

app = FastAPI()

# ---------------------------------------------------------
#  ENABLE CORS (Crucial for Frontend-Backend Communication)
# ---------------------------------------------------------

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# ---------------------------------------------------------
#  API ENDPOINTS
# ---------------------------------------------------------
app.include_router(match_router, prefix="/api")
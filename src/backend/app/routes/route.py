from fastapi import APIRouter
from controllers import matchController

router = APIRouter()

router.post("/getMatch", matchController.get_match)
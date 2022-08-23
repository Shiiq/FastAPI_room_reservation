from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession

from ..validators import check_meeting_room_exists, check_reservation_intersections
from crud.reservation import reservation_crud
from core.db import get_async_session
from schemas.reservation import ReservationCreate, ReservationDB

router = APIRouter()


@router.post('/',
    response_model=ReservationDB
)
async def create_reservation(
        reservation: ReservationCreate,
        session: AsyncSession = Depends(get_async_session)
) -> ReservationDB:
    await check_meeting_room_exists(reservation.meetingroom_id, session)
    await check_reservation_intersections(**reservation.dict(), session=session)
    new_reservation = await reservation_crud.create(reservation, session)
    return new_reservation

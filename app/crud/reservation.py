from typing import Optional

from datetime import datetime
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import and_, between, or_, select

from crud.base import CRUDBase
from models import Reservation, User


class CRUDReservation(CRUDBase):

    async def get_by_user(
            self, session: AsyncSession, user: User
    ):
        reservations = await session.execute(
            select(Reservation).where(
                Reservation.user_id == user.id
            )
        )
        return reservations.scalars().all()

    async def get_reservations_at_the_same_time(
            self,
            *,
            from_reserve: datetime,
            to_reserve: datetime,
            meetingroom_id: int,
            reservation_id: Optional[id] = None,
            session: AsyncSession,
    ) -> list[Reservation]:
        select_statement = select(Reservation).where(
            Reservation.meetingroom_id == meetingroom_id,
            and_(
                from_reserve <= Reservation.to_reserve,
                to_reserve >= Reservation.from_reserve
            )
        )
        if reservation_id is not None:
            select_statement = select_statement.where(
                Reservation.id != reservation_id
            )
        reservations = await session.execute(select_statement)
        reservations = reservations.scalars().all()
        return reservations

    async def get_future_reservations_for_room(self, meetingroom_id, session):
        select_statement = select(Reservation).where(
            Reservation.meetingroom_id == meetingroom_id,
            Reservation.to_reserve > datetime.now()
        )
        reservations = await session.execute(select_statement)
        reservations = reservations.scalars().all()
        return reservations


reservation_crud = CRUDReservation(Reservation)

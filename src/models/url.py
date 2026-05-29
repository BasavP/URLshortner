from datetime import datetime

from sqlalchemy import BigInteger, DateTime, Index, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column

from src.db.base import Base


class Url(Base):
    __tablename__ = "urls"

    short_code: Mapped[str] = mapped_column(String, primary_key=True)
    long_url: Mapped[str] = mapped_column(Text, nullable=False)
    canonical_long_url: Mapped[str] = mapped_column(Text, nullable=False)
    generation_type: Mapped[str] = mapped_column(String, nullable=False)
    expires_at: Mapped[datetime | None] = mapped_column(DateTime(timezone=True), nullable=True)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        nullable=False,
        server_default=func.now(),
    )
    created_by_user_id: Mapped[int | None] = mapped_column(BigInteger, nullable=True)


Index(
    "unique_system_canonical",
    Url.canonical_long_url,
    unique=True,
    postgresql_where=Url.generation_type == "system",
)

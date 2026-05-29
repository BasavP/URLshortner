"""create urls table

Revision ID: 0001_create_urls_table
Revises: 
Create Date: 2026-05-29 00:00:00.000000
"""

import sqlalchemy as sa

from alembic import op

revision = "0001_create_urls_table"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "urls",
        sa.Column("short_code", sa.String(), primary_key=True, nullable=False),
        sa.Column("long_url", sa.Text(), nullable=False),
        sa.Column("canonical_long_url", sa.Text(), nullable=False),
        sa.Column("generation_type", sa.String(), nullable=False),
        sa.Column("expires_at", sa.DateTime(timezone=True), nullable=True),
        sa.Column(
            "created_at",
            sa.DateTime(timezone=True),
            nullable=False,
            server_default=sa.func.now(),
        ),
        sa.Column("created_by_user_id", sa.BigInteger(), nullable=True),
    )
    op.create_index(
        "unique_system_canonical",
        "urls",
        ["canonical_long_url"],
        unique=True,
        postgresql_where=sa.text("generation_type = 'system'"),
    )


def downgrade() -> None:
    op.drop_index("unique_system_canonical", table_name="urls")
    op.drop_table("urls")

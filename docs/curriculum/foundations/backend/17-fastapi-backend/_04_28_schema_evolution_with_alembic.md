# Schema Evolution with Alembic

> **Course**: Fastapi | **Module**: Database Integration | **Difficulty**: advanced

---

### 1. Alembic Setup
```bash
pip install alembic
alembic init alembic
```

```python
# alembic/env.py
from app.models import Base
target_metadata = Base.metadata

def run_migrations_online():
    connectable = engine_from_config(...)
    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)
        with context.begin_transaction():
            context.run_migrations()
```

### 2. Creating Migrations
```bash
alembic revision --autogenerate -m "add users table"
alembic upgrade head
alembic downgrade -1
alembic history --verbose
alembic current
```

### 3. Migration File
```python
# alembic/versions/001_add_users.py
def upgrade():
    op.create_table('users',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('email', sa.String(255), nullable=False, unique=True),
        sa.Column('created_at', sa.DateTime(), server_default=sa.func.now()),
    )
    op.create_index('ix_users_email', 'users', ['email'])

def downgrade():
    op.drop_index('ix_users_email')
    op.drop_table('users')
```

### 4. Async Alembic
```python
# For SQLAlchemy async engine
from sqlalchemy.ext.asyncio import AsyncConnection

async def run_async_migrations():
    async with engine.begin() as conn:
        await conn.run_sync(do_run_migrations)
```

---

Add `created_at` and `updated_at` columns to an existing `products` table via Alembic migration. Then add an index, run forward/backward migrations, and verify with `alembic history`.

---

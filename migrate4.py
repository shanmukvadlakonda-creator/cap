from app.app import create_app, db
from sqlalchemy import text

app = create_app()
with app.app_context():
    with db.engine.connect() as conn:
        conn.execute(text("""
            ALTER TABLE loans
                ADD COLUMN IF NOT EXISTS type VARCHAR(50) NOT NULL DEFAULT 'Personal',
                ADD COLUMN IF NOT EXISTS lender VARCHAR(200),
                ADD COLUMN IF NOT EXISTS principal_amount NUMERIC(15,2) NOT NULL DEFAULT 0,
                ADD COLUMN IF NOT EXISTS interest_rate NUMERIC(5,2),
                ADD COLUMN IF NOT EXISTS emi_amount NUMERIC(15,2),
                ADD COLUMN IF NOT EXISTS start_date DATE,
                ADD COLUMN IF NOT EXISTS end_date DATE,
                ADD COLUMN IF NOT EXISTS account_id INTEGER REFERENCES accounts(id),
                ADD COLUMN IF NOT EXISTS notes TEXT,
                ADD COLUMN IF NOT EXISTS is_active BOOLEAN NOT NULL DEFAULT TRUE,
                ADD COLUMN IF NOT EXISTS created_at TIMESTAMP DEFAULT NOW();
        """))
        conn.commit()
    print("Migration 4 complete: loans table expanded.")

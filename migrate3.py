from app.app import create_app, db
from sqlalchemy import text

app = create_app()
with app.app_context():
    with db.engine.connect() as conn:
        conn.execute(text(
            "ALTER TABLE transactions ADD COLUMN IF NOT EXISTS account_id INTEGER REFERENCES accounts(id);"
        ))
        conn.execute(text(
            "ALTER TABLE transactions ADD COLUMN IF NOT EXISTS payment_method VARCHAR(50) DEFAULT 'Cash';"
        ))
        conn.execute(text(
            "ALTER TABLE transactions ADD COLUMN IF NOT EXISTS note TEXT;"
        ))
        conn.commit()
    print("Migration 3 complete: account_id, payment_method, note added to transactions.")

from database import SessionLocal, engine
import models

def seed_problems():
    db = SessionLocal()
    try:
        # Check if problems already exist
        if db.query(models.Problem).first():
            print("Problems already exist. Skipping seed.")
            return

        problems = [
            models.Problem(
                id="1",
                title="1. Implement Linear Regression Prediction",
                difficulty="Easy",
                description="Write a function `predict(x, w, b)` that computes the linear regression prediction $y = wx + b$.",
                starting_code="def predict(x, w, b):\n    # Your code here\n    pass\n"
            ),
            models.Problem(
                id="2",
                title="2. Softmax Function",
                difficulty="Medium",
                description="Implement the softmax function `softmax(z)` which normalizes an array of values to a probability distribution.",
                starting_code="import numpy as np\n\ndef softmax(z):\n    # Your code here\n    pass\n"
            )
        ]
        db.add_all(problems)
        db.commit()
        print("Successfully seeded problems.")
    except Exception as e:
        print(f"Error seeding problems: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    # Create tables if they don't exist
    models.Base.metadata.create_all(bind=engine)
    seed_problems()

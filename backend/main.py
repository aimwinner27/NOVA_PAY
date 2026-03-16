from fastapi import FastAPI
from pydantic import BaseModel
from payment_logic import evaluate_transaction

app = FastAPI()

class PaymentRequest(BaseModel):
    amount: int
    recipient: str


# Home route (fix for 404)
@app.get("/")
def read_root():
    return {"message": "Welcome to NOVA_PAY API 🚀"}


@app.post("/process-payment")
def process_payment(payment: PaymentRequest):
    amount = payment.amount
    recipient = payment.recipient

    return evaluate_transaction(amount, recipient)

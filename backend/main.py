from fastapi import FastAPI
from pydantic import BaseModel

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

    # Simple risk logic
    if amount > 5000:
        return {
            "status": "warning",
            "message": f"⚠️ Transaction of ₹{amount} to {recipient} looks unusual. Please verify."
        }

    return {
        "status": "success",
        "message": f"✅ Payment of ₹{amount} to {recipient} processed successfully."
    }
def evaluate_transaction(amount, recipient):

    trust_score = 90

    # Simple fraud detection logic
    if amount > 5000:
        trust_score = 40

    if trust_score < 50:
        return {
            "status": "warning",
            "message": "⚠️ This transaction looks unusual. Please verify carefully."
        }

    return {
        "status": "success",
        "message": f"✅ Payment of ₹{amount} to {recipient} processed successfully."
    }
const micBtn = document.getElementById('micBtn');
const voiceStatus = document.getElementById('voiceStatus');
const recipientInput = document.getElementById('recipient');
const amountInput = document.getElementById('amount');
const feedback = document.getElementById('feedback');

// Simulate Voice Recognition
function startVoice() {
        micBtn.classList.add('listening');
        voiceStatus.innerText = "Listening...";
        feedback.style.display = "none";

        // Simulating AI processing time
        setTimeout(() => {
            micBtn.classList.remove('listening');
            voiceStatus.innerText = "";
            
            // Mocking extracted data from a voice command: "Send 500 rupees to Ravi"
            recipientInput.value = "Ravi";
            amountInput.value = "500";
            
            showFeedback("I've filled the details for Ravi. Please check and press Send.", "warning-msg");
        }, 2500);
    }

    function processPayment() {
        const name = recipientInput.value;
        const amt = amountInput.value;

        if (!name || !amt) {
            showFeedback("Please tell me who and how much.", "error-msg");
            return;
        }

        // Warning for large amounts (Elderly protection)
        if (amt > 5000) {
            showFeedback("⚠️ That's a lot of money! Are you sure you want to send ₹" + amt + " to " + name + "?", "warning-msg");
            // Change button text to confirm
            document.querySelector('.send-btn').innerText = "YES, I AM SURE";
            document.querySelector('.send-btn').onclick = confirmFinal;
            return;
        }

        confirmFinal();
    }

    function confirmFinal() {
        const name = recipientInput.value;
        const amt = amountInput.value;
        
        showFeedback("✅ Success! ₹" + amt + " sent to " + name + ".", "success-msg");
        
        // Reset button
        const btn = document.querySelector('.send-btn');
        btn.innerText = "SEND MONEY NOW";
        btn.onclick = processPayment;
        
        // Clear fields after short delay
        setTimeout(() => {
            recipientInput.value = "";
            amountInput.value = "";
        }, 3000);
    }

    function showFeedback(text, className) {
        feedback.innerText = text;
        feedback.className = className;
        feedback.style.display = "block";
    }




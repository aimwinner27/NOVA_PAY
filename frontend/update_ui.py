from pathlib import Path
p = Path('index.html')
text = p.read_text(encoding='utf-8')
start = text.find('<style>')
end = text.find('</style>', start)
if start == -1 or end == -1:
    raise SystemExit('style chunk not found')
end += len('</style>')
new_style = '''    <style>
        :root {
            --primary: #3E7BFF;
            --accent: #1EC2A9;
            --purple: #7569FF;
            --indigo: #2E3A8D;
            --text: #102547;
            --muted: #667992;
            --white: #ffffff;
            --card: rgba(255,255,255,0.85);
            --shadow: 0 24px 40px rgba(35, 62, 143, 0.21);
        }

        *, *::before, *::after {
            box-sizing: border-box;
        }

        html, body {
            margin: 0;
            min-height: 100%;
            color: var(--text);
            font-family: 'Lexend', sans-serif;
            background: radial-gradient(circle at 21% 13%, #e9f2ff 0%, #f5f9ff 40%, #f5f9ff 100%);
        }

        body {
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 2rem;
        }

        .app-container {
            width: min(100%, 540px);
            border-radius: 28px;
            border: 1px solid rgba(81, 124, 247, 0.17);
            background: linear-gradient(150deg, rgba(255,255,255,0.95), rgba(255,255,255,0.70));
            box-shadow: var(--shadow);
            overflow: hidden;
            backdrop-filter: blur(7px);
        }

        .hero-banner {
            text-align: center;
            background: linear-gradient(145deg, #3E7BFF, #7569FF);
            color: var(--white);
            padding: 1.3rem 1.2rem;
        }

        .logo {
            margin: 0;
            font-size: 2rem;
            font-weight: 900;
            letter-spacing: 0.06rem;
            text-shadow: 0 10px 22px rgba(0,0,0,0.2);
        }

        .subtitle {
            margin: 0.3rem 0 0;
            font-size: 1rem;
            font-weight: 500;
            color: rgba(255,255,255,0.9);
        }

        .app-main {
            padding: 1.6rem;
        }

        .voice-section {
            background: rgba(62, 123, 255, 0.08);
            border: 1px dashed rgba(62, 123, 255, 0.38);
            border-radius: 18px;
            padding: 1.2rem;
            margin-bottom: 1.35rem;
            text-align: center;
        }

        .voice-section label {
            display: block;
            font-weight: 700;
            color: #274b93;
            margin-bottom: 0.45rem;
        }

        .mic-btn {
            width: 92px;
            height: 92px;
            border-radius: 999px;
            border: 0;
            background: linear-gradient(145deg, #1EC2A9, #3E7BFF);
            color: #fff;
            font-size: 2.1rem;
            cursor: pointer;
            box-shadow: 0 12px 22px rgba(62, 123, 255, 0.32);
            transition: transform 0.2s ease, filter 0.3s ease;
        }

        .mic-btn:hover { transform: translateY(-2px) scale(1.04); filter: saturate(1.2); }

        .mic-btn.listening {
            animation: pulse 1.2s ease-out infinite;
            background: #ff4b6e;
        }

        @keyframes pulse {
            0% { box-shadow: 0 0 0 0 rgba(255, 75, 110, 0.35); }
            70% { box-shadow: 0 0 0 20px rgba(255, 75, 110, 0); }
            100% { box-shadow: 0 0 0 0 rgba(255, 75, 110, 0); }
        }

        .input-group { margin-bottom: 1.05rem; }

        label {
            font-size: 0.94rem;
            font-weight: 700;
            color: #2a4372;
            margin-bottom: 0.35rem;
            display: block;
        }

        input {
            width: 100%;
            padding: 0.95rem 1rem;
            border: 1px solid rgba(56, 93, 155, 0.25);
            border-radius: 14px;
            background: rgba(255,255,255,0.92);
            font-size: 1.05rem;
            font-weight: 600;
            color: #24395f;
            transition: all 0.2s ease;
        }

        input:focus {
            outline: none;
            border-color: var(--primary);
            box-shadow: 0 0 0 5px rgba(62, 123, 255, 0.13);
        }

        .send-btn {
            width: 100%;
            border-radius: 14px;
            border: 0;
            padding: 0.95rem;
            background: linear-gradient(120deg, #1EC2A9, #2F9BFC);
            color: #fff;
            font-size: 1.1rem;
            font-weight: 800;
            letter-spacing: 0.02rem;
            cursor: pointer;
            margin-top: 0.7rem;
            box-shadow: 0 14px 28px rgba(46, 58, 141, 0.25);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
        }

        .send-btn:hover { transform: translateY(-2px); box-shadow: 0 18px 34px rgba(46, 58, 141, 0.36); }

        #feedback {
            margin-top: 1.25rem;
            padding: 0.8rem 1rem;
            border-radius: 12px;
            display: none;
            font-size: 0.96rem;
            font-weight: 600;
            border: 1px solid transparent;
        }

        .success-msg { background: #E8F7F4; color: #0f765e; border-color: #1EC2A9; }
        .warning-msg { background: #FFF7EB; color: #C7661D; border-color: #F2A248; }
        .error-msg { background: #FFF1F2; color: #A42D42; border-color: #E13B4D; }

        .hint { font-size: 0.88rem; color: var(--muted); margin: 0; }

        .stats { display: grid; grid-template-columns: repeat(2, 1fr); gap: 0.65rem; margin-top: 1rem; }

        .stat-card {
            background: rgba(255,255,255,0.75);
            border: 1px solid rgba(90, 112, 187, 0.18);
            border-radius: 12px;
            padding: 0.65rem;
            text-align: center;
            font-weight: 700;
            color: #1f3e83;
            font-size: 0.84rem;
        }

        .stat-card span { display: block; font-size: 1.1rem; margin-top: 0.15rem; color: #1f3e83; }
    </style>'''
text = text[:start] + new_style + text[end:]

body_start = text.find('<div class="app-container">')
if body_start == -1:
    raise SystemExit('app container not found')
body_end = text.find('<script>', body_start)
if body_end == -1:
    raise SystemExit('script section not found')

new_app_html = '''<div class="app-container">
    <div class="hero-banner">
        <h1 class="logo">NOVA_PAY</h1>
        <p class="subtitle">Fast, Secure, Voice-Enabled Payments</p>
    </div>

    <div class="app-main">
        <div class="voice-section">
            <label>Tap the mic and say your command</label>
            <button id="micBtn" class="mic-btn" onclick="startVoice()">🎙️</button>
            <p class="hint">Try: "Send 500 to Ravi"</p>
            <p id="voiceStatus" style="font-weight:bold;color:var(--primary);height:20px;"></p>
        </div>

        <div class="input-group">
            <label for="recipient">Payee</label>
            <input type="text" id="recipient" placeholder="Enter recipient name" />
        </div>

        <div class="input-group">
            <label for="amount">Amount (₹)</label>
            <input type="number" id="amount" placeholder="0.00" />
        </div>

        <button class="send-btn" onclick="processPayment()">SEND MONEY NOW</button>

        <div id="feedback"></div>

        <div class="stats">
            <div class="stat-card">Today’s transfers<span>3</span></div>
            <div class="stat-card">Pending requests<span>1</span></div>
        </div>
    </div>
</div>'''
text = text[:body_start] + new_app_html + text[body_end:]
p.write_text(text, encoding='utf-8')
print('UI upgraded successfully')

p.write_text(text, encoding='utf-8')
print('UI upgraded successfully')

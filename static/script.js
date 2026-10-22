// 1. HTML se form aur elements ko unki ID se pakdo
const loginForm = document.getElementById('loginForm');

// 2. Form ke submit event par listener lagao
if (loginForm) {
    loginForm.addEventListener('submit', function (e) {
        
        // 3. CRITICAL: Browser ka default behavior (page redirect) roko
        e.preventDefault();

        // 4. Input fields se values uthao
        const usernameInput = document.getElementById('username').value.trim();
        const passwordInput = document.getElementById('password').value;

        // 5. Data ko ek simple object (dictionary) me taiyar karo
        const formData = {
            username: usernameInput,
            password: passwordInput
        };

        console.log("Sending data to backend:", formData);

        // 6. Fetch API URL setup:
        // Agar Flask server (port 5000) se chal raha ho toh relative path '/login' use hoga,
        // aur agar Live Server ya direct file se ho toh full URL 'http://127.0.0.1:5000/login' use hoga.
        const apiUrl = (window.location.port === '5000' || window.location.host.includes(':5000'))
            ? '/login'
            : 'http://127.0.0.1:5000/login';

        // Fetch API se Flask server ko POST request bhejo
        fetch(apiUrl, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json' // Backend ko batane ke liye ki hum JSON bhej rahe hain
            },
            body: JSON.stringify(formData) // Object ko string me badal kar bheja
        })
        .then(response => {
            return response.json().then(data => {
                // Response ka status check karo (200 matlab success, 401 matlab unauthorized)
                if (response.status === 200) {
                    alert("🎉 " + (data.message || data.status || "Login successful :)."));
                } else if (response.status === 401) {
                    const errorMsg = data.message || data.status || "Invalid credentials!";
                    alert("❌ " + errorMsg);
                } else {
                    const serverMsg = data.message || data.status || ("Status code: " + response.status);
                    alert("⚠️ " + serverMsg);
                }
            }).catch(() => {
                alert("⚠️ Unexpected response! Status code: " + response.status);
            });
        })
        .catch(error => {
            console.error("Fetch error:", error);
            alert("Server connect nahi ho pa raha! Pakka karo ki Flask server (app.py) chal raha hai.");
        });
    });
}
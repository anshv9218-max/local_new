// 1. HTML se form aur elements ko unki ID se pakdo
const loginForm = document.getElementById('loginForm');

// 2. Form ke submit event par listener lagao
loginForm.addEventListener('submit', function (e) {
    
    // 3. CRITICAL: Browser ka default behavior (page redirect) roko
    e.preventDefault();

    // 4. Input fields se values uthao (ek baar check kar lena HTML me yahi IDs hain na)
    const usernameInput = document.getElementById('username').value;
    const passwordInput = document.getElementById('password').value;

    // 5. Data ko ek simple object (dictionary) me taiyar karo
    const formData = {
        username: usernameInput,
        password: passwordInput
    };

    console.log("Sending data to backend:", formData);

    // 6. Fetch API se Flask server ko POST request bhejo
    // Kyunki app.py me route '@front.route('/sign_up')' hai, toh vahan hit marega
    fetch('http://127.0.0.1:5000/sign_up', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json' // Backend ko batane ke liye ki hum JSON bhej rahe hain
        },
        body: JSON.stringify(formData) // Object ko string me badal kar bheja
    })
    .then(response => {
        // Response ka status check karo (200 matlab success, 401 matlab unauthorized)
        if (response.status === 200) {
            return response.json().then(data => {
                alert("🎉 " + data.message); // Login successful ka alert aayega
                // Yahan se tum page 2 par redirect kar sakte ho baad me:
                // window.location.href = "page2.html";
            });
        } else if (response.status === 401) {
            return response.json().then(data => {
                alert("❌ Error: " + data.message); // User not found ya galat password
            });
        } else {
            alert("⚠️ Something went wrong! Status code: " + response.status);
        }
    })
    .catch(error => {
        console.error("Fetch error:", error);
        alert("Server connect nahi ho pa raha! Pakka karo ki Flask server (app.py) chal raha hai.");
    });
});
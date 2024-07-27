async function login() {
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    const loginMessage = document.getElementById('login-message');

    try {
        const response = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ username, password })
        });

        if (response.ok) {
            const data = await response.json();
            localStorage.setItem('token', data.token);
            document.getElementById('login-section').style.display = 'none';
            document.getElementById('protected-section').style.display = 'block';
        } else {
            const errorData = await response.json();
            loginMessage.textContent = errorData.message;
        }
    } catch (error) {
        loginMessage.textContent = 'Error: ' + error.message;
    }
}

async function getProtectedResource() {
    const token = localStorage.getItem('token');
    const protectedMessage = document.getElementById('protected-message');

    try {
        const response = await fetch('/protected', {
            headers: {
                'Authorization': `Bearer ${token}`
            }
        });

        if (response.ok) {
            const data = await response.json();
            protectedMessage.textContent = data.message;
        } else {
            const errorData = await response.json();
            protectedMessage.textContent = errorData.message;
        }
    } catch (error) {
        protectedMessage.textContent = 'Error: ' + error.message;
    }
}

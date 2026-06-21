
// (Register Page)
const registerForm = document.querySelector('.auth-form'); 
const registerEmail = document.getElementById('RegisterEmail');
const registerPassword = document.getElementById('RegisterPassword');

if (registerForm && registerEmail && document.title === 'Register') {
    
    registerForm.addEventListener('submit', function(e) {
        e.preventDefault(); 
        
        const email = registerEmail.value.trim();
        const password = registerPassword.value.trim();
        const messagePara = registerForm.querySelector('.error-text');

        if (!email || !password) {
            messagePara.textContent = 'გთხოვთ შეავსოთ ორივე ველი!';
            return;
        }

        let users = JSON.parse(localStorage.getItem('users')) || [];
        const userExists = users.find(user => user.email === email);

        if (userExists) {
            messagePara.textContent = 'ეს იმეილი უკვე დარეგისტრირებულია!';
        } else {
            users.push({ email: email, password: password });
            localStorage.setItem('users', JSON.stringify(users));
            
            messagePara.textContent = '';
            alert('რეგისტრაცია წარმატებით დასრულდა!');
            window.location.href = 'login.html'; 
        }
    });
}


//  (Login Page)
const loginForm = document.querySelector('.auth-form');
const loginEmail = document.getElementById('LoginEmail');
const loginPassword = document.getElementById('LoginPassword');

if (loginForm && loginEmail && document.title === 'Login') {
    
    loginForm.addEventListener('submit', function(e) {
        e.preventDefault();
        
        const email = loginEmail.value.trim();
        const password = loginPassword.value.trim();
        const messagePara = loginForm.querySelector('.error-text');

        if (!email || !password) {
            messagePara.textContent = 'გთხოვთ შეავსოთ ორივე ველი!';
            return;
        }

        let users = JSON.parse(localStorage.getItem('users')) || [];
        const authenticatedUser = users.find(user => user.email === email && user.password === password);

        if (authenticatedUser) {
            messagePara.textContent = '';
            localStorage.setItem('currentUser', JSON.stringify(authenticatedUser));
            
            alert('სისტემაში შესვლა წარმატებულია!');
            window.location.href = 'Home.html'; // შეცვლილია: გადაგიყვანს Home.html-ზე
        } else {
            messagePara.textContent = 'იმეილი ან პაროლი არასწორია!';
        }
    });
}


// 3.  (Home Page)

const navLoginBtn = document.getElementById('login'); 
const navRegisterBtn = document.getElementById('register'); 

if (navLoginBtn) {
    const currentUser = JSON.parse(localStorage.getItem('currentUser'));

    if (currentUser) {
        // თუ იუზერი სისტემაშია
        navLoginBtn.textContent = 'Log Out';
        
        if (navRegisterBtn) {
            navRegisterBtn.style.display = 'none'; 
        }
        
        // Log Out დაჭერის ლოგიკა
        navLoginBtn.addEventListener('click', function() {
            localStorage.removeItem('currentUser'); 
            alert('თქვენ გამოხვედით სისტემიდან!');
            window.location.reload(); 
        });
    } else {
        // თუ იუზერი არ არის სისტემაში - ღილაკების გადამისამართება
        navLoginBtn.addEventListener('click', function() {
            window.location.href = 'login.html';
        });

        if (navRegisterBtn) {
            navRegisterBtn.addEventListener('click', function() {
                window.location.href = 'register.html';
            });
        }
    }
}
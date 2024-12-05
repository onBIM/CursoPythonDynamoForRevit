import { initializeApp } from 'https://www.gstatic.com/firebasejs/10.9.0/firebase-app.js'
import {
    getAuth,
    GoogleAuthProvider,
    sendPasswordResetEmail,
    signInWithEmailAndPassword,
    onAuthStateChanged,
    signOut
} from 'https://www.gstatic.com/firebasejs/10.9.0/firebase-auth.js'

// Firebase Configuration
const firebaseConfig = {
    apiKey: "AIzaSyAAp5kC1AMZjk3DUIWsvo5UV3IfBiNpxk0",
    authDomain: "hostingcursopython.firebaseapp.com",
    projectId: "hostingcursopython",
    appId: "1:91314052559:web:22347a8436cae3c03fc6ba",
    measurementId: "G-H625JFEZWQ"
};

// Initialize Firebase
const app = initializeApp(firebaseConfig);
const auth = getAuth(app);

// Select elements
const authWrapper = document.getElementById("authWrapper");
const contentWrapper = document.getElementById("contentWrapper");
const contentIframe = document.getElementById("contentIframe");

// Function to show login form
const showLoginForm = () => {
    authWrapper.innerHTML = `
    <div class="grid grid-cols-1">
    <div class="flex justify-center">
    <img src="logo.png" width="200px">
</div>
<div>
    <form id="loginForm" class="space-y-4">
      <div>
        <label for="email" class="block text-sm font-medium text-gray-700">Email</label>
        <input
          type="email"
          id="email"
          class="w-full mt-1 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500"
          placeholder="Enter your email"
          required
        >
      </div>
      <div>
        <label for="password" class="block text-sm font-medium text-gray-700">Password</label>
        <input
          type="password"
          id="password"
          class="w-full mt-1 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-blue-500 focus:border-blue-500"
          placeholder="Enter your password"
          required
        >
      </div>
      <button
        type="submit"
        class="w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:ring focus:ring-blue-300"
      >
        Login
      </button>

    </form>
    <button
    id="resetPasswordBtn"
    class="w-full mt-4 bg-gray-500 text-white py-2 rounded-md hover:bg-gray-600 focus:outline-none focus:ring focus:ring-gray-300"
    >
    Reset Password
  </button>
    <button
      id="googleLoginBtn"
      class="hidden w-full bg-blue-500 text-white py-2 rounded-md hover:bg-blue-600 focus:outline-none focus:ring focus:ring-blue-300 mt-2"
    >
      Login with Google
    </button>
    <p id="errorMessage" class="text-red-500 text-sm mt-4 hidden"></p>
</div>
</div>
    

  `;

    // Handle login
    const loginForm = document.getElementById("loginForm");
    const errorMessage = document.getElementById("errorMessage");
    const handlePasswordReset = () => {
        const email = prompt("Enter your email to reset your password:");

        if (!email) {
            alert("Email is required to reset the password.");
            return;
        }

        sendPasswordResetEmail(auth, email)
            .then(() => {
                alert(`Password reset email sent to ${email}. Check your inbox.`);
            })
            .catch((error) => {
                console.error("Error resetting password:", error.message);

                if (error.code === "auth/user-not-found") {
                    alert("No account found with this email.");
                } else if (error.code === "auth/invalid-email") {
                    alert("The email address is invalid.");
                } else {
                    alert("An error occurred. Please try again later.");
                }
            });
    };
    document.getElementById("resetPasswordBtn").addEventListener("click", handlePasswordReset);

    loginForm.addEventListener("submit", async (e) => {
        e.preventDefault();
        const email = document.getElementById("email").value;
        const password = document.getElementById("password").value;

        try {
            await signInWithEmailAndPassword(auth, email, password);
        } catch (error) {
            errorMessage.textContent = error.message;
            errorMessage.classList.remove("hidden");
        }
    });
    const googleLoginBtn = document.getElementById("googleLoginBtn");
    googleLoginBtn.addEventListener("click", async () => {
        try {
            await signInWithPopup(auth, provider);
        } catch (error) {
            const errorMessage = document.getElementById("errorMessage");
            errorMessage.textContent = error.message;
            errorMessage.classList.remove("hidden");
        }
    });
};




// Function to show the public content
const showContent = () => {
    authWrapper.classList.add("hidden");
    contentWrapper.classList.remove("hidden");

    const logoutBtn = document.getElementById("logoutBtn");
    logoutBtn.addEventListener("click", async () => {
        await signOut(auth);
    });
};

// Listen for authentication state changes
onAuthStateChanged(auth, (user) => {
    if (user) {
        // User is authenticated, show the content
        showContent();
    } else {
        // User is not authenticated, show login form
        contentWrapper.classList.add("hidden");
        authWrapper.classList.remove("hidden");
        showLoginForm();
    }
});

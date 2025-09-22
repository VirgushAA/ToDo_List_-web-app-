
document.addEventListener("DOMContentLoaded", () => {
    const notesForm = document.getElementById("note-form");
    const signUpForm = document.getElementById("sign-up-form");
    const loginForm = document.getElementById("login-form");
    const notesList = document.getElementById("notes-list");

    notesForm.addEventListener("submit", (e) => {
        e.preventDefault();

        const textarea = notesForm.querySelector("textarea");
        const noteText = textarea.value.trim();

        if (noteText) {
            const noteItem = document.createElement("div");
            noteItem.className = 'note';
            noteItem.textContent = noteText;
            notesList.appendChild(noteItem);
            textarea.value = "";
            textarea.style.height = "auto";
        }
    });

    signUpForm.addEventListener("submit", (e) => {
        e.preventDefault();
        pass;
    })

    document.getElementById('switch-to-login').addEventListener('click', () => {
        document.getElementById('sign-up-area').style.display = 'none';
        document.getElementById('login-area').style.display = 'block';
    })

    loginForm.addEventListener("submit", (e)=> {
        e.preventDefault();
        pass;
    })

    document.getElementById("switch-to-signup").addEventListener("click", () => {
        document.getElementById("login-area").style.display = "none";
        document.getElementById("sign-up-area").style.display = "block";
    });

    document.querySelectorAll("textarea").forEach((ta) => {
        ta.addEventListener("input", () => {
            ta.style.height = "auto";
            ta.style.height = ta.scrollHeight + "px";
        })
    })
})

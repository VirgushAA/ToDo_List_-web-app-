
document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("note-form");
    const notesList = document.getElementById("notes-list");

    form.addEventListener("submit", (e) => {
        e.preventDefault();

        const textarea = form.querySelector("textarea");
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

    document.querySelectorAll("textarea").forEach((ta) => {
        ta.addEventListener("input", () => {
            ta.style.height = "auto";
            ta.style.height = ta.scrollHeight + "px";
        })
    })
})

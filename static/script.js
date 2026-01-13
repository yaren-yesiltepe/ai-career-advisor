let selectedInterests = [];
let selectedSkills = [];

function toggle(button) {
    button.classList.toggle("active");

    const value = button.innerText;
    const parentId = button.parentElement.id;

    let list = parentId === "interests" ? selectedInterests : selectedSkills;

    if (button.classList.contains("active")) {
        if (list.length >= 5) {
            button.classList.remove("active");
            alert("En fazla 5 seçim yapabilirsin.");
            return;
        }
        list.push(value);
    } else {
        list = list.filter(item => item !== value);
    }

    if (parentId === "interests") {
        selectedInterests = list;
    } else {
        selectedSkills = list;
    }
}

function analyzeCareer() {
    if (selectedInterests.length === 0 && selectedSkills.length === 0) {
        alert("En az bir ilgi alanı veya beceri seçmelisin.");
        return;
    }

    fetch("/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            interests: selectedInterests,
            skills: selectedSkills
        })
    })
    .then(response => response.json())
    .then(data => {
        renderResults(data);
    });
}

function renderResults(results) {
    const resultDiv = document.getElementById("result");
    resultDiv.innerHTML = "";

    results.forEach(item => {
        const reasons = [];

        if (item.reason.interests.length > 0) {
            reasons.push(
                "İlgi alanların: " + item.reason.interests.join(", ")
            );
        }

        if (item.reason.skills.length > 0) {
            reasons.push(
                "Becerilerin: " + item.reason.skills.join(", ")
            );
        }

        resultDiv.innerHTML += `
            <div class="card">
                <h2>${item.career} – %${item.score} Uyum</h2>
                <div class="progress">
                    <div class="progress-bar" style="width:${item.score}%"></div>
                </div>
                <p>${item.description}</p>
                <p class="reason">${reasons.join(" • ")}</p>
            </div>
        `;
    });
}
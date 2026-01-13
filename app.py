from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

careers = {
    "Frontend Developer": {
        "interests": ["Dizayn", "Yaratıcılık", "Teknoloji"],
        "skills": ["HTML", "CSS", "JavaScript"],
        "description": "Web sitelerinin kullanıcı arayüzlerini geliştiren yazılımcı."
    },
    "UI/UX Designer": {
        "interests": ["Dizayn", "Yaratıcılık"],
        "skills": ["Figma", "Design Thinking"],
        "description": "Kullanıcı deneyimi ve arayüz tasarımı yapan uzman."
    },
    "Product Designer": {
        "interests": ["Dizayn", "Yaratıcılık", "Problem Çözme"],
        "skills": ["Figma", "UX Research"],
        "description": "Dijital ürünlerin uçtan uca tasarımını yapan tasarımcı."
    },
    "Data Analyst": {
        "interests": ["Analiz", "Sayılar"],
        "skills": ["SQL", "Excel", "Python"],
        "description": "Verileri analiz ederek iş kararlarını destekler."
    },
    "Business Analyst": {
        "interests": ["Analiz", "Problem Çözme"],
        "skills": ["Excel", "SQL"],
        "description": "İş süreçlerini analiz eden ve iyileştiren analist."
    },
    "AI Developer": {
        "interests": ["Teknoloji", "Problem Çözme"],
        "skills": ["Python"],
        "description": "Yapay zeka ve akıllı sistemler geliştiren mühendis."
    },
    "Machine Learning Engineer": {
        "interests": ["Teknoloji", "Analiz"],
        "skills": ["Python"],
        "description": "Makine öğrenmesi modelleri geliştiren mühendis."
    },
    "QA Engineer": {
        "interests": ["Analiz", "Problem Çözme"],
        "skills": ["Testing"],
        "description": "Yazılım kalitesini ve hataları test eden mühendis."
    },
    "Product Manager": {
        "interests": ["Problem Çözme", "Teknoloji"],
        "skills": ["Communication"],
        "description": "Ürün vizyonunu belirleyen ve ekipleri yöneten kişi."
    },
    "Digital Marketing Specialist": {
        "interests": ["Yaratıcılık", "Analiz"],
        "skills": ["SEO", "Content"],
        "description": "Dijital kanallarda pazarlama stratejileri yürüten uzman."
    }
}



@app.route("/")
def home():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    interests = data.get("interests", [])
    skills = data.get("skills", [])

    results = []

    for career, info in careers.items():
        score = 0

        matched_interests = [i for i in interests if i in info["interests"]]
        matched_skills = [s for s in skills if s in info["skills"]]

        if matched_interests:
            score += 60

        if matched_skills:
            score += 40

        if score > 0:
            results.append({
                "career": career,
                "score": score,
                "description": info["description"],
                "reason": {
                    "interests": matched_interests,
                    "skills": matched_skills
                }
            })

    results = sorted(results, key=lambda x: x["score"], reverse=True)[:2]

    return jsonify(results)


if __name__ == "__main__":
    print("FLASK BAŞLIYOR...")
    app.run(debug=True)
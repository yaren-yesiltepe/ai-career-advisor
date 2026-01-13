# 🤖 AI Career Advisor

AI Career Advisor is a **rule-based AI simulation** that suggests suitable career paths
based on a user's **interests** and **skills**.

Unlike simple form-based applications, this project focuses on
**decision-making logic** and **explainable AI principles**.

---

## 🎯 Project Purpose

The main goals of this project are:

- To prioritize **personal interests** over skills in career recommendations
- To build a **transparent and explainable** decision-making system
- To clearly answer the question: *“Why did the AI recommend this career?”*
- To create a realistic, portfolio-ready AI project

---

## 🧠 AI Logic (How It Works)

The system is fully **rule-based**.

### 🔹 Decision Weights

- Interest match → **60%**
- Skill match → **40%**

> The idea is simple:
> even if someone has strong technical skills,
> long-term success is unlikely without genuine interest.

### 🔹 Process Flow

1. The user selects their interests and skills
2. The backend analyzes matches for each career
3. A score (0–100) is calculated
4. The **top 2 matching careers** are recommended
5. Each recommendation includes:
   - Compatibility percentage
   - Explanation
   - Reasoning behind the suggestion

---

## 🧩 Features

- Interest & skill-based career analysis
- Percentage-based compatibility scoring
- Explainable AI decisions
- Modern frontend (HTML, CSS, JavaScript)
- Flask-based backend
- Clean and extensible project structure

---

## 🛠 Technologies Used

- **Python**
- **Flask**
- **HTML**
- **CSS**
- **JavaScript**

---

## ▶️ How to Run the Project

### 1️⃣ Clone the repository

```bash
git clone https://github.com/yaren-yesiltepe/ai-career-advisor.git
cd ai-career-advisor

import customtkinter as ctk
from tkinter import filedialog

# -------------------- App Settings --------------------
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

# -------------------- Main Window --------------------
app = ctk.CTk()
app.configure(fg_color="#C4C1C1")
app.title("Exam Question Difficulty Analyzer")
app.geometry("1000x650")
app.resizable(False, False)


# -------------------- FUNCTION --------------------
def start_analysis():

    window = ctk.CTkToplevel(app)
    window.title("Question Analyzer")
    window.geometry("750x600")
    window.configure(fg_color="#CEEAF7")

    # ---------------- TITLE ----------------
    title = ctk.CTkLabel(
        window,
        text="Enter Your Exam Questions",
        font=("Segoe UI", 30, "bold"),
        text_color="#1E3A8A",
    )
    title.pack(pady=20)

    # ---------------- TEXTBOX ----------------
    textbox = ctk.CTkTextbox(
        window,
        width=650,
        height=80,
        fg_color="white",
        text_color="black",
        border_color="#3B82F6",
        border_width=2,
    )
    textbox.pack(pady=10)

    # ---------------- SUBJECT ----------------
    subject_label = ctk.CTkLabel(
        window,
        text="Select Subject",
        font=("Segoe UI", 16, "bold"),
        text_color="#1E3A8A"
    )
    subject_label.pack(pady=(10, 5))

    subject_menu = ctk.CTkComboBox(
        window,
        values=["Computer Science", "Mathematics", "Physics", "Chemistry", "English"],
        width=250
    )
    subject_menu.pack(pady=5)

    # ---------------- TYPE ----------------
    type_label = ctk.CTkLabel(
        window,
        text="Question Type",
        font=("Segoe UI", 16, "bold"),
        text_color="#1E3A8A"
    )
    type_label.pack(pady=(10, 5))

    type_menu = ctk.CTkComboBox(
        window,
        values=["MCQ", "Short Question", "Long Question"],
        width=250
    )
    type_menu.pack(pady=5)

    # ---------------- RESULT ----------------
    result = ctk.CTkLabel(
        window,
        text="Prediction will appear here",
        font=("Segoe UI", 20, "bold"),
        text_color="#16A34A"
    )
    result.pack(pady=15)

    # ---------------- WORD COUNT ----------------
    word_label = ctk.CTkLabel(
        window,
        text="",
        font=("Segoe UI", 16, "bold"),
        text_color="#1E3A8A",
    )
    word_label.pack(pady=5)

    # ---------------- SUMMARY ----------------
    easy_label = ctk.CTkLabel(
        window,
        text="",
        font=("Segoe UI", 16, "bold"),
        text_color="#16A34A"
    )
    easy_label.pack()

    medium_label = ctk.CTkLabel(
        window,
        text="",
        font=("Segoe UI", 16, "bold"),
        text_color="#F59E0B"
    )
    medium_label.pack()

    hard_label = ctk.CTkLabel(
        window,
        text="",
        font=("Segoe UI", 16, "bold"),
        text_color="#EF4444"
    )
    hard_label.pack()

    # ---------------- ANALYZE FUNCTION ----------------
    def analyze():
        text = textbox.get("1.0", "end").strip()

        if text == "":
            result.configure(text="Please enter questions.")
            return

        questions = text.split("\n")

        easy = 0
        medium = 0
        hard = 0
        total_words = 0

        for q in questions:
            if q.strip() == "":
                continue

            words = len(q.split())
            total_words += words

            if words <= 8:
                easy += 1
            elif words <= 18:
                medium += 1
            else:
                hard += 1

        confidence = 90 - (total_words // max(1, len(questions)))
        confidence = max(60, min(confidence, 95))

        result.configure(
            text=f"Analysis Completed ✔️ | Confidence: {confidence}%"
        )

        word_label.configure(
            text=f"Total Questions: {len(questions)} | Total Words: {total_words}"
        )

        easy_label.configure(text=f"🟢 Easy: {easy}")
        medium_label.configure(text=f"🟡 Medium: {medium}")
        hard_label.configure(text=f"🔴 Hard: {hard}")

    # ---------------- BUTTONS ----------------
    analyze_button = ctk.CTkButton(
        window,
        text="🔍 Analyze",
        width=180,
        height=40,
        font=("Segoe UI", 16, "bold"),
        fg_color="#06B6D4",
        hover_color="#0891B2",
        corner_radius=12,
        command=analyze
    )
    analyze_button.pack(pady=10)

    clear_button = ctk.CTkButton(
        window,
        text="🧹 Clear",
        width=180,
        height=40,
        font=("Segoe UI", 16, "bold"),
        fg_color="#E7AB45",
        hover_color="#F7A84D",
        corner_radius=12,

        command=lambda: (
            textbox.delete("1.0", "end"),
            result.configure(text="Prediction will appear here"),
            word_label.configure(text=""),
            easy_label.configure(text=""),
            medium_label.configure(text=""),
            hard_label.configure(text="")
        )
    )
    clear_button.pack(pady=10)


# -------------------- MAIN SCREEN --------------------
title = ctk.CTkLabel(
    app,
    text="📚 Exam Question Difficulty Analyzer",
    font=("Segoe UI", 34, "bold"),
    text_color="#042C3E",
)
title.pack(pady=30)

description = ctk.CTkLabel(
    app,
    text="Analyze exam questions and predict their difficulty level.",
    font=("Segoe UI", 22, "bold"),
    text_color="#096F9B",
)
description.pack(pady=10)

start_button = ctk.CTkButton(
    app,
    text="Start Analysis",
    width=240,
    height=50,
    font=("Segoe UI", 20, "bold"),
    command=start_analysis
)
start_button.pack(pady=40)

app.mainloop()
# General Knowledge Quiz Application
# Step 1: Questions and Answers
questions = [
    {"question": "What is the capital of india?", "answer": "delhi"},
    {"question": "Which planet iour planet name?", "answer": "earth"},
    {"question": "What is the largest mountain?", "answer": "mount everest"},
    {"question": "Who wrote 'National anthem'?", "answer": "ravindranath tagore "},
    {"question": "What is the full form CSE?", "answer": "computer science and engineering"}
]

# Step 2: Initialize Score
score = 0

# Step 3: Start Quiz
print("🧠 Welcome to the General Knowledge Quiz!")
print("----------------------------------------\n")

for i, q in enumerate(questions, 1):
    user_answer = input(f"Q{i}: {q['question']} ").strip().lower()
    
    if user_answer == q["answer"]:
        print("✅ Correct!")
        score += 1
    else:
        print(f"❌ Incorrect! The correct answer is: {q['answer'].title()}")
    
    print(f"Current Score: {score}/{i}\n")

# Step 4: End of Quiz
print("🎉 Quiz Completed!")
print(f"Your Final Score: {score}/{len(questions)}")

# Step 5: Feedback Message
if score == len(questions):
    print("🏆 Excellent! You got all questions right!")
elif score >= len(questions) * 0.6:
    print("👍 Good job! You passed the quiz.")
else:
    print("📘 Keep practicing. You can do better next time!")

# Step 6: Testing
# Try replacing questions or adding more to test the application.

🍳 ChefGPT

ChefGPT is a full-stack web application that generates recipes based on ingredients provided by the user. Instead of searching endlessly for meals, users simply enter what they already have — and ChefGPT suggests a complete recipe.

🚀 Features

🥕 Ingredient-based recipe generation

📋 Step-by-step cooking instructions

🔥 Meal planning assistance

💾 Firebase backend integration

🌐 Responsive web interface

👤 User authentication (optional, if implemented)

📱 Clean and intuitive UI

🛠️ Tech Stack

Frontend

HTML

CSS

JavaScript

Backend / Database

Firebase (Authentication, Firestore, Hosting)

Other Tools

Git & GitHub

Firebase CLI

🧠 How It Works

The user enters available ingredients into an input field.

The application processes the ingredients.

A matching recipe is generated and displayed.

(Optional) The recipe can be saved to the user's account in Firebase.

📂 Project Structure
ChefGPT/
│
├── index.html
├── style.css
├── script.js
├── firebase-config.js
└── README.md

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/yourusername/chefgpt.git
cd chefgpt

2️⃣ Install Firebase CLI (if needed)
npm install -g firebase-tools

3️⃣ Initialize Firebase
firebase login
firebase init


Select:

Hosting

Firestore (if used)

Authentication (if used)

4️⃣ Run Locally

You can simply open index.html in your browser
OR use Firebase hosting:

firebase serve

🔐 Firebase Configuration

Create a firebase-config.js file:

const firebaseConfig = {
  apiKey: "YOUR_API_KEY",
  authDomain: "YOUR_PROJECT_ID.firebaseapp.com",
  projectId: "YOUR_PROJECT_ID",
  storageBucket: "YOUR_PROJECT_ID.appspot.com",
  messagingSenderId: "XXXX",
  appId: "XXXX"
};

firebase.initializeApp(firebaseConfig);

🎯 Future Improvements

🍽️ Nutrition tracking (calories, macros)

🧾 Grocery list generator

🤖 AI-powered recipe suggestions

🗂️ Save favorite meals

🌎 Cuisine filters

📊 Meal prep weekly planner

🧪 Example Use Case

Input:

Chicken, rice, broccoli, garlic


Output:

Garlic Chicken Stir Fry with Rice
- Step 1: Season and cook chicken...
- Step 2: Sauté broccoli and garlic...
- Step 3: Combine and serve over rice...

📌 Why ChefGPT?

ChefGPT solves the common problem of:

Wasting ingredients

Not knowing what to cook

Spending too much time searching for recipes

It simplifies meal planning into a quick and efficient experience.

👨‍💻 Authors

Ana Moron Cervantes
Opeoluwa Orisadahunsi
Favour Aloziem
Nicholas Watson
Jason Vo
RJ Cortez
Omieibi Harcourt


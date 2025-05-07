# 🧪 A/B Testing - Product Display using Streamlit

This project simulates A/B testing of two product page layouts on an e-commerce platform. The goal is to determine which version performs better in terms of user engagement, by tracking actions like **view** and **add to cart**.

---

## 🎯 Project Objective

In real-world platforms changing the UI/UX of a product listing page can significantly impact conversion rates. This project helps test that using two different display versions of the same product and tracking user behavior.

We simulate:

- **Version A**: Clean and minimal layout with a small image.
- **Version B**: Enhanced layout with a large image and visible product reviews.

Each user is randomly shown either version A or B, and their interactions are logged.

---

## 📦 Features

✅ Random assignment of users to Version A or B  
✅ Product image and layout changes based on version  
✅ Button to simulate user adding product to cart  
✅ Logging of interaction (timestamp, user ID, version, action)  
✅ Data saved to CSV for further analysis

---

## 🛠️ Technologies Used

| Tool        | Purpose                          |
|-------------|----------------------------------|
| Python      | Core programming logic           |
| Streamlit   | Web UI for displaying versions   |
| Pandas      | Data handling and CSV operations |
| CSV         | Storing user interaction logs    |

---

## 💻 What Happens in the App
The app assigns a random user ID.

Randomly selects Version A or B.

Shows corresponding product image and layout.

You can simulate an action: either just viewing or clicking "Add to Cart".

The action gets logged in data.csv.

![Output](https://github.com/AnanyaS-03/ML/blob/main/AB%20Testing%20on%20product%20display/Screenshot%202025-05-06%20151811.png?raw=true)


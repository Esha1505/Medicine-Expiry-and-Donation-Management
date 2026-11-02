# 💊 Medicine Expiry & Donation Management System

A simple Python-based project designed to manage medicine inventory, keep track of expiry dates, and make medicine donations easier to manage.

## 📌 About the Project

Medicines are often wasted because people forget to check their expiry dates or don't know how to manage unused stock properly.

I created this project to solve this problem in a simple way. The **Medicine Expiry & Donation Management System** helps maintain medicine records, monitor expiry dates, manage available stock, and keep track of medicine donations and requests.

The main idea behind this project is to reduce medicine wastage and encourage better medicine inventory management.

## ✨ Features

- **Add Medicine:** Add new medicines with details such as ID, name, batch number, quantity, price, manufacturing date, expiry date, and donor company.
- **View Medicines:** Display all available medicine records.
- **Search Medicine:** Search for a medicine using its name or ID.
- **Check Expiry:** Check medicine expiry dates and identify medicines that are expired, expiring soon, or still safe.
- **Donate Medicine:** Manage medicine donations and update the available stock.
- **Request Medicine:** Record medicine requests from companies or organizations.
- **View Requests:** View all previously recorded medicine requests.

## 🛠️ Technologies Used

- **Python** – Main programming language.
- **JSON** – To store and manage medicine, donation, and request records.
- **Datetime Module** – To handle manufacturing dates, expiry dates, and expiry calculations.
- **OOP (Object-Oriented Programming)** – To organize the program using classes and methods.
- **Exception Handling** – To handle invalid inputs and file-related errors.

## 📂 Project Structure

```text
Medicine-Expiry-Donation-Manager/
│
├── main.py
├── medicine.json
├── donation.json
├── request_med.json
└── README.md
```

*Note: JSON files are created when records are saved, so they may not exist when the project is first downloaded.*

## ▶️ How to Run the Project

**Step 1:** Clone the repository.

```bash
git clone <your-repository-link>
```

**Step 2:** Open the project folder.

```bash
cd Medicine-Expiry-Donation-Manager
```

**Step 3:** Run the Python program.

```bash
python main.py
```

**Step 4:** Select an option from the menu and start managing medicine records.

## 📚 What I Learned

While developing this project, I got practical experience with:

- Working with Python classes and objects.
- Reading and writing data using JSON files.
- Handling dates and calculating medicine expiry.
- Implementing searching and sorting operations.
- Using exception handling to manage errors.
- Applying conditional statements and loops to solve real-world problems.
- Developing logical thinking through practical implementation.

## 🚀 Future Improvements

I would like to improve this project further by adding:

- Medicine stock update and delete functionality.
- Complete donation history.
- Automatic notifications for medicines approaching expiry.
- Medicine request matching with available inventory.
- A graphical user interface for easier usage.
- Database integration using MySQL.

## 👩‍💻 Developed By

**Esha Patil**

A Python-based academic project developed as part of my learning journey in programming and software development.

---

⭐ *This project is a small step towards using technology to solve everyday problems and reduce unnecessary medicine wastage.*

**Note:** This project is intended for educational and inventory-management purposes. Medicine donation and redistribution must follow applicable regulations and appropriate safety checks. Expired medicines should never be redistributed.

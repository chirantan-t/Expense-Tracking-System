import tkinter as tk
from tkinter import messagebox
from tkinter import ttk


class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Login Page")
        self.root.geometry("500x450")  # Increased window size for better spacing

        # Set modern background color and style inspired by Canva designs
        self.root.configure(bg='#f0f4f8')  # Light neutral background

        # Store user data and expenses
        self.users = {}
        self.current_user = None
        self.expenses = {}

        # Apply custom styling for ttk widgets
        style = ttk.Style()
        style.theme_use('clam')
        style.configure("TButton", background="#28a745", foreground="white", font=('Helvetica', 14, 'bold'), padding=10)
        style.configure("TLabel", background="#f0f4f8", foreground="#333", font=('Helvetica', 14, 'bold italic'))
        style.configure("TEntry", font=('Helvetica', 12), padding=5)

        # Initialize Login Page
        self.show_login_page()

    # Login Page
    def show_login_page(self):
        self.clear_window()

        tk.Label(self.root, text="Login", font=('Helvetica', 28, 'bold italic'), bg="#f0f4f8", fg="#2c3e50").pack(pady=20)

        tk.Label(self.root, text="Username", font=('Helvetica', 14), bg="#f0f4f8", fg="#34495e").pack(pady=5)
        self.username_entry = ttk.Entry(self.root)
        self.username_entry.pack(ipady=8, padx=10)

        tk.Label(self.root, text="Password", font=('Helvetica', 14), bg="#f0f4f8", fg="#34495e").pack(pady=5)
        self.password_entry = ttk.Entry(self.root, show="*")
        self.password_entry.pack(ipady=8, padx=10)

        ttk.Button(self.root, text="Login", command=self.login).pack(pady=20)
        ttk.Button(self.root, text="Register", command=self.show_register_page).pack(pady=10)

    # Registration Page
    def show_register_page(self):
        self.clear_window()

        tk.Label(self.root, text="Registration", font=('Helvetica', 28, 'bold italic'), bg="#f0f4f8", fg="#2c3e50").pack(pady=20)

        tk.Label(self.root, text="Username", font=('Helvetica', 14), bg="#f0f4f8", fg="#34495e").pack(pady=5)
        self.reg_username_entry = ttk.Entry(self.root)
        self.reg_username_entry.pack(ipady=8, padx=10)

        tk.Label(self.root, text="Email ID", font=('Helvetica', 14), bg="#f0f4f8", fg="#34495e").pack(pady=5)
        self.reg_email_entry = ttk.Entry(self.root)
        self.reg_email_entry.pack(ipady=8, padx=10)

        tk.Label(self.root, text="Password", font=('Helvetica', 14), bg="#f0f4f8", fg="#34495e").pack(pady=5)
        self.reg_password_entry = ttk.Entry(self.root, show="*")
        self.reg_password_entry.pack(ipady=8, padx=10)

        tk.Label(self.root, text="Total Salary", font=('Helvetica', 14), bg="#f0f4f8", fg="#34495e").pack(pady=5)
        self.reg_salary_entry = ttk.Entry(self.root)
        self.reg_salary_entry.pack(ipady=8, padx=10)

        ttk.Button(self.root, text="Register", command=self.register).pack(pady=20)
        ttk.Button(self.root, text="Back to Login", command=self.show_login_page).pack(pady=10)

    # Dashboard Page
    def show_dashboard(self):
        self.clear_window()
        self.root.title("Dashboard")

        tk.Label(self.root, text=f"Welcome, {self.current_user['username']}", font=('Helvetica', 24, 'bold italic'), bg="#f0f4f8", fg="#2c3e50").pack(pady=20)

        ttk.Button(self.root, text="Add Expense", command=self.show_add_expense_page).pack(pady=15)
        ttk.Button(self.root, text="View Expenses", command=self.show_view_expenses_page).pack(pady=10)
        ttk.Button(self.root, text="View Salary", command=self.view_salary).pack(pady=10)
        ttk.Button(self.root, text="Logout", command=self.logout).pack(pady=10)

    # Add Expense Page
    def show_add_expense_page(self):
        self.clear_window()
        self.root.title("Add Expense")

        tk.Label(self.root, text="Add Expense", font=('Helvetica', 24, 'bold italic'), bg="#f0f4f8", fg="#2c3e50").pack(pady=20)

        tk.Label(self.root, text="Expense Name", font=('Helvetica', 14), bg="#f0f4f8", fg="#34495e").pack(pady=5)
        self.expense_name_entry = ttk.Entry(self.root)
        self.expense_name_entry.pack(ipady=8, padx=10)

        tk.Label(self.root, text="Expense Cost", font=('Helvetica', 14), bg="#f0f4f8", fg="#34495e").pack(pady=5)
        self.expense_cost_entry = ttk.Entry(self.root)
        self.expense_cost_entry.pack(ipady=8, padx=10)

        ttk.Button(self.root, text="Add Expense", command=self.add_expense).pack(pady=20)
        ttk.Button(self.root, text="Back to Dashboard", command=self.show_dashboard).pack(pady=10)

    # View Expenses Page
    def show_view_expenses_page(self):
        self.clear_window()
        self.root.title("View Expenses")

        tk.Label(self.root, text="Your Expenses", font=('Helvetica', 24, 'bold italic'), bg="#f0f4f8", fg="#2c3e50").pack(pady=20)

        tree = ttk.Treeview(self.root, columns=('Expense', 'Cost'), show='headings')
        tree.heading('Expense', text='Expense')
        tree.heading('Cost', text='Cost')
        tree.pack(fill=tk.BOTH, expand=True)

        # Insert expenses into the table
        for expense, cost in self.expenses.get(self.current_user['username'], []):
            tree.insert("", tk.END, values=(expense, cost))

        ttk.Button(self.root, text="Back to Dashboard", command=self.show_dashboard).pack(pady=20)

    # Functions for user interaction
    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in self.users and self.users[username]['password'] == password:
            self.current_user = self.users[username]
            self.show_dashboard()
        else:
            messagebox.showerror("Error", "Invalid credentials!")

    def register(self):
        username = self.reg_username_entry.get()
        email = self.reg_email_entry.get()
        password = self.reg_password_entry.get()
        salary = self.reg_salary_entry.get()

        if username in self.users:
            messagebox.showerror("Error", "Username already exists!")
        else:
            self.users[username] = {'username': username, 'email': email, 'password': password, 'salary': float(salary)}
            self.expenses[username] = []
            messagebox.showinfo("Success", "Registration successful!")
            self.show_login_page()

    def add_expense(self):
        expense_name = self.expense_name_entry.get()
        expense_cost = float(self.expense_cost_entry.get())

        self.expenses[self.current_user['username']].append((expense_name, expense_cost))
        messagebox.showinfo("Success", "Expense added!")
        self.show_dashboard()

    def view_salary(self):
        total_expenses = sum(cost for _, cost in self.expenses.get(self.current_user['username'], []))
        salary_left = self.current_user['salary'] - total_expenses
        messagebox.showinfo("Salary", f"Your remaining salary is: Rs.{salary_left:.2f}")

    def logout(self):
        self.current_user = None
        self.show_login_page()

    # Helper function to clear the window
    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()


# Run the app
root = tk.Tk()
app = ExpenseTrackerApp(root)
root.mainloop()

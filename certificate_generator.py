from reportlab.pdfgen import canvas
import tkinter as tk
from tkinter import messagebox

def generate_certificate(name, course, date):
    filename = f"{name.replace(' ', '_')}_certificate.pdf"
    c = canvas.Canvas(filename)
    c.setFont("Helvetica-Bold", 36)
    c.drawString(100, 700, "Certificate of Completion")
    
    c.setFont("Helvetica", 24)
    c.drawString(100, 600, f"This is to certify that")
    c.drawString(100, 550, name)
    c.drawString(100, 500, f"has Successfully completed the course:")
    c.drawString(100, 450, course)
    c.drawString(100, 400, f"Date: {date}")
    
    c.save()
    print(f"Certificate saved as: Bakka_Alfa")

def submit_details():
    name = entry_name.get()
    course = entry_course.get()
    date = entry_date.get()
    generate_certificate(name, course, date)
    messagebox.showinfo("Success", "Certificate generated successfully!")

app = tk.Tk()
app.title("Certificate Generator")

tk.Label(app, text="Name:").grid(row=0)
tk.Label(app, text="Course:").grid(row=1)
tk.Label(app, text="Date:").grid(row=2)

entry_name = tk.Entry(app)
entry_course = tk.Entry(app)
entry_date = tk.Entry(app)

entry_name.grid(row=0, column=1)
entry_course.grid(row=1, column=1)
entry_date.grid(row=2, column=1)

tk.Button(app, text="Generate Certificate", command=submit_details).grid(row=3, columnspan=2)

app.mainloop()

import tkinter as tk
from tkinter import messagebox

class ContactManager:
    def __init__(self, filename="friendsContact.txt"):
        self.filename = filename

    def add_contact(self, name, phone):
        with open(self.filename, "a") as f:
            f.write(f"{name},{phone}\n")

    def read_contacts(self):
        try:
            with open(self.filename, "r") as f:
                return [line.strip().split(",") for line in f.readlines()]
        except FileNotFoundError:
            return []

    def update_contact(self, name, new_phone):
        contacts = self.read_contacts()
        updated = False

        with open(self.filename, "w") as f:
            for contact_name, contact_phone in contacts:
                if contact_name == name:
                    f.write(f"{name},{new_phone}\n")
                    updated = True
                else:
                    f.write(f"{contact_name},{contact_phone}\n")

        return updated

    def delete_contact(self, name):
        contacts = self.read_contacts()
        deleted = False

        with open(self.filename, "w") as f:
            for contact_name, contact_phone in contacts:
                if contact_name != name:
                    f.write(f"{contact_name},{contact_phone}\n")
                else:
                    deleted = True

        return deleted

class ContactApp:
    def __init__(self, root):
        self.manager = ContactManager()
        self.root = root
        self.root.title("Friends Contact Manager")
        self.root.geometry("400x440")

        # ---------- ENTRY FIELDS ----------
        tk.Label(root, text="Name:").pack()
        self.entry_name = tk.Entry(root, width=30)
        self.entry_name.pack()

        tk.Label(root, text="Phone:").pack()
        self.entry_phone = tk.Entry(root, width=30)
        self.entry_phone.pack()

        # ---------- BUTTONS ----------
        tk.Button(root, text="Add Contact", width=20, command=self.add_contact).pack(pady=5)
        tk.Button(root, text="View Contacts", width=20, command=self.view_contacts).pack(pady=5)
        tk.Button(root, text="Update Contact", width=20, command=self.update_contact).pack(pady=5)
        tk.Button(root, text="Delete Contact", width=20, command=self.delete_contact).pack(pady=5)

        # ---------- DISPLAY AREA ----------
        tk.Label(root, text="Contacts:").pack()
        self.text_area = tk.Text(root, width=45, height=15)
        self.text_area.pack()

    def add_contact(self):
        name = self.entry_name.get().strip()
        phone = self.entry_phone.get().strip()

        if not name or not phone:
            messagebox.showwarning("Warning", "Both fields are required.")
            return

        self.manager.add_contact(name, phone)
        messagebox.showinfo("Success", "Contact added!")
        self.view_contacts()

    def view_contacts(self):
        contacts = self.manager.read_contacts()
        self.text_area.delete("1.0", tk.END)

        if not contacts:
            self.text_area.insert(tk.END, "No contacts found.")
            return

        for name, phone in contacts:
            self.text_area.insert(tk.END, f"Name: {name} | Phone: {phone}\n")

    def update_contact(self):
        name = self.entry_name.get().strip()
        new_phone = self.entry_phone.get().strip()

        if not name or not new_phone:
            messagebox.showwarning("Warning", "Enter both name and new phone.")
            return

        success = self.manager.update_contact(name, new_phone)
        if success:
            messagebox.showinfo("Success", "Contact updated!")
        else:
            messagebox.showerror("Error", "Contact not found.")

        self.view_contacts()

    def delete_contact(self):
        name = self.entry_name.get().strip()

        if not name:
            messagebox.showwarning("Warning", "Enter a name to delete.")
            return

        success = self.manager.delete_contact(name)
        if success:
            messagebox.showinfo("Success", "Contact deleted!")
        else:
            messagebox.showerror("Error", "Contact not found.")

        self.view_contacts()

root = tk.Tk()
app = ContactApp(root)
root.mainloop()
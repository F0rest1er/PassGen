import random
import string
import tkinter as tk
import customtkinter

class PassGen:
    def __init__(self, root):
        self.root = root
        self.root.title("PassGen")

        self.create_widgets()

    def create_widgets(self):
        self.length_label = customtkinter.CTkLabel(self.root, text="Длина пароля:")
        self.length_label.pack()

        self.length_entry = customtkinter.CTkEntry(self.root)
        self.length_entry.pack()

        self.use_uppercase_var = tk.BooleanVar()
        self.use_uppercase_var.set(True)
        self.uppercase_check = customtkinter.CTkCheckBox(self.root, text="Заглавные буквы", variable=self.use_uppercase_var)
        self.uppercase_check.pack()

        self.use_lowercase_var = tk.BooleanVar()
        self.use_lowercase_var.set(True)
        self.lowercase_check = customtkinter.CTkCheckBox(self.root, text="Строчные буквы", variable=self.use_lowercase_var)
        self.lowercase_check.pack()

        self.use_digits_var = tk.BooleanVar()
        self.use_digits_var.set(True)
        self.digits_check = customtkinter.CTkCheckBox(self.root, text="Цифры", variable=self.use_digits_var)
        self.digits_check.pack()

        self.use_special_var = tk.BooleanVar()
        self.use_special_var.set(False)
        self.special_check = customtkinter.CTkCheckBox(self.root, text="Специальные символы", variable=self.use_special_var)
        self.special_check.pack()

        self.count_label = customtkinter.CTkLabel(self.root, text="Количество паролей:")
        self.count_label.pack()

        self.count_entry = customtkinter.CTkEntry(self.root)
        self.count_entry.pack()

        self.generate_button = customtkinter.CTkButton(self.root, text="Сгенерировать", command=self.generate_passwords)
        self.generate_button.pack()

        self.generated_passwords_text = customtkinter.CTkTextbox(self.root, height=150, width=300)
        self.generated_passwords_text.pack()

    def generate_passwords(self):
        length = int(self.length_entry.get())
        use_uppercase = self.use_uppercase_var.get()
        use_lowercase = self.use_lowercase_var.get()
        use_digits = self.use_digits_var.get()
        use_special = self.use_special_var.get()
        count = int(self.count_entry.get())

        characters = ""
        if use_uppercase:
            characters += string.ascii_uppercase
        if use_lowercase:
            characters += string.ascii_lowercase
        if use_digits:
            characters += string.digits
        if use_special:
            characters += string.punctuation

        passwords = []
        for _ in range(count):
            password = ''.join(random.choice(characters) for _ in range(length))
            if use_special:
                if len(password) > 1:
                    password = password[:1] + random.choice(string.punctuation) + password[1:]
            passwords.append(password)

        passwords_text = "\n".join(passwords)
        self.generated_passwords_text.delete(1.0, tk.END)
        self.generated_passwords_text.insert(tk.END, passwords_text)

if __name__ == "__main__":
    root = customtkinter.CTk()
    app = PassGen(root)
    root.mainloop()

import tkinter as tk
from tkinter import font

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Variable to store the expression
        self.expression = ""
        
        # Create the display
        self.display = tk.Entry(
            self.root,
            font=("Arial", 24),
            borderwidth=2,
            relief="solid",
            justify="right",
            bg="#f0f0f0"
        )
        self.display.pack(fill="both", padx=10, pady=20, ipady=10)
        
        # Create buttons frame
        buttons_frame = tk.Frame(self.root)
        buttons_frame.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Define button layout
        buttons = [
            ["C", "←", "/", "*"],
            ["7", "8", "9", "-"],
            ["4", "5", "6", "+"],
            ["1", "2", "3", "="],
            ["0", ".", "00", ""]
        ]
        
        # Create buttons
        for row in buttons:
            row_frame = tk.Frame(buttons_frame)
            row_frame.pack(fill="both", expand=True, pady=5)
            
            for btn_text in row:
                if btn_text == "":
                    # Empty space for layout
                    empty = tk.Frame(row_frame, bg="white")
                    empty.pack(side="left", fill="both", expand=True, padx=5)
                else:
                    btn = tk.Button(
                        row_frame,
                        text=btn_text,
                        font=("Arial", 18, "bold"),
                        command=lambda text=btn_text: self.on_button_click(text),
                        bg=self.get_button_color(btn_text),
                        fg="white",
                        relief="raised",
                        bd=2,
                        activebackground="#333"
                    )
                    btn.pack(side="left", fill="both", expand=True, padx=5)
    
    def get_button_color(self, text):
        """Return color based on button type"""
        if text == "C":
            return "#e74c3c"  # Red for clear
        elif text == "=":
            return "#27ae60"  # Green for equals
        elif text in ["←", "/", "*", "-", "+"]:
            return "#f39c12"  # Orange for operators
        else:
            return "#34495e"  # Dark gray for numbers
    
    def on_button_click(self, char):
        """Handle button clicks"""
        if char == "C":
            self.expression = ""
            self.display.delete(0, tk.END)
        
        elif char == "←":
            self.expression = self.expression[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)
        
        elif char == "=":
            try:
                result = eval(self.expression)
                self.display.delete(0, tk.END)
                self.display.insert(0, str(result))
                self.expression = str(result)
            except:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                self.expression = ""
        
        else:
            self.expression += str(char)
            self.display.delete(0, tk.END)
            self.display.insert(0, self.expression)

# Main program
if __name__ == "__main__":
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
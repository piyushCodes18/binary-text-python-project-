# binary-text-python-project-
# Description: This is a repository for a Binary to text and vice versa conversion project completely made in Python language

def text_to_binary(text):
   return ' '.join(format(ord(c), '08b') for c in text)
def binary_to_text(binary):
   try:
     return ''.join(chr(int(b, 2)) for b in binary.split())
   except ValueError:
     return "Invalid binary input!"
def main():
   while True:
     print("\n--- Binary Text Converter ---")
     print("1. Text → Binary\n2. Binary → Text\n3. Exit")
  choice = input("Enter choice (1/2/3): ").strip()
    if choice == "1":
       print("Binary:", text_to_binary(input("Enter text: ")))
   elif choice == "2":
     print("Text:", binary_to_text(input("Enter binary (bytes spaced): ")))
   elif choice == "3":
     print("Goodbye!")
      break
   else:
     print("Invalid choice!")
if __name__ == "__main__":
 main()

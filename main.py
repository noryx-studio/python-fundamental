# 2/8/2026

class Data:
    def __init__(self, id: int = 0, name: str = "", phone: str = ""):
        self.id = id
        self.name = name
        self.phone = phone
    
def CreateData(arr, name, phone):
    # Determine the next ID based on the last item in the list
    new_id = arr[-1].id + 1 if arr else 1
    # Create the object and append it to our list
    new_entry = Data(id=new_id, name=name, phone=phone)
    arr.append(new_entry)

def UpdateData(arr, id, name, phone):
    # Loop through objects and update the one with the matching ID
    for item in arr:
        if item.id == id:
            item.name = name
            item.phone = phone
            return 

def DeleteData(arr, id):
    # Overwrite list contents with everyone EXCEPT the specified ID
    arr[:] = [item for item in arr if item.id != id]

def PrintData(arr):
    # Check if the list is empty before trying to print
    if not arr:
        print("\n--- Table is empty ---")
        return

    # Print the Header
    # {:<5} means: align left, 5 spaces wide
    # {:<15} means: align left, 15 spaces wide
    print(f"\n{'ID':<5} | {'Name':<15} | {'Phone':<15}")
    print("-" * 40) # Print a separator line

    # Loop and print each row
    for item in arr:
        print(f"{item.id:<5} | {item.name:<15} | {item.phone:<15}")
    print("-" * 40)

# --- Execution ---

users = [
    Data(1, "Alice", "123-456"),
    Data(2, "Bob", "987-654"),
    Data(3, "Charlie", "555-789")
]

# Add new data
CreateData(users, "Thomas", "338-111")

# Update ID 2
UpdateData(users, 2, "Marlie", "232-000")

# Delete ID 1
DeleteData(users, 1)

# Display the final table
PrintData(users)

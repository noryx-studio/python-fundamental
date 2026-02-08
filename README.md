# Simple CRUD with Python
This project is a basic implementation of Create, Read, Update, and Delete (CRUD) operations. It uses a Python list to manage a collection of custom objects, mimicking how a simple database works.

### Overview
This system provides a clean way to handle structured data without needing external libraries. It features automatic ID incrementing and a formatted table display for easy data viewing.

### Core Functionality
* Create: Adds new entries and automatically assigns a unique ID by checking the last item in the list.

* Read: Displays the entire dataset in a cleanly aligned table using string formatting.

* Update: Finds a specific record by its unique ID and modifies the name and phone fields.

* Delete: Removes a record by ID using a memory-efficient list filtering method.

### Code Structure
#### Data Class
The Data class serves as the blueprint for each record, storing an integer id and string values for name and phone.

#### Methods
`
CreateData(arr, name, phone): Handles object instantiation and list appending.
`

`
PrintData(arr): Uses f-string alignment to print columns.
`

`
UpdateData(arr, id, name, phone): Iterates through the list to find a match.
`

`
DeleteData(arr, id): Uses list comprehension to remove a specific record.
`

Example Output
When PrintData is called, the system generates a formatted view:

```

ID    | Name            | Phone          
----------------------------------------
2     | Marlie          | 232-000        
3     | Charlie         | 555-789        
4     | Thomas          | 338-111        
----------------------------------------
```

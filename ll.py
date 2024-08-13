class Employee:
    def __init__(self, empName, department, netPay):
        self.empName = empName
        self.dept = department
        self.pay = netPay
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, empName, department, netPay):
        new_employee = Employee(empName, department, netPay)
        if self.head is None:
            self.head = new_employee
        else:
            new_employee.next = self.head
            self.head = new_employee
        
    def trav(self):
        t = self.head
        while t is not None:
            print(f"Name: {t.empName}, Dept: {t.dept}, NetPay: {t.pay}")
            t = t.next

# Create an instance of LinkedList
o = LinkedList()

# Insert employees into the linked list
o.insert("Roro", "CSE", 12)
o.insert("Jane", "Math", 15)

# Traverse the linked list and print employee details
o.trav()

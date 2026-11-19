class Requisition:

    requisition_counter = 0
    requisition_records = []

    def __init__(self,req_date,req_staff_id,req_staff_name):

        Requisition.requisition_counter += 1

        self.requisition_id = (Requisition.requisition_counter + 10000)

        self.date = req_date
        self.staff_id = req_staff_id
        self.staff_name = req_staff_name

        self.items = []
        self.total = 0.0

        self.status = ""
        self.approval_reference ="Not Available"

        Requisition.requisition_records.append(self)


    def add_requisition(self):
        print("\nAdd Items:")
        while True:

            item_name = input("Item Name: ")
            item_price = float(input("Item Price: $"))

            self.items.append(
                {
                    "name": item_name,
                    "price": item_price
                }
            )

            self.total += item_price
            again = input("Add another item? (yes/no): ").lower()

            if again == "no":
                break

    def requisition_approval(self):

        if self.total < 500:
            self.status = "Approved"

            self.approval_reference =(self.staff_id +str(self.requisition_id)[-3:])

        elif self.total <= 1000:
             self.status = "Pending"

        else:
            self.status = "Not approved"

    def display_requisition(self):
        print("=====Requisition Details=====")
        print(f"\nDate: {self.date}")
        print(f"Requisition ID: "f"{self.requisition_id}")

        print(f"Staff ID: "f"{self.staff_id}")

        print(f"Staff Name: "f"{self.staff_name}")

        if self.total == int(self.total):
            print(f"Total: ${self.total:.0f}")
        else:
            print(f"Total: ${self.total}")

        print(f"Status: {self.status}")

        print("Approval Reference Number:",self.approval_reference)

def requisition_statistics():

    approved = 0
    pending = 0
    not_approved = 0

    for req in Requisition.requisition_records:

        if req.status == "Approved":
            approved += 1

        elif req.status == "Pending":
            pending += 1

        elif req.status == "Not approved":
            not_approved += 1

    print("========Statistics=========")

    print("The total number of requisitions submitted:",len(Requisition.requisition_records))

    print("The total number of approved requisitions:",approved)

    print("The total number of pending requisitions:", pending)

    print("The total number of not approved requisitions:",not_approved)







number_of_requisitions = int(input("Enter number of requisitions: "))

for i in range(number_of_requisitions):

    print(f"\nEnter Details for "f"Requisition {i + 1}")

    date = input("Date: ")
    staff_id = input("Staff ID: ")
    staff_name = input("Staff Name: ")

    requisition = Requisition(
        date,
        staff_id,
        staff_name)

    requisition.add_requisition()

    requisition.requisition_approval()


for requisition in Requisition.requisition_records:

    requisition.display_requisition()

requisition_statistics()

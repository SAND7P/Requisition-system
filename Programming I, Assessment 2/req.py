class Requisition:

    requisition_counter = 0
    requisition_records = []

    def __init__(self,req_date,req_staff_id,req_staff_name):

        Requisition.requisition_counter += 1

        self.requisition_id = (
            Requisition.requisition_counter + 10000
        )

        self.date = req_date
        self.staff_id = req_staff_id
        self.staff_name = req_staff_name

        self.items = []
        self.total = 0.0

        self.status = ""
        self.approval_reference = "Not available"

        Requisition.requisition_records.append(self)


    def add_requisition(self):

        print("\nAdd Items:")

        while True:

            item_name = input("Item Name: ")
            item_price = float(
                input("Item Price: $")
            )

            self.items.append(
                {
                    "name": item_name,
                    "price": item_price
                }
            )

            self.total += item_price

            again = input(
                "Add another item? (yes/no): "
            ).lower()

            if again == "no":
                break

    def requisition_approval(self):

        if self.total < 500:

            self.status = "Approved"

            self.approval_reference = (
                self.staff_id +
                str(self.requisition_id)[-3:]
            )

        elif self.total <= 1000:

            self.status = "Pending"

        else:

            self.status = "Not approved"


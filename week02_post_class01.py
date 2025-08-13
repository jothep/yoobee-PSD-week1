from dataclasses import dataclass

@dataclass(slots=True)
class Employee:
    id: str #It is usually necessary to distinguish people by a unique ID.
    name: str
    salary: float
    job_title: str

    def display_info(self) -> None:
        print(
            f"id: {self.id}\n"
            f"name: {self.name}\n"
            f"salary: {self.salary}\n"
            f"job_title: {self.job_title}\n"
        )

    def give_raise(self, amount: float) -> None:
        self.salary += amount

def display_all(employees: list[Employee]) -> None:
    if not employees:
        print("No employees.")
        return
    for e in employees:
        e.display_info()

if __name__ == "__main__":
    e1 = Employee("E001", "Jothep", 2000.0, "Manager")
    e2 = Employee("E002", "JSK", 2300.0, "Dev")
    e3 = Employee("E003", "CZ", 1700.0, "QA")

    e2.give_raise(200.0) 
    print("Print once to verify functionality:")
    e2.display_info()

    all_members: list[Employee] = [e1, e2, e3]
    print("Print all members' info:")
    display_all(all_members)
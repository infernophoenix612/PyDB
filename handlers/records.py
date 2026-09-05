class Record:
    def __init__(self, name, age, branch):

        # Validate name
        if not name:
            raise ValueError("Name cannot be empty")

        # Validate age
        if not isinstance(age, int):
            raise ValueError("Age must be an integer")

        if age <= 0:
            raise ValueError("Age must be greater than 0")

        # Validate branch
        if not branch:
            raise ValueError("Branch cannot be empty")

        self.name = name
        self.age = age
        self.branch = branch

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Branch:", self.branch)

    def to_dict(self):
        return {
            "Name": self.name,
            "Age": self.age,
            "Branch": self.branch
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["Name"],
            int(data["Age"]),
            data["Branch"]
        )
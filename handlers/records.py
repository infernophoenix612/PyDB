class Record:
    def __init__(self, name, age, branch):
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
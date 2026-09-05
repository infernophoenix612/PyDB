from handlers.exceptions import InvalidRecordError


class Record:
    def __init__(self, name, age, branch):

        if not isinstance(name, str) or not name.strip():
            raise InvalidRecordError("Name cannot be empty")

        if not isinstance(age, int):
            raise InvalidRecordError("Age must be an integer")

        if age <= 0:
            raise InvalidRecordError("Age must be greater than 0")

        if not isinstance(branch, str) or not branch.strip():
            raise InvalidRecordError("Branch cannot be empty")

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
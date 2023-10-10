class User:
    def __init__(self, name, email, license) -> None:
        self.name = name
        self.email = email
        self.license = license

    def __str__(self) -> str:
        return f"Username: {self.name}\nEmail: {self.email}\nLicense #: {self.license}"

user1 = User("Jimmy", "jimmy@gimmy.com", "as;lkdjfao92wi3")
user2 = User("Johnny", "johnny@johnny.com", "a;lkm219o2wre")

print(user1)
print(user2)
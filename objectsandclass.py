#objects and class

class Person:
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone

    def greet(self, other_person):
        print(f"Hello {other_person.name}, I am {self.name}.")

sonny = Person("Sonny","sonny@hotmail.com","483-485-4948")
print(sonny.name)
print(sonny.email)
print(sonny.phone)
print("**********************")
jordan = Person("Jordan","jordan@aol.com","495-586-3456")
print(jordan.name)
print(jordan.email)
print(jordan.phone)
print("**********************")
sonny.greet(jordan)
print("**********************")
jordan.greet(sonny)

print("**********************")
print(f"""Here is Sonny's contact info:
Email: {sonny.email}
Phone Number: {sonny.phone}
""")
print("**********************")
print(f"""Here is Sonny's contact info:
Email: {jordan.email}
Phone Number: {jordan.phone}
""")

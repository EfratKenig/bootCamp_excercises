import random

from Document import Document
from Employee import Employee


class Clerk(Employee):
    def __init__(self, name, skills, salary=15000):
        super().__init__(name, salary)
        self.skills = skills

    def add_skill(self, skill):
        self.skills.append(skill)

    def work(self, office):
        """A function that pushes a random number of new documents (between 1-10)
        to the office documents list, and prints "<name> added <# of documents> documents".
         The document type should be one of the clerk skills
         """
        doc_type = self.skills[random.randrange(len(self.skills))] if len(self.skills) else "unknown"
        num_docs = random.randrange(1, 10)
        for i in range(num_docs):
            new_doc = Document(self.name, doc_type)
            office.documents.append(new_doc)
        print(self.name + " added " + str(num_docs) + " documents")

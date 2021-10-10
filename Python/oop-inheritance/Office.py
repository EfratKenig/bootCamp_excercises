from Cleaner import Cleaner
from Manager import Manager


class Office:
    def __init__(self, documents, managers, cleaners):
        self.documents = documents
        self.managers = managers
        self.cleaners = cleaners

    def hire_cleaner(self, name):
        """ adds a new cleaner """
        new_cleaner = Cleaner(name)
        self.cleaners.append(new_cleaner)

    def hire_manager(self, name):
        """ adds a new manager """
        new_manager = Manager([], name)
        self.managers.append(new_manager)

    def add_document(self, document):
        """ adds a document """
        self.documents.append(document)

    def start_work_day(self):
        """ make all managers and all cleaners work """
        for manager in self.managers:
            manager.work(self)
        for cleaner in self.cleaners:
            cleaner.work()

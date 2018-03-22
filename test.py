class Contact():

    def __init__(self, name, organisation, number):

        self.contact_list = [[name, organisation, number]]

    def add_entry(self, name, organisation, number):

        self.contact_list.append([name, organisation, number])

    def remove_entry(self, name, organisation):

        i = 0
        for each_item in self.contact_list:

            if (each_item[0].upper() == name.upper()) and (each_item[1].upper() == organisation.upper()):

                self.contact_list.pop(i)
            i += 1

    def __len__(self):

        return len(self.contact_list)

    def search_byname(self, name):

        i = 0
        for each_item in self.contact_list:
            if each_item[0].upper() == name.upper():
                return each_item
            i += 1


contr = Contact("Yury", "Coles", "95555555")
contr.add_entry("Yury1", "Coles1", "295555555")
contr.add_entry("Yury2", "Coles2", "295555555")
contr.add_entry("Yury3", "Coles3", "295555555")
contr.add_entry("Yury4", "Coles4", "295555555")
contr.add_entry("Yury5", "Coles5", "295555555")
print(contr.contact_list)
print(contr.__len__())
contr.remove_entry("Yury2", "Coles2")
print(contr.__len__())
print(contr.contact_list)

print(contr.search_byname('Yury3'))

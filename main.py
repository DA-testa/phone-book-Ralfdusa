class ContactList:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, number, name):
        self.contacts[number] = name

    def remove_contact(self, number):
        if number in self.contacts:
            del self.contacts[number]

    def find_contact(self, number):
        if number in self.contacts:
            return self.contacts[number]
        else:
            return 'not found'

def read_queries():
    n = int(input())
    queries = []
    for i in range(n):
        query = input().split()
        queries.append((query[0], int(query[1]), query[2] if len(query) == 3 else None))
    return queries

def process_queries(queries):
    result = []
    contact_list = ContactList()
    for query in queries:
        if query[0] == 'add':
            contact_list.add_contact(query[1], query[2])
        elif query[0] == 'del':
            contact_list.remove_contact(query[1])
        else:
            result.append(contact_list.find_contact(query[1]))
    return result

def write_responses(result):
    print('\n'.join(result))

if __name__ == '__main__':
    queries = read_queries()
    result = process_queries(queries)
    write_responses(result)

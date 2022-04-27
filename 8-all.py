'''Module to work with MongoDB
'''


def list_all(mongo_collection):
    '''Returns all documents in a collection
    '''
    return [i for i in mongo_collection.find()]

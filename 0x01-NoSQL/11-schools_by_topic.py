#!/usr/bin/env python3
'''Task 11 module
'''


def schools_by_topic(mongo_collection, topic):
    '''Returns the list of schools having a specific topic
    '''
    return [i for i in mongo_collection.find({
        'topics': {
            '$elemMatch': {
                '$eq': topic,
            },
        },
    })]

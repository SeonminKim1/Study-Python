
# https://www.py4u.net/discuss/168535
import mongomock

# mongomock - update
def test_update_one_with_upsert():
        # 1. get collection 
        collection = mongomock.MongoClient().db.collection

        # 2. insert
        filter_doc = {'_id': '2', 'field': 456}
        collection.insert(filter_doc)
        print('insert', collection.find({'field': 456}))

        # 3. update
        collection.update_one(filter = {'field':456}, update={'$set': {'field': 123}}, upsert=True)
        print('update', collection.find({'field': 123}))

        # 4. 최종 확인
        result_obj = collection.find_one(filter='2')
        print('result_obj', result_obj)
        assert result_obj['field'] == 123
# projectlist = [

# { 'projectid' : 1, 'en': 'the Forestias by MQDC', 'p_lat': '13.657199', 'p_lng': '100.667798'},
# { 'projectid' : 2, 'en': 'FLO by Sansiri', 'p_lat': '13.731885', 'p_lng': '100.503835'},
# { 'projectid' : 3, 'en': 'Elements Srinakarin', 'p_lat': '13.696393', 'p_lng': '100.645592'},
# { 'projectid' : 4, 'en': 'Chapter Charoennakorn Riverside', 'p_lat': '13.714368', 'p_lng': '100.504626'},

# ]

# from airtable import Airtable

from pyairtable import Table

# Connect to Airtable
my_api_token = 'patqeUrC7eLbBBjx5.3fa0ab9407f2512416c9ae44562fa2a83c5c4231022022c745b418e940e79667'
my_base_id = 'appoblgGwVGW6XWbQ'
my_table_id = 'tblgMYC6WGtDO11kL'
my_table_name = 'ant_nearby'

def air_deliver_data():
    table = Table(my_api_token, my_base_id, my_table_id)
    # print(table.all())

    new_recordset = []

    for record in table.all():
        new_record = {}
        new_record['projectid'] = record['fields']['projectid']
        new_record['en'] = record['fields']['en']
        new_record['p_lat'] = record['fields']['p_lat']
        new_record['p_lng'] = record['fields']['p_lng']
        new_recordset.append(new_record)

    new_recordset_sorted_reverse = sorted(new_recordset, key=lambda x: x['projectid'], reverse=False)

    print(new_recordset_sorted_reverse)

    return new_recordset_sorted_reverse

# air_deliver_data()

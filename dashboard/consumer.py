# %%
import json
from kafka import KafkaConsumer, KafkaAdminClient

# %%
# check the topics
admin_client = KafkaAdminClient(bootstrap_servers="localhost:9093", client_id='test')
admin_client.list_topics()

# %%
# To consume latest messages and auto-commit offsets
topic = 'ppeAvailabilityHospitalC'
consumer = KafkaConsumer(topic,
                         group_id='my-group',
                         bootstrap_servers=['localhost:9093'],
                         auto_offset_reset='earliest')
# for message in consumer:
#     print(message)
# %%
# consumer.partitions_for_topic(topic)

# seek to beginning
# consumer.seek_to_beginning()

while True:
    print('polling...')
    records = consumer.poll(timeout_ms=1000)
    for _, consumer_records in records.items():
        # Parse records
        for consumer_record in consumer_records:
            print(consumer_record.value)
        continue
# %%

# %%
import json
from kafka import KafkaProducer, KafkaAdminClient
from random import randint, choice
from time import sleep

# %%
# check the topics
admin_client = KafkaAdminClient(bootstrap_servers="localhost:9093", client_id="test")
admin_client.list_topics()
# %%
# To consume latest messages and auto-commit offsets
topic = "ppeAvailabilityHospitalC"
producer = KafkaProducer(
    bootstrap_servers=["localhost:9093"],
    value_serializer=lambda x: json.dumps(x).encode("utf-8"),
)
# %%
category_list = ["Mask", "Gloves", "Gowns", "Face Shields"]
product_list = ["N95 Masks", "Surgical Masks", "Gloves", "Gowns", "Face Shields"]
while True:
    try:
        msg = {
            "ID": f"103azaetf63hd{randint(0, 10000000000)}",
            "CATEGORY": choice(category_list),
            "PRODUCT": choice(product_list),
            "NUMBERofUNITS": randint(0, 10000),
        }
        producer.send(topic, value=msg)
        sleep(5)
    except KeyboardInterrupt:
        break

# %%

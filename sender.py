import json
from google.cloud import pubsub_v1
from os import getenv

PROJECT_ID = getenv('GCP_PROJECT')
TOPIC_NAME = getenv('TOPIC_NAME')
RECIPIENTS = getenv('RECIPIENTS', '').split(',')

publisher = pubsub_v1.PublisherClient()
TOPIC = publisher.topic_path(PROJECT_ID, TOPIC_NAME)


def main():
    dict_data = {
        'subject': 'Test email from pubsub',
        'recipients': RECIPIENTS,
        'message': 'Test email body'
    }
    json_data = json.dumps(dict_data)
    _ = publisher.publish(TOPIC, data=json_data.encode())
    print(f'Message sent to topic: {TOPIC_NAME}')

if __name__ == '__main__':
    main()

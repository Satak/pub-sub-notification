def send_email(subject, recipients, message):
    """Email sender function
    Expecting these environment variables:
    SENDER (email address)
    SMTP_SERVER
    SMTP_USERNAME
    SMTP_PASSWORD
    """
    import smtplib
    from email.message import EmailMessage
    from os import getenv

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = getenv('SENDER')
    msg['To'] = recipients
    msg.set_content(message)
    with smtplib.SMTP_SSL(getenv('SMTP_SERVER'), 465) as smtp:
        smtp.login(getenv('SMTP_USERNAME'), getenv('SMTP_PASSWORD'))
        smtp.send_message(msg)
        print(f'Email sent to {recipients}')


def notification(data, context):
    """Background Cloud Function to be triggered by Pub/Sub.
    Args:
         data (dict): The dictionary with data specific to this type of event.
         data has data key that contains the actual data as base64 encoded string
         this specific function expects that the string contains a json object
         context (google.cloud.functions.Context): The Cloud Functions event
         metadata.
    """
    import base64
    import json
    import logging

    if 'data' not in data:
        print('Message without data')
        return None

    try:
        message_dict = json.loads(base64.b64decode(data['data']))
        expected_keys = ('subject', 'recipients', 'message')
        if isinstance(message_dict, dict) and all(key in message_dict for key in expected_keys):
            send_email(
                subject=message_dict['subject'],
                recipients=message_dict['recipients'],
                message=message_dict['message']
            )
        else:
            logging.error(f'Data schema is wrong: {message_dict} expected keys: {expected_keys}')
    except Exception as err:
        logging.error(f'Error while trying to decode the data: {err}')

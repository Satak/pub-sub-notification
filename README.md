# Email Notification Function

Simple GCP cloud function that sends email messages from Pub/Sub messages. Expected Pub/Sub topic name: `notification`

## Prerequisites

- Create GCP project
- Enable Pub/Sub
- Create topic called `notification`
- Create `env.yaml` file and enter these according to your environment. For example use gmail or AWS SES.

### `env.yaml`

You need to create this yaml file with this content or pass the environment variables in command line for `gcloud functions deploy` command.

```yaml
SENDER: <email address>
SMTP_SERVER: <server name>
SMTP_USERNAME: <username>
SMTP_PASSWORD: <password>
```

### AWS SES

If you use AWS SES you need to first validate sender and receiver email addresses

## Deploy

Run the `deploy.ps1` Powershell script or use run this command:

`gcloud functions deploy notification --runtime python37 --trigger-topic notification --project <gcpProjectId> --region <region> --env-vars-file env.yaml --source ./src`

## `sender.py`

It requires these environment variables:

- `GOOGLE_APPLICATION_CREDENTIALS` (path to your service account `json` file)
- `GCP_PROJECT`
- `TOPIC_NAME` (gcp pub/sub topic)
- `RECIPIENTS` (comma separated string with email recipients. Example: `test@test.com,another@domain.com`)

## Message structure

Message is simple python dict object that is stringified with `json.dumps` and encoded to bytes since Pub/Sub `data` section expects the data be bytes.

```python
{
    'subject': 'Subject string',
    'recipients': ['email@domain.com', 'another@domain.com'],
    'message': 'Message body as string'
}
```

## Architecture

![UI Main](/img/pubsub-notification.png)

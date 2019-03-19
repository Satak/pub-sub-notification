# Email Notification Function

Simple GCP cloud function that sends email messages from Pub/Sub messages.

## Prerequisites

- Create GCP project
- Enable Pub/Sub
- Create topic called `notification`
- Create `env.yaml` file and enter these according to your environment. For example use gmail or AWS SES.

### `env.yaml`

```yaml
SENDER: <email address>
SMTP_SERVER: <server name>
SMTP_USERNAME: <username>
SMTP_PASSWORD: <password>
```

### AWS SES

If you use AWS SES you need to first validate sender and receiver email addresses

## `sender.py`

It requires these environment variables:

- `GCP_PROJECT`
- `TOPIC_NAME` (gcp pub/sub topic)
- `RECIPIENTS` (comma separated string with email recipients. Example: `test@test.com,another@domain.com`)

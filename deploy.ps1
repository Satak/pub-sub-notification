param (
    [Parameter(Mandatory)]
    [string]$Project,
	$Region="europe-west1"
)

gcloud functions deploy notification --runtime python37 --trigger-topic notification --project $Project --region $Region --env-vars-file env.yaml --source ./src

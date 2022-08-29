# converter
converting values


gcloud container clusters create --machine-type=e2-medium migration-cluster 
gcloud container clusters get-credentials migration-cluster 

docker push gcr.io/poc-sandy/cloudruntest:1.0.0
docker images
docker push us.gcr.io/poc-sandy/cloudruntest:1.0.0


docker tag cloudruntest:1.0.0 us.gcr.io/poc-sandy/cloudruntest:1.0.0
docker tag cloudruntest:1.0.0  gcr.io/poc-sandy/cloudruntest:1.0.0

docker build -t cloudruntest:1.0.0 .
docker pull in28min/todo-web-application-h2:0.0.1-SNAPSHOT


docker tag in28min/todo-web-application-h2:0.0.1-SNAPSHOT  gcr.io/app-mod-gebu-trainees/todo-web-app:1.0.0
docker push gcr.io/app-mod-gebu-trainees/todo-web-app:1.0.0


kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

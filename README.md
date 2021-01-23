# ScalableAPI

Simple API interface that takes a json object as reverses the order 


## Test
```bash
cd scalableapi
python3 manage.py test --settings=app.settings_testing
```

## Architecture

The app is scaled horizontially and traffic is distributed using a Loadbalancer, Kubernetes HPA (Horizontal Pod Autoscaler) is used to scale to demand 


https://raw.githubusercontent.com/hyperioxx/ScalableAPI/main/assets/scalableapi.png

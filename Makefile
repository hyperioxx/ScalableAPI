deploy:
	@echo "Deploying current configuration..."
	kubectl apply -f scalableapi.yaml
build:
	@echo "Building Docker Image..."
	docker build --tag hyperioxx/scalableapi:latest .
push:
	@echo "Pushing Docker Image..."
	docker push hyperioxx/scalableapi:latest

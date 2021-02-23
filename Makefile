run-frontend:
	cd frontend/covid_calc && \
		npm run start

run-backend:
	-@export FLASK_ENV=development
	-@set FLASK_ENV=development
	cd backend && \
		flask run

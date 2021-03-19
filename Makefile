run-frontend:
	cd frontend/covid_calc && \
		npm run start

run-backend:
	-@export FLASK_ENV=app.py
	-@set FLASK_ENV=app.py
	cd backend && \
		flask run

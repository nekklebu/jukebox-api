FROM	python:3.11-slim
WORKDIR	/app
COPY	./	/app/
ENV	PORT=4040
ENV	FLASK_APP=app.py
RUN	pip install --upgrade pip \
	&& pip install -r requirements.txt
RUN	apt-get update && apt-get install -y \
	bash
CMD	["bash","-c","python -m flask run --host=0.0.0.0 --port=${PORT:-4040} --no-debugger --no-reload"]

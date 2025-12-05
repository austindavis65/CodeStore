FROM python:3.9
EXPOSE 8080
WORKDIR /usr/src/app
COPY requirements.txt .
RUN apt update && apt install -y fortune
RUN pip install --no-cache-dir -r requirements.txt
COPY fortune.py ./.
CMD ["gunicorn", "-b", "0.0.0.0:8080", "fortune:__hug_wsgi__"]


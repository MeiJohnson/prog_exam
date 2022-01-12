FROM python:3.9
LABEL maintainer="meikojeiko@gmail.com"

RUN apt-get update
RUN mkdir /app
COPY . /app/
WORKDIR /app
EXPOSE 9000
CMD ["python", "-m", "http.server", "9000"]
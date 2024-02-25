FROM python:3.10
EXPOSE 5000
WORKDIR /app
COPY . .
RUN pip install -r requirments.txt 
CMD ["flask", "run", "--host", "0.0.0.0"]

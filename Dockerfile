FROM python:3

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
#RUN pip uninstall tf-nightly
RUN pip install tensorflow --upgrade --force-reinstall
COPY . .

EXPOSE 5000

CMD ["python", "run.py"]
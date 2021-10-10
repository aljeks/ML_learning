FROM agrigorev/zoomcamp-model:3.8.12-slim

RUN pip install pipenv scikit-learn numpy flask gunicorn

WORKDIR /app

COPY ["Pipfile", "Pipfile.lock", "./"]

RUN pipenv install --system --deploy

COPY ["Homework_05.py", "model1.bin", "dv.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "Homework_05:app"]

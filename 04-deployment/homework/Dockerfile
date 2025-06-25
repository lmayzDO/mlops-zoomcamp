FROM agrigorev/zoomcamp-model:mlops-2024-3.10.13-slim

# Install dependencies
RUN pip install -U pip
RUN pip install pipenv 
RUN pip install numpy
RUN pip install pandas
RUN pip install scikit-learn
RUN pip install pyarrow

WORKDIR /app

COPY [ "Pipfile", "Pipfile.lock", "./" ]

RUN pipenv install --system --deploy

COPY [ "predict.py", "./" ]

EXPOSE 9696

ENTRYPOINT [ "python3", "predict.py" ]
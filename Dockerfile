FROM inseefrlab/onyxia-python-minimal

COPY . /app
WORKDIR /app

RUN pip --no-cache-dir install -r requirements.txt

EXPOSE 8000
ENTRYPOINT ["uvicorn", "main:app", "--reload"]
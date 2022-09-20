FROM inseefrlab/onyxia-python-minimal

COPY . /app
WORKDIR /app
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000
ENTRYPOINT ["uvicorn", "main:app", "--reload"]

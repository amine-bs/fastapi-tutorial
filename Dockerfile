FROM inseefrlab/onyxia-python-minimal

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt --find-links https://download.pytorch.org/whl/cu113

EXPOSE 8000
ENTRYPOINT ["uvicorn", "main:app", "--reload"]

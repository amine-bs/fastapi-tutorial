FROM inseefrlab/onyxia-python-minimal

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt 

EXPOSE 8000
ENTRYPOINT ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0"]

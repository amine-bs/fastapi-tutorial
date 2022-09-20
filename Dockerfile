FROM inseefrlab/onyxia-python-minimal

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt --find-links https://download.pytorch.org/whl/cu113

EXPOSE 80
ENTRYPOINT ["uvicorn", "main:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "80"]

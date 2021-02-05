FROM python
RUN pip install Flask
RUN pip install exoscale
COPY autoscaler_3.py /
ENTRYPOINT ["python", "/autoscaler_3.py"]
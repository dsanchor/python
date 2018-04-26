FROM registry.access.redhat.com/rhscl/python-36-rhel7:1-12
RUN mkdir /tmp/app
WORKDIR /tmp/app
COPY main.py /tmp/app/main.py
COPY requirements.txt /tmp/app/requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8888
ENTRYPOINT ["python"]
CMD ["main.py"]
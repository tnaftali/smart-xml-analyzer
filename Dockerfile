FROM alpine:3.10
RUN apk update && apk add --no-cache python3
WORKDIR /app
COPY . /app
RUN pip3 install --trusted-host pypi.python.org -r requirements.txt
ENV FILE1 ""
ENV FILE2 ""
ENV ELEMENT_ID ""
CMD ["python3", "-i", "app.py $FILE1 $FILE2 $ELEMENT_ID"]
FROM  python:3.10-bullseye

ENV PYTHONUNBUFFERED=1

WORKDIR /

COPY Pipfile /

COPY Pipfile.lock /

RUN pip install pipenv

RUN pipenv install --deploy --ignore-pipfile

COPY . ./

RUN ["chmod", "+x", "entrypoint.sh"]

EXPOSE 5000

ENTRYPOINT [ "./entrypoint.sh" ]

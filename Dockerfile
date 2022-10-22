FROM node:18.10-bullseye AS builder

WORKDIR /betula
COPY . .

# build the vue frontend
RUN npm install
RUN npm run build


FROM python:3.10.7-bullseye AS runner

# copy data from repo
COPY --from=builder /betula /betula
WORKDIR /betula

#install python packages
RUN pip install -r requirements.txt

#install wsgi server
RUN pip install gunicorn

WORKDIR /betula/api

#create directories for images and data
RUN mkdir /data
RUN mkdir /photos

#run with wsgi server
CMD [ "gunicorn", "-b", "0.0.0.0:5000", "app:app" ]

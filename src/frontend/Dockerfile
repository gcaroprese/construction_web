FROM node:0.10.33
MAINTAINER Joni Bekenstein <jonibekenstein@gmail.com>

RUN npm install --global gulp@3.8.10 bower@1.3.12

COPY package.json /app/src/frontend/
RUN ln -s /app/src/frontend/package.json /app/package.json
RUN cd /app/ && npm install

COPY bower.json /app/src/frontend/
RUN ln -s /app/src/frontend/bower.json /app/bower.json
RUN cd /app/ && bower --allow-root install

WORKDIR /app
VOLUME /app/static-compiled
EXPOSE 3000

ENTRYPOINT ["gulp", "--color", "--gulpfile", "src/frontend/gulpfile.coffee"]
CMD ["--tasks"]

COPY . /app/src/frontend

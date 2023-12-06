FROM nginx:alpine

WORKDIR /

RUN rm -rf /usr/share/nginx/html/*

COPY index.html /usr/share/nginx/html

EXPOSE 80

ENTRYPOINT ["nginx", "-g", "daemon off;"]




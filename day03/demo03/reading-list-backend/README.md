# reading-list-backend

The frontend code have written in React, find out [here](https://github.com/faysalmehedi/reading-list-frontend.git)

### App running instructions:

```console
sudo apt update
sudo apt install docker.io

git clone https://github.com/faysalmehedi/reading-list-backend.git
cd reading-list-backend

sudo docker build . -t reading-list-backend
sudo docker run -p 5000:5000 -d \
                    -e POSTGRES_HOST=<backend_address> \
                    -e POSTGRES_PORT=5432 \
                    -e POSTGRES_USER=<postgres_user> \
                    -e POSTGRES_PASSWORD=<postgres_password>  \
                    -e POSTGRES_DB=<db_name>  \
                    --name backend reading-list-backend
```

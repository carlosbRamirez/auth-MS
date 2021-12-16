FROM python:3
#se crea una variable de entorno
#es como una variable pero que se crea dentro de mi sistema operativo
#la puedo llamar en mi programa cuando quiera
ENV PYTHONUNBUFFERED 1
RUN mkdir /users
WORKDIR /users
#agregue todo lo que esta en la raiz de la carpeta o proyecto
ADD . /users/
RUN pip install -r requirements.txt
EXPOSE 8080
CMD python manage.py makemigrations && python manage.py migrate && python manage.py runserver 0.0.0.0:$PORT
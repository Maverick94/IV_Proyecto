FROM python:3

MAINTAINER Andrés J Gallardo

RUN apt-get install -y git
RUN git clone https://github.com/Maverick94/IV_Proyecto.git
RUN pip3 install -r IV_Proyecto/requirements.txt

EXPOSE 5000

CMD cd IV_Proyecto && gunicorn API_web:__hug_wgsi__

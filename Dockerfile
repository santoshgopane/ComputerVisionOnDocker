FROM  python:3.6

RUN apt update
RUN apt install python3 -y

WORKDIR /usr/app/src

COPY requirements.txt ./

RUN apt-get update && apt-get install -y libgl1-mesa-glx
RUN pip install --upgrade pip 
RUN pip install -r requirements.txt

COPY MyFirstDockerCode.py ./

COPY FaceDetectionModelV4.model ./
COPY NNmodelv2.h5 ./
COPY facenet_keras.h5 ./

CMD ["python3", "./MyFirstDockerCode.py"]
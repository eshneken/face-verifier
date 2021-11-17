FROM python:3.8 as build-stage
WORKDIR /function
ADD requirements.txt /function/

			RUN pip3 install --target /python/  --no-cache --no-cache-dir -r requirements.txt &&\
			    rm -fr ~/.cache/pip /tmp* requirements.txt func.yaml Dockerfile .venv &&\
			    chmod -R o+r /python
RUN pip3 install --upgrade pip
RUN pip3 install --target /python/  --no-cache --no-cache-dir numpy
RUN pip3 install --target /python/  --no-cache --no-cache-dir pandas
RUN pip3 install --target /python/  --no-cache --no-cache-dir gdown
RUN pip3 install --target /python/  --no-cache --no-cache-dir tqdm
RUN pip3 install --target /python/  --no-cache --no-cache-dir Pillow
RUN pip3 install --target /python/  --no-cache --no-cache-dir opencv-python
RUN pip3 install --target /python/  --no-cache --no-cache-dir opencv-contrib-python
RUN pip3 install --target /python/  --no-cache --no-cache-dir tensorflow==1.9.0
RUN pip3 install --target /python/  --no-cache --no-cache-dir keras
RUN pip3 install --target /python/  --no-cache --no-cache-dir deepface --no-deps
ADD . /function/
RUN rm -fr /function/.pip_cache
FROM python:3.8-slim
WORKDIR /function
COPY --from=build-stage /python /python
COPY --from=build-stage /function /function
RUN chmod -R o+r /function
RUN apt-get update
RUN apt-get install -y libglib2.0-0
RUN apt-get install ffmpeg libsm6 libxext6  -y
ENV PYTHONPATH=/function:/python
ENV DEEPFACE_HOME=/tmp
ENV HOME=/tmp
#ENTRYPOINT ["/python/bin/fdk", "/function/func.py", "handler"]
ENTRYPOINT ["/bin/sh"]

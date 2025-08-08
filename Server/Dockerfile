FROM python:3.13-slim 

WORKDIR /app

ENV NODE_VERSION="v22.18.0"
ENV PY_DIR="./Scripts"

RUN apt -y update
RUN apt -y upgrade

# install node
ENV NODE="/app/node/bin"
RUN apt install -y curl xz-utils
RUN curl https://nodejs.org/dist/$NODE_VERSION/node-$NODE_VERSION-linux-x64.tar.xz -o ./node.tar.xz
RUN mkdir tempNode && tar -xf node.tar.xz -C tempNode && mv tempNode/* node && rm -r tempNode node.tar.xz
ENV PATH="$NODE:$PATH"

# libraqm build (this is a dependecy for Pillow)
RUN curl -L https://github.com/HOST-Oman/libraqm/releases/download/v0.10.3/raqm-0.10.3.tar.xz -o raqm-0.10.3.tar.xz && tar -xf raqm-0.10.3.tar.xz
RUN apt-get install -y libfreetype6-dev libharfbuzz-dev libfribidi-dev meson gtk-doc-tools
WORKDIR /app/raqm-0.10.3
RUN meson build
RUN ninja -C build
RUN ninja -C build install

WORKDIR /app

COPY . .

# download dependencies
RUN python3 -m venv $PY_DIR/.pyenv
RUN "$PY_DIR/.pyenv/bin/pip" install -r $PY_DIR/requirements.txt
RUN npm i

CMD ["npm", "run", "dev"]
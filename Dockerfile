From   manimcommunity/manim

USER root
RUN apt update && apt install -y vim 
USER manimuser
RUN pip install --upgrade pip && pip install manim_chemistry jupyterlab-language-pack-ja-JP manim_plugintemplate

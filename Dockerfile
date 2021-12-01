# FROM manimcommunity/manim:v0.12.0
FROM 3b1b/manimgl:v1.2.0

COPY --chown=manimuser:manimuser . /manim

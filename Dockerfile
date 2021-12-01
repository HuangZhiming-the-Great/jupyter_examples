# FROM manimcommunity/manim:v0.12.0
FROM 3b1b/manim:v1.2.0

COPY --chown=manimuser:manimuser . /manim

FROM manimcommunity/manim:v0.12.0
# FROM 3b1b/manim:v1.2.0
# It seems I can't use 3b1b's manim use this way.
COPY --chown=manimuser:manimuser . /manim

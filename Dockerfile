FROM squidfunk/mkdocs-material:9

RUN pip install --no-cache-dir \
  mkdocs-gen-files \
  markdown-include

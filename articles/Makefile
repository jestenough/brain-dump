DOCKER_IMAGE ?= article-builder
DOCKER_TAG ?= v0

IMAGE := $(DOCKER_IMAGE):$(DOCKER_TAG)

OUT_DIR := $(shell pwd)/dist

.PHONY: build run clean help clean-image

all: build compile clean clean-image

help:
	@echo "Available commands:"
	@echo "  make build                  - Build Docker image"
	@echo "  make compile key=key        - Compile LaTeX file inside Docker"
	@echo "                               Output PDF will be in ./dist"
	@echo "  make clean                  - Remove auxiliary LaTeX files from ./dist"
	@echo "  make clean-image            - Remove Docker image"
	@echo ""
	@echo "Example:"
	@echo "  make compile FILE=main.tex"

build:
	@docker build -t $(IMAGE) ./articles

compile:
	@docker run --rm -it -v $(OUT_DIR):/app/dist $(IMAGE) -k $(key) $(if $(langs),-l $(langs))

clean:
	@rm -f $(OUT_DIR)/*.aux $(OUT_DIR)/*.log $(OUT_DIR)/*.fls $(OUT_DIR)/*.fdb_latexmk $(OUT_DIR)/*.synctex.gz

clean-image:
	@docker rmi $(IMAGE) || echo "Image not found"

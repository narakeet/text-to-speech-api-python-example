DOCKER_IMAGE := python:3.7
run:
	@[[ ! -z "$(NARAKEET_API_KEY)" ]] || (echo "NARAKEET_API_KEY not set" && exit 1)
	docker run -it --rm -eNARAKEET_API_KEY=$(NARAKEET_API_KEY) -v $(shell pwd):/data -w /data --entrypoint /bin/bash $(DOCKER_IMAGE) -c "pip install -r requirements.txt && python tts.py"


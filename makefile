tag := 'docusaurus-test'
name := 'instant-docusaurus-server'
target := 'website.config.json'


.PHONY: build-docker
build-docker: build-docusaurus-docker, build-mdconverter-docker;


.PHONY: build-docusaurus-docker
build-docusaurus-docker:
	@docker build \
		-t $(tag) \
		--build-arg WEBSITE_TARGET_DIRECTORY=$(target) \
	.

.PHONY: build-mdconverter
build-mdconverter:
	@docker build \
		-t mdconverter \
		-f ./mdconverter/Dockerfile \
		./mdconverter

.PHONY: run-docusaurus-docker
run-docusaurus-docker:
	@docker run --rm -i -t \
		--name ${name} \
		-e PORT=8080 \
		-e HOST=0.0.0.0 \
		-p 8080:8080 \
		$(tag) \
		$(cmd)

.PHONY: run-mdconverter
run-mdconverter:
	@docker run --rm -i -t \
		--name proc-mdconverter \
		-v `pwd`/report:/app/input \
		-v `pwd`/mdconverter/output:/app/output/ \
		mdconverter \
		$(cmd)

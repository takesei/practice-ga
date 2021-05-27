tag := 'docusaurus-test'
name := 'instant-docusaurus-server'
target := 'website.config.json'


.PHONY: build-docker
build-docusaurus-docker:
	@docker build \
		-t $(tag) \
		--build-arg WEBSITE_TARGET_DIRECTORY=$(target) \
	.

.PHONY: run-docusaurus-docker
run-docusaurus-docker:
	@docker run --rm -i -t \
		--name ${name} \
		-e PORT=8080 \
		-e HOST=0.0.0.0 \
		-p 8080:8080 \
		$(tag) \
		$(cmd)

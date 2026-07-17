# Deploy the quiz web app to the VPS.
#
#   make deploy          # sync web/ + data/ (text only) and (re)start the container
#   make deploy-logs     # tail the remote container logs
#
# Media (video/audio) never leaves the machine — the web app only needs
# conspect.md / quiz.json / info.md. The remote attempts DB
# (quiz_results.db) is never overwritten by a deploy: the VPS accumulates
# its own attempts. To seed it once from the local DB:
#   scp data/quiz_results.db $(DEPLOY_HOST):$(DEPLOY_DIR)/data/
#
# DEPLOY_HOST is machine-specific: set it in deploy.local.mk (gitignored),
#   DEPLOY_HOST = user@your-vps
# or pass it on the command line: make deploy DEPLOY_HOST=user@your-vps

-include deploy.local.mk

DEPLOY_HOST ?=
DEPLOY_DIR  ?= /opt/lectorium

.PHONY: deploy deploy-logs

deploy: check-deploy-host
deploy-logs: check-deploy-host

.PHONY: check-deploy-host
check-deploy-host:
ifeq ($(strip $(DEPLOY_HOST)),)
	$(error DEPLOY_HOST is not set — put it in deploy.local.mk or pass DEPLOY_HOST=user@host)
endif

deploy:
	ssh $(DEPLOY_HOST) 'mkdir -p $(DEPLOY_DIR)'
	rsync -az --delete \
		--exclude 'node_modules' \
		--exclude '.next' \
		web docker-compose.prod.yml $(DEPLOY_HOST):$(DEPLOY_DIR)/
	rsync -az --delete \
		--exclude '*.mp4' --exclude '*.mov' --exclude '*.mkv' --exclude '*.webm' \
		--exclude '*.wav' --exclude '*.mp3' --exclude '*.m4a' \
		--exclude 'quiz_results.db' \
		data $(DEPLOY_HOST):$(DEPLOY_DIR)/
	ssh $(DEPLOY_HOST) 'cd $(DEPLOY_DIR) && docker compose -f docker-compose.prod.yml up -d --build'

deploy-logs:
	ssh $(DEPLOY_HOST) 'cd $(DEPLOY_DIR) && docker compose -f docker-compose.prod.yml logs -f --tail 100'

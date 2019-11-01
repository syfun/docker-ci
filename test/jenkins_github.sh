#!/user/bin/env bash
curl -X POST -H "Content-Type: application/json" https://jenkins-local.teletraan.io/github-webhook/ -d @test/github-payload.json

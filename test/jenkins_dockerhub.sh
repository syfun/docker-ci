#!/user/bin/env bash
curl -X POST -H "Content-Type: application/json" https://jenkins-cn.teletraan.io/dockerhub-webhook/notify -d @test/dockerhub-payload.json

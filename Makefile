NETWORK_NAME = super-network
NETWORK_GATEWAY = 10.10.0.1
NETWORK_SUBNET = 10.10.0.0/16

# ネットワークの作成
upnet:
	@if [ -z "`docker network ls | grep $(NETWORK_NAME)`" ]; then docker network create --gateway $(NETWORK_GATEWAY) --subnet $(NETWORK_SUBNET) $(NETWORK_NAME); fi
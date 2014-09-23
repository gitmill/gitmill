.PHONY: all
all: ssh_host_dsa_key ssh_host_rsa_key ssh_host_ecdsa_key ssh_host_ed25519_key

ssh_host_dsa_key:
	ssh-keygen -t dsa -N "" -f ssh_host_dsa_key

ssh_host_rsa_key:
	ssh-keygen -t rsa -N "" -f ssh_host_rsa_key

ssh_host_ecdsa_key:
	ssh-keygen -t ecdsa -N "" -f ssh_host_ecdsa_key

ssh_host_ed25519_key:
	ssh-keygen -t ed25519 -N "" -f ssh_host_ed25519_key

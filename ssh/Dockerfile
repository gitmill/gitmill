FROM dockerfile/python

RUN export DEBIAN_FRONTEND=noninteractive && \
    apt-get update && \
    apt-get install -y ssh git && \
    rm -f /etc/ssh/ssh_host_* && \
    rm -rf /var/lib/apt/lists/* && \
    pip install requests

RUN adduser --system --shell /bin/sh --group --disabled-password --home /home/git --uid 888 git

ADD gitmill-keys /usr/local/bin/gitmill-keys
ADD gitmill-serve /usr/local/bin/gitmill-serve

ADD ssh_host_rsa_key /etc/ssh/ssh_host_rsa_key
ADD ssh_host_rsa_key.pub /etc/ssh/ssh_host_rsa_key.pub
ADD ssh_host_dsa_key /etc/ssh/ssh_host_dsa_key
ADD ssh_host_dsa_key.pub /etc/ssh/ssh_host_dsa_key.pub
ADD ssh_host_ecdsa_key /etc/ssh/ssh_host_ecdsa_key
ADD ssh_host_ecdsa_key.pub /etc/ssh/ssh_host_ecdsa_key.pub
ADD ssh_host_ed25519_key /etc/ssh/ssh_host_ed25519_key
ADD ssh_host_ed25519_key.pub /etc/ssh/ssh_host_ed25519_key.pub

RUN chmod 0555 /usr/local/bin/gitmill-* && \
    mkdir -p /var/run/sshd && \
    echo "PasswordAuthentication no" >> /etc/ssh/sshd_config && \
    echo "AuthorizedKeysCommand /usr/local/bin/gitmill-keys" >> /etc/ssh/sshd_config && \
    echo "AuthorizedKeysCommandUser root" >> /etc/ssh/sshd_config && \
    echo "AllowUsers git" >> /etc/ssh/sshd_config

CMD /usr/sbin/sshd -D

EXPOSE 22

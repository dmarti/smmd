# smmd

[Surveillance Marketing Meta Directory](https://dmarti.github.io/smmd/)

Goals: generate reports of differences among various
directories of surveillance marketing companies,
to help keep all resources up to date.


## Contributing

Send a pull request to the `gh-pages` branch.  The site is built from this branch.

Questions or feature requests, please file an issue.


## Previewing locally

### Installing on Linux

Install Docker from the package manager and start it
with the service manager.  For Fedora:

```
sudo dnf install docker
sudo systemctl start docker
```

### Installing on Mac OS 

[Install Docker Desktop for
Mac](https://docs.docker.com/docker-for-mac/install/).
(You do not need to make a Docker Hub account, just
start Docker.)

### Check your Docker install

Test that you can connect to the Docker daemon with:

```
docker ps
```

If you can't connect and get an error, you may need to
add yourself to the `docker` group and restart Docker.

```
sudo groupadd docker && sudo gpasswd -a ${USER} docker && sudo systemctl restart docker
newgrp docker
```

### Starting a preview

Run the script `preview.sh` and navigate your browser to http://localhost:4000/



## Credits

https://github.com/caprivacy/ -- CAPrivacy list.

See LICENSE.caprivacy for license.

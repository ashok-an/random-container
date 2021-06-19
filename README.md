### Description
  Launches a demo container (exposed on port `5000`) and prints some data

### Use
  For testing load balancers

### Dockerhub image name
  `ashoka007/random-bg-color`

### Test run
```
$ docker-compose up --scale random-bg=3 -d
```
Browse to [nginx-url](0.0.0.0:4000) (and refresh)
